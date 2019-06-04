import discord
from discord.ext import commands
import time
import datetime

class EventCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    channel = self.client.get_channel(580383812438065193)
    time = datetime.datetime.now()
    await channel.send("Joined server {} at {}".format(guild, time))

  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    channel = self.client.get_channel(580383812438065193)
    time = datetime.datetime.now()
    await channel.send("Left server {} at {}".format(guild, time))

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    name = str(ctx.message.author)
    stuff = ctx.message.content
    server = ctx.message.guild
    error = str(error)
    channel = self.client.get_channel(580383812438065193)
    f = open('log.txt', 'a')
    f.write("Error: {}\n".format(error))
    f.close()
    fi = open('log.txt', 'r')
    print(fi.read())
    if "is not found" in error:
      return
    else:
      await ctx.send("Error: {}".format(error))

def setup(client):
  client.add_cog(EventCog(client))
