import discord
from discord.ext import commands
import datetime
import inspect
import os
from jishaku.paginators import PaginatorInterface
import humanize


class PaginatorEmbedInterface(PaginatorInterface):
    """
    A subclass of :class:`PaginatorInterface` that encloses content in an Embed.
    """

    def __init__(self, *args, **kwargs):
        self._embed = kwargs.pop("embed", None) or discord.Embed()
        super().__init__(*args, **kwargs)

    @property
    def send_kwargs(self) -> dict:
        display_page = self.display_page
        self._embed.description = self.pages[display_page]
        self._embed.set_footer(text=f"Page {display_page + 1}/{self.page_count}")
        self._embed.colour = 0x00FF00
        self._embed.set_author(
            name=self.bot.user.display_name, icon_url=str(self.bot.user.avatar_url)
        )
        return {"embed": self._embed}

    max_page_size = 2048

    @property
    def page_size(self) -> int:
        return self.paginator.max_size


class MinimalEmbedPaginatorHelp(commands.MinimalHelpCommand):
    """
    A subclass of :class:`commands.MinimalHelpCommand` that uses a PaginatorEmbedInterface for pages.
    """

    async def send_pages(self):
        if isinstance(self.context.channel, discord.DMChannel):
            destination = self.context.author
        else:
            destination = self.get_destination()

        interface = PaginatorEmbedInterface(
            self.context.bot, self.paginator, owner=self.context.author
        )
        await interface.send_to(destination)


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._original_help_command = commands.MinimalHelpCommand()
        client.help_command = MinimalEmbedPaginatorHelp()
        client.help_command.cog = self
        self.start_time = datetime.datetime.now()

    def cog_unload(self):
        self.client.help_command = self._original_help_command

    @commands.command()
    async def invite(self, ctx):
        print("Advertising Start!")
        name = ctx.message.author.display_name
        avy = str(ctx.message.author.avatar_url)
        embed = await self.client.embed(title="Invite YashBot3001")
        embed.add_field(
            name="YashBot3001",
            value="[Invite YashBot3001](http://www.karx.xyz/projects.html#yashbot)",
            inline=False,
        )
        embed.add_field(
            name="Uno Reverse Card",
            value="[Invite Uno Reverse Card](https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=565565207326490624)",
            inline=False,
        )
        embed.add_field(
            name="Support Server",
            value="[Join the Support Server](https://discord.gg/hG6RDZz)",
        )
        embed.set_thumbnail(url=str(ctx.guild.me.avatar_url))
        embed.set_author(name=name, icon_url=avy)
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        name = ctx.message.author.display_name
        avy = str(ctx.message.author.avatar_url)
        users = len(self.client.users)
        servers = len(self.client.guilds)
        embed = await self.client.embed()
        embed.add_field(
            name="YashBot3001 info",
            value=f"This bot was made by Yash Karandikar. It is spread out in {self.client.filecount} files and made of {self.client.linecount} lines, is written in Python 3.7, and uses discord.py {discord.__version__}.\nEnjoy!",
            inline=False,
        )
        embed.add_field(name="Prefix", value=";", inline=False)
        # embed.add_field(name="Changelog", value="[Check out the changelog here!](https://tinyurl.com/yashrobot)", inline=False)
        embed.add_field(
            name="Users", value=f"This bot can see {users} users and {servers} servers."
        )
        embed.set_thumbnail(url=str(ctx.guild.me.avatar_url))
        embed.set_author(name=name, icon_url=avy)
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=embed)

    @commands.command(aliases=["src"])
    async def source(self, ctx, *, command: str = None):
        """Displays my full source code or for a specific command.
        To display the source code of a subcommand you can separate it by
        periods, e.g. user.info for the info subcommand of the user command
        or by spaces.
        """
        source_url = "https://github.com/nerdstep710/YashBot3001"
        branch = "master"
        if command is None:
            return await ctx.send(source_url)

        if command == "help":
            src = type(self.client.help_command)
            filename = inspect.getsourcefile(src)
        else:
            obj = self.client.get_command(command.replace(".", " "))
            if obj is None:
                return await ctx.send("https://github.com/nerdstep710/YashBot3001")

            # since we found the command we're looking for, presumably anyway, let's
            # try to access the code itself
            src = obj.callback.__code__
            filename = src.co_filename

        lines, firstlineno = inspect.getsourcelines(src)

        location = os.path.relpath(filename).replace("\\", "/")

        final_url = f"<{source_url}/blob/{branch}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}>"
        await ctx.send(final_url)

    @commands.command()
    async def uptime(self, ctx):
        command_time = datetime.datetime.now()
        ut = command_time - self.start_time
        await ctx.send(f"This bot has been alive for {humanize.naturaldelta(ut)}")

    @commands.command(aliases=["servers"])
    async def guilds(self, ctx):
        server_count = len(self.client.guilds)
        await ctx.send(f"I am in **{server_count}** guilds!")

    @commands.command(aliases=["members"])
    async def users(self, ctx):
        user_count = len(self.client.users)
        await ctx.send(f"I can see **{user_count}** users!")


def setup(client):
    client.help_command.cog = Info(client)
    client.add_cog(Info(client))
