import discord
from discord.ext import commands
import datetime

class counter:
  start_time = datetime.datetime.now()
c = counter()

class Info(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def invite(self, ctx):
    print("Advertising Start!")
    name = ctx.message.author.display_name
    avy = str(ctx.message.author.avatar_url)
    embed=discord.Embed(title="Invite YashBot 3001", description="", color=0x00ff00)
    embed.add_field(name="YashBot3001", value="[Invite YashBot3001](https://yashbot3001--nerdstep710.repl.co/invite)", inline=False)
    embed.add_field(name="Uno Reverse Card", value="[Invite Uno Reverse Card](https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=565565207326490624)", inline=False)
    embed.add_field(name="Support Server", value="[Join the Support Server](https://discord.gg/hG6RDZz)")
    embed.set_thumbnail(url="https://t7.rbxcdn.com/68430bd256a968981b749621ef547fec")
    embed.set_author(name=name, icon_url=avy)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  @commands.command()
  async def info(self, ctx):
    name = ctx.message.author.display_name
    avy = str(ctx.message.author.avatar_url)
    users = len(self.client.users)
    servers = len(self.client.guilds)
    embed=discord.Embed(title="", description="", color=0x00ff00)
    embed.add_field(name="YashBot3001 info", value="This bot was made by Yash Karandikar. It has 1015 lines of code, is written in Python 3.7, and uses discord.py 1.1.1.\nEnjoy!", inline=False)
    embed.add_field(name="Prefix", value=";", inline=False)
    embed.add_field(name="Changelog", value="[Check out the changelog here!](https://tinyurl.com/yashrobot)", inline=False)
    embed.add_field(name="Users", value=f"This bot can see {users} users and {servers} servers.")
    embed.set_thumbnail(url="https://t7.rbxcdn.com/68430bd256a968981b749621ef547fec")
    embed.set_author(name=name, icon_url=avy)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  

  
  @commands.command()
  async def source(self, ctx):
    await ctx.send("My code can be found here: https://github.com/nerdstep710/YashBot3001")

  @commands.command()
  async def uptime(self, ctx):
    command_time = datetime.datetime.now()
    ut = command_time - c.start_time
    await ctx.send(f"This bot has been alive for {ut}")

  @commands.command(aliases=["servers"])
  async def guilds(self, ctx):
    server_count = len(self.client.guilds)
    await ctx.send(f"I am in **{server_count}** guilds!")

  @commands.command(aliases=["members"])
  async def users(self, ctx):
    user_count = len(self.client.users)
    await ctx.send(f"I can see **{user_count}** users!")

def setup(client):
  client.add_cog(Info(client))
