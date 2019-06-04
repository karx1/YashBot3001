import discord
from discord.ext import commands
from pyfiglet import figlet_format
from gtts import gTTS
import time
import datetime


class TextCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def secret(self, ctx, *, message= ""):
	  if message is "":
		  message = ctx.message.author.display_name
	  await ctx.send("|| {} ||".format(message))

  @commands.command()
  async def embed(self, ctx, *, message=""):
    avy = ctx.message.author.avatar_url
    avy_str = str(avy)
    username = ctx.message.author.display_name
    if message is "":
      message = username
    embed=discord.Embed(title="", description=message, color=0x00ff00)
    embed.set_author(name=username, icon_url=avy_str)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  @commands.command()
  async def echo(self, ctx, *, message=""):
    if message is "":
      message = ctx.message.author.display_name
    await ctx.send(message)

  @commands.command()
  async def tts(self, ctx, *, message=""):
    num = ctx.message.author.display_name
    time = datetime.datetime.now()
    time = str(time)
    if message is "":
      message = ctx.message.author.display_name
    await ctx.trigger_typing()
    tts = gTTS(text=message.lower(), lang="en-GB-Standard-D")
    tts.save('cogs/data/out/out.wav')
    await ctx.send(file=discord.File('cogs/data/out/out.wav'))

  @commands.command()
  async def ascii(self, ctx, *, inp=""):
    if inp == "":
      inp = ctx.message.author.display_name
    ascii_banner = figlet_format(inp, font="small")
    await ctx.send("```{}```".format(ascii_banner))
  

  @commands.command()
  async def upper(self, ctx, *, message=""):
    if message == "":
      message = ctx.message.author.display_name
    message = message.upper()
    await ctx.send(message)

  @commands.command()
  async def lower(self, ctx, *, message=""):
    if message == "":
      message = ctx.message.author.display_name
    message = message.lower()
    await ctx.send(message)

  @commands.command()
  async def reverse(self, ctx, *, message=""):
    if message == "":
      message = ctx.message.author.name
    message = message[::-1]
    await ctx.send(message)



def setup(client):
  client.add_cog(TextCog(client))
