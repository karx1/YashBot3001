import discord
from discord.ext import commands
import sqlite3


class Tags(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.con = sqlite3.connect('data.db')
    self.cur = self.con.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")

  
  @commands.command()
  async def make(self, ctx, name, *, content: commands.clean_content):
    """Makes a tag"""
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"INSERT INTO tags VALUES(?, ?)", (name.lower(), content))
    self.con.commit()
    await ctx.send(f"Created tag {name}")
  
  @commands.command()
  async def show(self, ctx, *, name):
    """Displays the content of a tag"""
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"SELECT content FROM tags WHERE title=?", [name.lower()])
    result = self.cur.fetchone()
    await ctx.send(result[0])
  
  @commands.command()
  async def edit(self, ctx, name, *, content: commands.clean_content):
    """Edits a tag"""
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"DELETE FROM tags WHERE title=?", [name.lower()])
    self.cur.execute(f"INSERT INTO tags VALUES(?, ?)", (name.lower(), content))
    self.con.commit()
    await ctx.send(f"Edited tag {name}")


  @commands.command()
  async def delete(self, ctx, *, name):
    """Deletes a tag"""
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"DELETE FROM tags WHERE title=?", [name.lower()])
    self.con.commit()
    await ctx.send(f"Deleted tag {name}")



  @commands.command()
  async def raw(self, ctx, *, name):
    """Shows a tag with markdown escaped"""
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"SELECT content FROM tags WHERE title=?", [name.lower()])
    result = self.cur.fetchone()
    cleaned = discord.utils.escape_markdown(result[0])
    await ctx.send(cleaned)

  @commands.command()
  async def create(self, ctx):
    """Walks you through the process fo making a tag"""
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    await ctx.send(f"Hey! So I heard you want to make a tag. What's it gonna be called? Type your answer in the chat, or type {ctx.prefix}abort at any time to stop making a tag.")
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
        self.cur.execute(f"INSERT INTO tags VALUES(?, ?)", (title.lower(), content))
        self.con.commit()
        await ctx.send(f"Created tag {title}")

  @commands.command()
  async def taglist(self, ctx):
    """Shows the title of every tag"""
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    results = [job[0] for job in self.cur.execute("SELECT title FROM tags")]
    x = []
    i = 0
    for result in results:
      i += 1
      x.append(f"{i}. {result}")
    embed = await self.client.embed(title="Tag List", description="\n".join(x))
    embed.colour = 0x00ff00
    embed.set_thumbnail(url=str(ctx.guild.me.avatar_url))
    await ctx.send(embed=embed)
    
  @commands.command()
  async def tagsearch(self, ctx, *, query):
    """Searches for all tags matching a query"""
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    new_query = f"%{query.lower()}%"
    results = [job[0] for job in self.cur.execute("SELECT title FROM tags WHERE title LIKE ?", [new_query])]
    x = []
    i = 0
    for result in results:
      i += 1
      x.append(f"{i}. {result}")
    embed = await self.client.embed(title=f"Results for {query}", description="\n".join(x))
    embed.colour = 0x00ff00
    embed.set_thumbnail(url=str(ctx.guild.me.avatar_url))
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Tags(client))