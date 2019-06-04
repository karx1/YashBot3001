import discord
from discord.ext import commands
import time
import datetime

class OtherCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def enigma(self, ctx):
    print("Advertising Start!")
    embed=discord.Embed(title="Check out Enigma Music", description="[Enigma Music](https://www.youtube.com/channel/UCjnt7bVGGGK0qeJ-zlhEaCw?)", color=0x00ff00)
    embed.set_thumbnail(url="https://yt3.ggpht.com/a/AGF-l7-4N9G81GpS-qHlE44YxG7Z9eSU5e3vPBCbGg=s288-mo-c-c0xffffffff-rj-k-no")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  @commands.command()
  async def nerdstep(self, ctx):
    print("Advertising Start!")
    embed=discord.Embed(title="Check out Nerdstep 710", description="[Nerdstep 710](https://www.youtube.com/channel/UCg3x6EXtKzeBiLnO-T1ge_A?)", color=0x00ff00)
    embed.set_thumbnail(url="https://yt3.ggpht.com/a-/AAuE7mBKMLAXZt8tVRNnAyeht6HWf6WLnrxD4pUUXA=s900-mo-c-c0xffffffff-rj-k-no")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  @commands.command()
  async def evrst(self, ctx):
    print("Advertising Start!")
    embed=discord.Embed(title="Check out EVRST", description="[EVRST](https://www.youtube.com/channel/UCYJSyqmbUxKO-kVhhnMGcLA)", color=0x00ff00)
    embed.set_thumbnail(url="https://yt3.ggpht.com/a/AGF-l7-tozXktVuFV4cCNioQiEDMrLJYwfzNlGD4Hg=s288-mo-c-c0xffffffff-rj-k-no")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  @commands.command()
  async def bros(self, ctx):
    print("Advertising Start!")
    embed=discord.Embed(title="Check out Bros at The Round Table", description="[Bros at The Round Table](https://www.youtube.com/channel/UCAiOlyupgvw1xTCpjlhV8aQ)", color=0x00ff00)
    embed.set_thumbnail(url="https://yt3.ggpht.com/a/AGF-l7_nCOXD51aTpMOcapJrYCJqP8KBd3LZP5S3mw=s288-mo-c-c0xffffffff-rj-k-no")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  @commands.command()
  async def dyt(self, ctx):
    print("Advertising Start!")
    embed=discord.Embed(title="Check out DysfunctionalYT", description="[DysfunctionalYT](https://www.youtube.com/channel/UCazvceDIaM2YuhMNKk9AeEw/)", color=0x00ff00)
    embed.set_thumbnail(url="https://yt3.ggpht.com/a/AGF-l79FlRrKCvNq8Y26q7Jkm9CSdep1x3CE0cSVBQ=s288-mo-c-c0xffffffff-rj-k-no")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)


def setup(client):
  client.add_cog(OtherCog(client))
