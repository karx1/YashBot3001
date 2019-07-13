import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import asyncio
import sqlite3
from jishaku.paginators import PaginatorInterface



async def get_prefix(client, message):
  if message.guild is None:
    return [";", ""]
  else:
    return ";"

class customContext(commands.Context):

  async def make_table(self):
    cur = sqlite3.connect('data.db').cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tags (title TEXT, content TEXT)")
    sqlite3.connect("data.db").commit()

  async def make_tag(self, name, content):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO tags VALUES(?, ?)", (name.lower(), content))
    con.commit()
    print("done")
  
  async def get_tag(self, name):
    cur = sqlite3.connect('data.db').cursor()
    cur.execute("SELECT content FROM tags WHERE title=?", [name.lower()])
    result = cur.fetchone()
    return result[0]
  
  async def update_tag(self, name, content):
    cur = sqlite3.connect('data.db').cursor()
    cur.execute("UPDATE tags SET content=? WHERE title=?", (content, name.lower()))
    sqlite3.connect('data.db').commit()

class customBot(commands.Bot):
  async def get_context(self, message, *, cls=None):
    return await super().get_context(message, cls=customContext)

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

extensions = [
  'jishaku',
  'cogs.fun',
  'cogs.math',
  'cogs.text',
  'cogs.yts',
  'cogs.web',
  'cogs.other',
  'cogs.owner',
  'cogs.events',
  'cogs.info',
  'cogs.image',
  'cogs.user',
  'cogs.tags'
]

if __name__ == '__main__':
  for e in extensions:
    client.load_extension(e)


#the discord game activity
@client.event
async def on_ready():
  user_count = len(client.users)
  server_count = len(client.guilds)
  print("Existing Servers:")
  async for guild in client.fetch_guilds():
    print(guild.name)
  while True:
    user_count = len(client.users)
    server_count = len(client.guilds)
    activity1 = discord.Activity(name=f'{user_count} users | {server_count} servers', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity1)
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Game(name=";help"))
    await asyncio.sleep(5)


#initialises the bot
keep_alive()
#the token is stored in an .env file. If you fork this, you have to recreate that with the token inside
code = os.environ.get("BOT_TOKEN")
client.run(code)
