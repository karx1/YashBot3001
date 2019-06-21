import discord
from discord.ext import commands
import os.path
import os
import sqlite3



class Tags(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.con = sqlite3.connect('cogs/data/data.db')
    self.cur = self.con.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")

  


  @commands.command()
  async def make(self, ctx, name, *, content: commands.clean_content):
    self.cur.execute(f"INSERT INTO tags VALUES('{name}', '{content}')")
    await ctx.send(f"Created tag {name}")
  
  @commands.command()
  async def show(self, ctx, *, name):
    self.cur.execute(f"SELECT content FROM tags WHERE title = '{name}'")
    result = self.cur.fetchone()
    await ctx.send(result[0])
  
  @commands.command()
  async def edit(self, ctx, name, *, content: commands.clean_content):
    self.cur.execute(f"DELETE FROM tags WHERE title = '{name}'")
    self.cur.execute(f"INSERT INTO tags VALUES('{name}', '{content}')")
    await ctx.send(f"Edited tag {name}")


  @commands.command()
  async def delete(self, ctx, *, name):
    self.cur.execute(f"DELETE FROM tags WHERE title = '{name}'")
    await ctx.send(f"Deleted tag {name}")



  @commands.command()
  async def raw(self, ctx, *, name):
    self.cur.execute(f"SELECT content FROM tags WHERE title = '{name}'")
    result = self.cur.fetchone()
    cleaned = discord.utils.escape_markdown(result[0])
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
        self.cur.execute(f"INSERT INTO tags VALUES('{title}', '{content}')")
        await ctx.send(f"Created tag {title}")

  @commands.command()
  async def taglist(self, ctx):
    result = [job[0] for job in self.cur.execute("SELECT title FROM tags")]
    embed = discord.Embed(title="Tag List", description="\n".join(result), color=)
    

def setup(client):
  client.add_cog(Tags(client))
