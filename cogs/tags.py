import discord
from discord.ext import commands
import aiosqlite



class Tags(commands.Cog):
  def __init__(self, client):
    self.client = client

  async def get_tag(self, name):
    async with aiosqlite.connect('data.db') as con:
      await con.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
      async with con.execute(f"SELECT content FROM tags WHERE title=?", [name.lower()]) as cur:
        result = await cur.fetchone()
        return result[0]

  async def make_tag(self, name, content):
    async with aiosqlite.connect('data.db') as con:
      await con.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
      await con.execute(f"INSERT INTO tags VALUES(?, ?)", (name.lower(), content))
      await con.commit()

  async def delete_tag(self, name):
    async with aiosqlite.connect('data.db') as con:
      await con.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
      await con.execute(f"DELETE FROM tags WHERE title=?", [name.lower()])
      await con.commit()

  @commands.command()
  async def make(self, ctx, name, *, content: commands.clean_content):
    await self.make_tag(name, content)
    await ctx.send(f"Created tag {name}")
  
  @commands.command(aliases=["tag", 'showtag'])
  async def show(self, ctx, *, name):
    result = await self.get_tag(name)
    await ctx.send(result)
  
  @commands.command()
  async def edit(self, ctx, name, *, content: commands.clean_content):
    await self.delete_tag(name)
    await self.make_tag(name, content)
    await ctx.send(f"Edited tag {name.lower()}")


  @commands.command()
  async def delete(self, ctx, *, name):
    await self.delete_tag(name)
    await ctx.send(f"Deleted tag {name}")


  @commands.command()
  async def raw(self, ctx, *, name):
    result = await self.get_tag(name)
    cleaned = discord.utils.escape_markdown(result)
    await ctx.send(cleaned)

  @commands.command(ignore_extra=True)
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
          await self.make_tag(title, content)
          await ctx.send(f"Created tag {title.lower()}")

  @commands.command()
  async def taglist(self, ctx):
    async with aiosqlite.connect('data.db') as con:
      await con.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
      async with con.execute('SELECT title FROM tags') as cur:
        x = []
        i = 0
        async for result in cur:
          i += 1
          x.append(f"{i}. {result[0]}")
        embed = discord.Embed(title="Tag List", description="\n".join(x), colour=0x00ff00)
        embed.set_thumbnail(url="https://t7.rbxcdn.com/68430bd256a968981b749621ef547fec")
        name = ctx.author.display_name
        avatar = str(ctx.author.avatar_url)
        embed.set_author(name=name, icon_url=avatar)
        await ctx.send(embed=embed)
    
  @commands.command()
  async def tagsearch(self, ctx, *, query):
    async with aiosqlite.connect('data.db') as con:
      await con.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
      async with con.execute(f"SELECT title FROM tags WHERE title LIKE '%{query.lower()}%'") as cur:
        x = []
        i = 0
        async for result in cur:
          i += 1
          x.append(f"{i}. {result[0]}")
        embed = discord.Embed(title=f"Results for {query}", description="\n".join(x), colour=0x00ff00)
        embed.set_thumbnail(url="https://t7.rbxcdn.com/68430bd256a968981b749621ef547fec")
        name = ctx.author.display_name
        avatar = str(ctx.author.avatar_url)
        embed.set_author(name=name, icon_url=avatar)
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Tags(client))
