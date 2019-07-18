import discord
from discord.ext import commands
from pyfiglet import figlet_format
from gtts import gTTS
import datetime
from io import BytesIO
from .utils import async_executor

@async_executor()
def do_tts(ctx, message):
  with ctx.typing():
    f = BytesIO()
    tts = gTTS(text=message.lower(), lang="en")
    tts.write_to_fp(f)
    f.seek(0)
    return f

class Text(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def secret(self, ctx, *, message= ""):
	  if message is "":
		  message = ctx.message.author.display_name
	  await ctx.send(f"||{message}||")

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
    embed.set_thumbnail(url=avy_str)
    await ctx.send(embed=embed)

  @commands.command()
  async def echo(self, ctx, *, message=""):
    if message is "":
      message = ctx.message.author.display_name
    await ctx.send(message)

  @commands.command()
  async def tts(self, ctx, *, message: commands.clean_content):
    buff = await do_tts(ctx, message)
    await ctx.send(file=discord.File(buff, "out.wav"))

  @commands.command()
  async def ascii(self, ctx, *, inp: commands.clean_content):
    ascii_banner = figlet_format(inp, font="small")
    await ctx.send(f"```{ascii_banner}```")
  

  @commands.command()
  async def upper(self, ctx, *, message: commands.clean_content):
    message = message.upper()
    await ctx.send(message)

  @commands.command()
  async def lower(self, ctx, *, message: commands.clean_content):
    message = message.lower()
    await ctx.send(message)

  @commands.command()
  async def reverse(self, ctx, *, message: commands.clean_content):
    message = message[::-1]
    await ctx.send(message)


def setup(client):
  client.add_cog(Text(client))