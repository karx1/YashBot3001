import discord
from discord.ext import commands
import os.path
import os
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
import dataset



class Tags(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(unique=True), tags=KEYWORD, icon=STORED, editor=TEXT(stored=True))
    self.db = dataset.connect('	postgres://rnoxyawx:C-JNS12hplxKvRoZz2IQSJbphtUy1SIF@hansken.db.elephantsql.com:5432/rnoxyawx')
    self.table = self.db['tags']
  


  @commands.command()
  async def make(self, ctx, name, *, content: commands.clean_content):
    self.table.insert(dict(title=name, content=content, editor=str(ctx.author)))
    self.db.commit()
    await ctx.send(f"Created tag {name}")
  
  @commands.command()
  async def show(self, ctx, *, name):
    result = self.table.find_one(title=name)
    await ctx.send(result['content'])
  
  @commands.command()
  async def edit(self, ctx, name, *, content: commands.clean_content):
    self.table.delete(title=name)
    self.table.insert(dict(title=name, content=content, editor=str(ctx.author)))
    self.db.commit()
    await ctx.send(f"Edited tag {name}")


  @commands.command()
  async def taglist(self, ctx):
    x = []
    i = 0
    for tag in self.db['tags']:
      i += 1
      x.append(f"{i}. {tag['title']}")
    embed = discord.Embed(title="Tag List", description="\n".join(x), colour=0x00ff00)
    await ctx.send(embed=embed)

  @commands.command()
  async def delete(self, ctx, *, name):
    self.table.delete(title=name)
    await ctx.send(f"Deleted tag {name}")


  @commands.command()
  async def raw(self, ctx, *, name):
    result = self.table.find_one(title=name)
    cleaned = discord.utils.escape_markdown(result['content'])
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
      if msg.content == f'{ctx.prefix}abort':
        await ctx.send("Stopping tag creation.")
      else:
        content = msg.content
        self.table.insert(dict(title=title, content=content, editor=str(ctx.author)))
        await ctx.send(f"Created tag {title}")
    

def setup(client):
  client.add_cog(Tags(client))
