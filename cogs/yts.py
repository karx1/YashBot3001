import discord
from discord.ext import commands

def yts():
  def predicate(ctx):
    return ctx.message.guild.id == 574596466773983244
  return commands.check(predicate)

class YTS(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["subscribe", "updates"])
  @yts()
  async def update(self, ctx):
    guild = ctx.message.guild
    await ctx.message.author.add_roles(guild.get_role(583105075795460096), reason="Subscribed", atomic=True)
    await ctx.send("You have subscribed, {}!".format(ctx.message.author.mention))

  @commands.command()
  @yts()
  async def polls(self, ctx):
    guild = ctx.message.guild
    role = guild.get_role(583105133232259085)
    await ctx.message.author.add_roles(role, reason="Subscribed", atomic=True)
    await ctx.send("You will now recieve notifications for polls, {}!".format(ctx.message.author.mention))

  @commands.command()
  @yts()
  async def unsubscribe(self, ctx):
    guild = ctx.message.guild
    role1 = guild.get_role(583105075795460096)
    role2 = guild.get_role(583105133232259085)
    await ctx.message.author.remove_roles(role1, reason="Unsubscribed", atomic=True)
    await ctx.message.author.remove_roles(role2, reason="Unsubscribed", atomic=True)
    await ctx.send("{} has unsubscribed!".format(ctx.message.author.mention))

  @commands.command(aliases=["add bot"])
  @yts()
  async def addbot(self, ctx, num=None):
    if num == None:
      await ctx.send("You must provide an ID!")
    await ctx.send("Ok {}, your bot has been requested to the moderators!".format(ctx.author.mention))
    channel = self.client.get_channel(584420500118437898)
    await channel.send("{} has requested a bot! here's the link: https://discordapp.com/oauth2/authorize?scope=bot&client_id={}".format(ctx.author.display_name, num))


def setup(client):
  client.add_cog(YTS(client))
