import discord
from discord.ext import commands
import datetime

class EventCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    channel = self.client.get_channel(580383812438065193)
    time = datetime.datetime.now()
    await channel.send(f"Joined server {guild} at {time}")

  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    channel = self.client.get_channel(580383812438065193)
    time = datetime.datetime.now()
    await channel.send(f"Left server {guild} at {time}")

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    error = str(error)
    f = open('log.txt', 'a')
    f.write("Error: {}\n".format(error))
    f.close()
    fi = open('log.txt', 'r')
    print(fi.read())
    if "is not found" in error:
      return
    elif "check functions for" in error:
      await ctx.send("It looks like you can't use this command. If you believe this is a mistake, ask for help in the support server!")
    elif "Results only has 0 hits" in error:
      await ctx.send("It looks like this tag does not exist. Use `;make` to create it!")
    else:
      await ctx.send("Error: {}".format(error))


def setup(client):
  client.add_cog(EventCog(client))
