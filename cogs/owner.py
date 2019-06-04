import discord
from discord.ext import commands

def is_me():
  def predicate(ctx):
    return ctx.message.author.id == 530064431909175346
  return commands.check(predicate)

class OwnerCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @is_me()
  async def test(self, ctx):
    channel = self.client.get_channel(577195540165558350)
    name = ctx.message.author.display_name
    avy = ctx.message.author.avatar
    print("Test successful for {}".format(name))
    await channel.send(avy)
    await channel.send("Test successful for {}".format(name))


  @commands.command()
  @is_me()
  async def poll(self, ctx, *, question=""):
    channel = self.client.get_channel(579317022740185098)
    role = ctx.message.guild.get_role(583105133232259085)
    await channel.send("{} {}".format(role.mention, question))
    message = channel.last_message
    await message.add_reaction(u"\U0001F44D")
    await message.add_reaction(u"\U0001F44E")

def setup(client):
  client.add_cog(OwnerCog(client))
