import discord
from discord.ext import commands
import typing
import os
import asyncio

class customBetaBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        extensions = [
            'jishaku',
            'cogs.music'
        ]

        for e in extensions:
            self.load_extension(e)

    async def on_ready(self):
        print(f"Logged in as: {client.user}")
        print(f"discord.py  version: {discord.__version__}")
    
    async def on_command_error(self, ctx, error):
        error_str = str(error)
        error = getattr(error, 'original', error)
        permcheck = (commands.BotMissingPermissions, commands.MissingPermissions, discord.Forbidden)
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Looks like you forgot to provide `{error.param}`!")
        elif isinstance(error, permcheck):
            await ctx.send(f"Looks like I am forbidden from performing this command here.")
        else:
            await ctx.send(f"Error: {error_str}")

client = customBetaBot(case_insensitive=True, command_prefix=":")





@client.command()
async def bot(ctx, member: typing.Union[discord.Member, discord.User], *, message: str):
    await ctx.message.delete()
    webhook = await ctx.channel.create_webhook(name=member.name)
    await webhook.send(content=message, avatar_url=str(member.avatar_url))
    await webhook.delete()

@client.command(hidden=True)
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting Down...")
    await asyncio.sleep(5)
    await ctx.send("Sucessfully shut down beta bot.")
    await client.close()


token = open("./token.txt", 'r').read()
client.run(token)
