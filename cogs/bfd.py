import discord
from discord.ext import commands
import aiohttp

class bfd(commands.Cog, name="Bots for Discord"):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def bfd(self, ctx):
    """Sends a link to the Bots for Discord page."""
    await ctx.send(f"https://botsfordiscord.com/bot/{self.client.user.id}")
  
  @commands.command()
  async def votes(self, ctx):
    async with self.client.http3.get(f"https://botsfordiscord.com/api/bot/{self.client.user.id}/votes") as resp:
      data = await resp.json()
      try:
        assert "votes" in data
        vote_count = data["votes"]
        await ctx.send(f"**{self.client.user.display_name}** has **{vote_count}** votes!")
      except AssertionError:
        await ctx.send("Looks like the service is currently down. Please try again.")
  
  @commands.command()
  async def upvote(self, ctx):
    """Sends a link to the voting page"""
    await ctx.send("https://botsfordiscord.com/bot/565318846349705230/vote")

def setup(client):
  client.add_cog(bfd(client))