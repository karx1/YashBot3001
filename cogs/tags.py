import discord
from discord.ext import commands
import os.path
import os
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.query import *
from whoosh.qparser import QueryParser

class Tags(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True),
                path=ID(stored=True), tags=KEYWORD, icon=STORED)
  
  @commands.command()
  async def make(self, ctx, name, *, content):
    if not os.path.exists("index"):
      os.mkdir("index")
      ix = create_in("index", self.schema)
    else:
      ix = open_dir("index")
    writer = ix.writer()
    writer.add_document(title=name, content=content, path=content)
    writer.commit()
    await ctx.send(f"Created tag {name}")
  
  @commands.command()
  async def show(self, ctx, *, name):
    if not os.path.exists("index"):
      os.mkdir("index")
      ix = create_in('index', self.schema)
    else:
      ix = open_dir("index")
    with ix.searcher() as searcher:
      parser = QueryParser('title', ix.schema)
      query = parser.parse(name)
      results = searcher.search(query)
      await ctx.send(results[0]['path'])
  


def setup(client):
  client.add_cog(Tags(client))
