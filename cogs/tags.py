import discord
from discord.ext import commands
import sqlite3



class Tags(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.con = sqlite3.connect('data.db')
    self.cur = self.con.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.con.commit()

  


  @commands.command()
  async def make(self, ctx, name, *, content: commands.clean_content):
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"INSERT INTO tags VALUES('{name}', '{content}')")
    self.con.commit()
    await ctx.send(f"Created tag {name}")
  
  @commands.command()
  async def show(self, ctx, *, name):
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"SELECT content FROM tags WHERE title = '{name}'")
    result = self.cur.fetchone()
    await ctx.send(result[0])
  
  @commands.command()
  async def edit(self, ctx, name, *, content: commands.clean_content):
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"DELETE FROM tags WHERE title = '{name}'")
    self.cur.execute(f"INSERT INTO tags VALUES('{name}', '{content}')")
    self.con.commit()
    await ctx.send(f"Edited tag {name}")


  @commands.command()
  async def delete(self, ctx, *, name):
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"DELETE FROM tags WHERE title = '{name}'")
    self.con.commit()
    await ctx.send(f"Deleted tag {name}")



  @commands.command()
  async def raw(self, ctx, *, name):
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    self.cur.execute(f"SELECT content FROM tags WHERE title = '{name}'")
    result = self.cur.fetchone()
    cleaned = discord.utils.escape_markdown(result[0])
    await ctx.send(cleaned)

  @commands.command()
  async def create(self, ctx):
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
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
        self.con.commit()
        await ctx.send(f"Created tag {title}")

  @commands.command()
  async def taglist(self, ctx):
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    results = [job[0] for job in self.cur.execute("SELECT title FROM tags")]
    x = []
    i = 0
    for result in results:
      i += 1
      x.append(f"{i}. {result}")
    embed = discord.Embed(title="Tag List", description="\n".join(x), colour=0x00ff00)
    embed.set_thumbnail(url="https://t7.rbxcdn.com/68430bd256a968981b749621ef547fec")
    name = ctx.author.display_name
    avatar = str(ctx.author.avatar_url)
    embed.set_author(name=name, icon_url=avatar)
    await ctx.send(embed=embed)
    
  @commands.command()
  @commands.is_owner()
  async def closedb(self, ctx):
    self.con.commit()
    self.con.close()
    await ctx.send("Done.")

def setup(client):
  client.add_cog(Tags(client))
