import discord
from discord.ext import commands
import typing
import os
import asyncio
import inspect

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

client = customBetaBot(case_insensitive=True, command_prefix=commands.when_mentioned_or(":"))





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

@client.command(aliases=["src"])
async def source(ctx, *, command: str = None):
        """Displays my full source code or for a specific command.
        To display the source code of a subcommand you can separate it by
        periods, e.g. tag.create for the create subcommand of the tag command
        or by spaces.
        """
        source_url = 'https://github.com/nerdstep710/YashBot3001'
        true_source_url = 'https://github.com/nerdstep710/YashBot3001/tree/beta'
        branch = 'beta'
        if command is None:
            return await ctx.send(true_source_url)

        if command == 'help':
            src = type(client.help_command)
            filename = inspect.getsourcefile(src)
        else:
            obj = client.get_command(command.replace('.', ' '))
            if obj is None:
                return await ctx.send(true_source_url)

            # since we found the command we're looking for, presumably anyway, let's
            # try to access the code itself
            src = obj.callback.__code__
            module = obj.callback.__module__
            filename = src.co_filename

        lines, firstlineno = inspect.getsourcelines(src)

        location = os.path.relpath(filename).replace('\\', '/')

        final_url = f'<{source_url}/blob/{branch}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}>'
        await ctx.send(final_url)

token = open("./token.txt", 'r').read()
client.run(token)
