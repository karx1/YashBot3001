import discord
from discord.ext import commands

class UserCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.group(invoke_without_command=True)
  async def user(self, ctx):
    await ctx.send("What? Did you expect something to happen?")
  
  @user.command()
  async def info(self, ctx, member: discord.Member = None):
    if member is None:
      member = ctx.message.author
    embed = discord.Embed(title="User info!", description=str(member), color=0x00ff00)
    embed.add_field(name="Activity:", value=member.activity)
    embed.add_field(name="Status:", value=f"Overall: {member.status}\nMobile: {member.mobile_status}\nDesktop: {member.desktop_status}\nWeb: {member.web_status}")
    embed.add_field(name="Timestamps:", value=f"Created at: {member.created_at}\nJoined at: {member.joined_at}\nPremium since: {member.premium_since}")
    await ctx.send(embed=embed)
  

  @user.command()
  async def avatar(self, ctx, member: discord.Member = None):
    if member is None:
      member = ctx.message.author
    embed = discord.Embed(title=f"{member.name}'s avatar", description="", color=0x00ff00)
    embed.set_image(url=str(member.avatar_url))
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(UserCog(client))
