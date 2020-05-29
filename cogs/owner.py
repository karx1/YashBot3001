import discord
from discord.ext import commands


def is_me():
    def predicate(ctx):
        return ctx.message.author.id == 530064431909175346

    return commands.check(predicate)


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    @is_me()
    async def test(self, ctx):
        await ctx.send(f"Test successful, {ctx.message.author.mention}")

    @commands.command(hidden=True)
    @is_me()
    async def poll(self, ctx, *, question=""):
        channel = self.client.get_channel(579317022740185098)
        guild = self.client.get_guild(574596466773983244)
        role = discord.utils.get(guild.roles, name="Polls")
        message = await channel.send(f"{role.mention} {question}")
        await message.add_reaction("\U0001F44D")
        await message.add_reaction("\U0001F44E")


def setup(client):
    client.add_cog(Owner(client))
