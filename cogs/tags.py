import discord
from discord.ext import commands
import os.path
import os
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.query import *
from whoosh.query import Every
from whoosh.qparser import QueryParser
from whoosh.writing import AsyncWriter



class Tags(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(unique=True), tags=KEYWORD, icon=STORED, editor=TEXT(stored=True))
  


  @commands.command()
  async def make(self, ctx, name, *, content: commands.clean_content):
    if not os.path.exists("index"):
      os.mkdir("index")
      ix = create_in("index", self.schema)
      ix = open_dir("index")
    else:
      ix = open_dir("index")
    writer = AsyncWriter(ix)
    writer.update_document(title=name, content=content, path=name, editor=str(ctx.message.author))

    writer.commit()
    await ctx.send(f"Created tag {name}")
  
  @commands.command()
  async def show(self, ctx, *, name):
    if not os.path.exists("index"):
      os.mkdir("index")
      ix = create_in('index', self.schema)
      ix = open_dir('index')
    else:
      ix = open_dir("index")
    with ix.searcher() as searcher:
      parser = QueryParser('title', schema=ix.schema)
      query = parser.parse(name)
      corrected = searcher.correct_query(query, name, maxdist=2)
      if corrected.query != query:
        await ctx.send(f"Tag not found. Did you mean: {corrected.string}?")
      else:
        results = searcher.search(query)
        await ctx.send(results[0]['content'])
  
  @commands.command()
  async def edit(self, ctx, name, *, content: commands.clean_content):
    if not os.path.exists("index"):
      os.mkdir("index")
      ix = create_in("index", self.schema)
      ix = open_dir("index")
    else:
      ix = open_dir("index")
    writer = AsyncWriter(ix)
    writer.update_document(title=name, content=content, path=name, editor=str(ctx.author))
    writer.commit()
    await ctx.send(f"Edited tag {name}")


  @commands.command()
  async def taglist(self, ctx):
    if not os.path.exists("index"):
      os.mkdir("index")
      ix = create_in('index', self.schema)
      ix = open_dir('index')
    else:
      ix = open_dir("index")
    x = []
    with ix.searcher() as searcher:
      results = searcher.search(Every(), limit=None)
      i = 0
      for result in results:
        i += 1
        title = result['title']
        x.append(f"{i}. {title}")
    embed = discord.Embed(title="Tag List", description="\n".join(x), colour=0x00ff00)
    await ctx.send(embed=embed)

  @commands.command()
  async def delete(self, ctx, *, name):
    if not os.path.exists("index"):
      os.mkdir("index")
      ix = create_in('index', self.schema)
      ix = open_dir('index')
    else:
      ix = open_dir("index")
    writer = AsyncWriter(ix)
    writer.delete_by_term('path', name)
    writer.commit()
    await ctx.send(f"Deleted tag {name}")

  @commands.command()
  async def taginfo(self, ctx, *, name):
    if not os.path.exists('index'):
      os.mkdir('index')
      ix = create_in('index', self.schema)
      ix = open_dir('index')
    else:
      ix = open_dir('index')
    with ix.searcher() as searcher:
      parser = QueryParser('title', schema=ix.schema)
      query = parser.parse(name)
      corrected = searcher.correct_query(query, name, maxdist=2)
      if corrected.query != query:
        await ctx.send(f"Tag not found. Did you mean: {corrected.string}?")
      else:
        results = searcher.search(query)
        title = results[0]['title']
        editor = results[0]['editor']
        embed = discord.Embed(title="Tag Info", description="", color=0x00ff00)
        embed.add_field(name="Title", value=title)
        embed.add_field(name="Last edited by", value=editor, inline=False)
        await ctx.send(embed=embed)

  @commands.command()
  async def tagsearch(self, ctx, *, name):
    if not os.path.exists('index'):
      os.mkdir('index')
      ix = create_in('index', self.schema)
      ix = open_dir('index')
    else:
      ix = open_dir('index')
    with ix.searcher() as searcher:
      parser = QueryParser('title', schema=ix.schema)
      query = parser.parse(name)
      results = searcher.search(query)
      corrected = searcher.correct_query(query, name, maxdist=2)
      if corrected.query != query:
        await ctx.send(f"Tag not found. Did you mean: {corrected.string}?")
      else:      
        x = []
        i = 0
        for result in results:
          i += 1
          title = result['title']
          x.append(f"{1}. {title}")
        y = "\n".join(x)
        embed = discord.Embed(title=f"Results for {name}:", description=y, color=0x00ff00)
        await ctx.send(embed=embed)

  @commands.command()
  async def raw(self, ctx, *, name):
    if not os.path.exists('index'):
      os.mkdir('index')
      ix = create_in('index', self.schema)
      ix = open_dir('index')
    else:
      ix = open_dir('index')
    with ix.searcher() as searcher:
      parser = QueryParser('title', ix.schema)
      query = parser.parse(name)
      corrected = searcher.correct_query(query, name, maxdist=2)
      if corrected.query != query:
        await ctx.send(f"Tag not found. Did you mean: {corrected.string}?")
      else:
        results = searcher.search(query)
        cleaned = discord.utils.escape_markdown(results[0]['content'])
        await ctx.send(cleaned)

  @commands.command()
  async def create(self, ctx):
    await ctx.send(f"Hey! So I heard you want to make a tag. What's it gonna be called? Type your answer in the chat, or type {ctx.prefix}abort at any to stop making a tag.")
    def check(m):
      return m.channel == ctx.message.channel and m.author == ctx.message.author
    msg = await self.client.wait_for('message', check=check)
    if msg.content == f"{ctx.prefix}abort":
      await ctx.send("Stopping tag creation.") 
    else:
      title = msg.content
      await ctx.send(f"Cool! The name is {title}. What about the content? Type your answer in the chat.")
      msg = await self.client.wait_for('message', check=check)
      if msg.content == f"{ctx.prefix}abort":
        await ctx.send("Stopping tag creation.")
      else:
        content = msg.content
        if not os.path.exists('index'):
          os.mkdir('index')
          ix = create_in('index', schema=self.schema)
          ix = open_dir('index')
        else:
          ix = open_dir('index')
        writer = AsyncWriter(ix)
        writer.update_document(title=title, content=content, path=title, editor=str(ctx.message.author))
        writer.commit()
        await ctx.send(f"Created tag {title}")
    

def setup(client):
  client.add_cog(Tags(client))
