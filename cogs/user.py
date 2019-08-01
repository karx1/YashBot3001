import discord
from discord.ext import commands
import typing

class User(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.group(invoke_without_command=True)
  async def user(self, ctx):
    await ctx.send_help(ctx.command)
  
  @user.command()
  async def info(self, ctx, member: typing.Union[discord.Member, discord.User] = None):
    if member is None:
      member = ctx.message.author
    embed = await self.client.embed(title="User info!", description=str(member))
    embed.add_field(name="Activity:", value=member.activity)
    embed.add_field(name="Status:", value=f"Overall: {member.status}\nMobile: {member.mobile_status}\nDesktop: {member.desktop_status}\nWeb: {member.web_status}")
    embed.add_field(name="Timestamps:", value=f"Created at: {member.created_at}\nJoined at: {member.joined_at}\nBoosting since: {member.premium_since}")
    await ctx.send(embed=embed)
  

  @user.command()
  async def avatar(self, ctx, member: typing.Union[discord.Member, discord.User] = None):
    if member is None:
      member = ctx.message.author
    embed = await self.client.embed(title=f"{member.name}'s avatar")
    embed.set_image(url=str(member.avatar_url))
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(User(client))