import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import asyncio
from jishaku.paginators import PaginatorInterface
import wikipedia
import datetime
import aiohttp


async def get_prefix(client, message):
  if message.guild is None:
    prefixes = [";", ""]
  elif message.author.id == 530064431909175346:
    prefixes = [";", ""]
  else:
    prefixes = [";"]
  
  return commands.when_mentioned_or(*prefixes)(client, message)

class customBot(commands.Bot):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.http2 = None
    self.http3 = None

    extensions = [
      'jishaku',
      'cogs.fun',
      'cogs.math',
      'cogs.text',
      'cogs.yts',
      'cogs.web',
      'cogs.other',
      'cogs.owner',
      'cogs.info',
      'cogs.image',
      'cogs.user',
      'cogs.tags',
      'cogs.bfd'
      ]
    
    for e in extensions:
      self.load_extension(e)

  async def on_ready(self):
    print("Existing Servers:")
    async for guild in self.fetch_guilds():
      print(guild.name)
    if not self.http2:
      self.http = aiohttp.ClientSession()
    if not self.http3:
      self.http2 = aiohttp.ClientSession(headers={"Authorization": "cce0575985727a5e75264b4baf9523251cb429f9f6941d39b853acac6b3eca8df42c27fccf5682cd8b661930600b6bab471a9e97eba7e75df4ac2d7bfc1bf4d7"})
    while True:
      activity1 = discord.Activity(name=f'{len(self.users)} users | {len(self.guilds)} servers', type=discord.ActivityType.watching)
      await self.change_presence(activity=activity1)
      await asyncio.sleep(5)
      await self.change_presence(activity=discord.Game(name=";help"))
      await asyncio.sleep(5)
  

  
  async def on_command_error(self, ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
      return
    elif isinstance(error, commands.CheckFailure):
      await ctx.send("It looks like you can't use this command. If you believe this is a mistake, ask for help in the support server!")
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Looks like you forgot to provide `{error.param}`!")
    elif isinstance(error, ZeroDivisionError):
      await ctx.send("I can't divide by zero!")
    elif isinstance(error, wikipedia.DisambiguationError):
      embed = discord.Embed(title=f"{error.title} may refer to:", description="\n".join(error.options), colour=0x00ff00)
      await ctx.send(embed=embed)
    elif isinstance(error, wikipedia.PageError):
      await ctx.send("That page does not exist.")
    elif isinstance(error, TypeError):
      if ctx.command.qualified_name == 'show':
        await ctx.send("Tag not found.")
      elif ctx.command.qualified_name == 'raw':
        await ctx.send("Tag not found.")
    elif isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f"This command is on cooldown. Try again in {round(error.retry_after, 2)}s")
      return
    else:
      await ctx.send("Error: {}".format(error_str))
    
    
    f = open('log.txt', 'a')
    f.write("Error: {}\n".format(error))
    f.close()
    fi = open('log.txt', 'r')
    print(fi.read())

  async def process_commands(self, message):
    ctx = await super().get_context(message, cls=commands.Context)
    await self.invoke(ctx)

  async def on_guild_join(self, guild):
    channel = self.fetch_channel(580383812438065193)
    time = datetime.datetime.now()
    await channel.send(f"Joined server {guild} at {time}")

  async def on_guild_remove(self, guild):
    channel = self.fetch_channel(580383812438065193)
    time = datetime.datetime.now()
    await channel.send(f"Left server {guild} at {time}")


  async def post_to_mystbin(self, data):
        data = str(data).encode("utf-8")
        async with self.http2.post("https://mystb.in/documents", data=data) as resp:
            out = await resp.json()

        assert "key" in out

        return "https://mystb.in/raw/" + out["key"]


client = customBot(command_prefix=get_prefix, case_insensitive=True)

client.remove_command('help')


class PaginatorEmbedInterface(PaginatorInterface):
    """
    A subclass of :class:`PaginatorInterface` that encloses content in an Embed.
    """

    def __init__(self, *args, **kwargs):
        self._embed = kwargs.pop('embed', None) or discord.Embed()
        super().__init__(*args, **kwargs)

    @property
    def send_kwargs(self) -> dict:
        display_page = self.display_page
        self._embed.description = self.pages[display_page]
        self._embed.set_footer(text=f'Page {display_page + 1}/{self.page_count}')
        self._embed.colour = 0x00ff00
        return {'embed': self._embed}

    max_page_size = 2048

    @property
    def page_size(self) -> int:
        return self.paginator.max_size

class MinimalEmbedPaginatorHelp(commands.MinimalHelpCommand):
    """
    A subclass of :class:`commands.MinimalHelpCommand` that uses a PaginatorEmbedInterface for pages.
    """

    async def send_pages(self):
        destination = self.get_destination()

        interface = PaginatorEmbedInterface(self.context.bot, self.paginator, owner=self.context.author)
        await interface.send_to(destination)

client.help_command = MinimalEmbedPaginatorHelp()



#initialises the bot
keep_alive()
#the token is stored in an .env file. If you fork this, you have to recreate that with the token inside
token = os.environ.get("BOT_TOKEN")
client.run(token, bot=True, reconnect=True)