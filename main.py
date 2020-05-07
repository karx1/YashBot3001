import discord
from discord.ext import commands, tasks
import os
import asyncio
import wikipedia
import datetime
import aiohttp
import numpy
import logging
import glob


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
    self.embed_color = 0x00ff00
    self.logger = logging.getLogger('discord')
    self.logger.setLevel(logging.WARNING)
    self.handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
    self.handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    self.logger.addHandler(self.handler)
    self.ps_task = self.loop.create_task(self.playingstatus())
    self.change_status = True



    extensions = [
      'jishaku',
      'cogs.fun',
      'cogs.math',
      'cogs.text',
      'cogs.yts',
      'cogs.web',
      'cogs.owner',
      'cogs.info',
      'cogs.image',
      'cogs.user',
      'cogs.tags',
      'cogs.bfd'
      ]

    for e in extensions:
      self.load_extension(e)

  async def playingstatus(self):
    await self.wait_until_ready()
    await asyncio.sleep(3) # Load users
    while self.is_ready() and self.change_status:
        activity1 = discord.Activity(name=f"{len(self.users)} users | {len(self.guilds)} servers", type=discord.ActivityType.watching)
        await client.change_presence(activity=activity1)
        await asyncio.sleep(30)
        await self.change_presence(activity=discord.Game(name=";help"))
        await asyncio.sleep(30)

  async def on_ready(self):
    print("Existing Servers:")
    async for guild in self.fetch_guilds():
      print(guild.name)
    if not self.http2:
      self.http2 = aiohttp.ClientSession()
    if not self.http3:
      self.http3 = aiohttp.ClientSession(headers={"Authorization": "cce0575985727a5e75264b4baf9523251cb429f9f6941d39b853acac6b3eca8df42c27fccf5682cd8b661930600b6bab471a9e97eba7e75df4ac2d7bfc1bf4d7"})
    # activity1 = discord.Activity(name=f'{len(client.users)} users | {len(client.guilds)} servers', type=discord.ActivityType.watching)
    # await client.change_presence(activity=activity1)

  async def on_command_error(self, ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
      return
    elif isinstance(error, commands.CheckFailure):
      await ctx.send("It looks like you can't use this command. If you believe this is a mistake, ask for help in the support server!")
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Looks like you forgot to provide `{error.param}`!")
      await ctx.send_help(ctx.command)
    elif isinstance(error, ZeroDivisionError):
      await ctx.send("I can't divide by zero!")
    elif isinstance(error, wikipedia.DisambiguationError):
      embed = await self.embed(title=f"{error.title} may refer to:", description="\n".join(error.options))
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
    elif isinstance(error, numpy.AxisError):
      await ctx.send("That is not a valid image.")
    elif "Cannot send an empty message" in error_str:
      if ctx.command.qualified_name == 'google':
        await ctx.send('No results were found')
      else:
        await ctx.send("Error: {}".format(error_str))
    else:
      await ctx.send("Error: {}".format(error_str))


    f = open('log.txt', 'a')
    f.write("Error: {}\n".format(error))
    f.close()
    fi = open('log.txt', 'r')
    print(fi.read())

  async def process_commands(self, message):
    if message.author.bot:
      return
    ctx = await super().get_context(message, cls=commands.Context)
    await self.invoke(ctx)

  async def on_guild_join(self, guild):
    channel1 = self.get_channel(580383812438065193)
    time = datetime.datetime.now()
    try:
      channel2 = discord.utils.get(guild.channels, name='general')
      await channel2.send("Hey! I'm YashBot3001! Do ;help for my commands and ;info for info about me!")
    except:
      pass
    finally:
      await channel1.send(f"Joined server {guild} at {time}")

  async def on_guild_remove(self, guild):
    channel = self.get_channel(580383812438065193)
    time = datetime.datetime.now()
    await channel.send(f"Left server {guild} at {time}")


  async def post_to_mystbin(self, data):
        data = str(data).encode("utf-8")
        async with self.http2.post("https://mystb.in/documents", data=data) as resp:
            out = await resp.json()

        assert "key" in out

        return "https://mystb.in/raw/" + out["key"]

  async def embed(self, *, title=None, description=None, color=None, colour=None):
    """A helper function that created discord.Embed objects"""
    color = color or self.embed_color
    title = title or ""
    description = description or ""
    colour = colour or color
    data = {
      'title': title,
      'description': description,
      'color': colour
    }
    embed = discord.Embed.from_dict(data)
    return embed

  def getlinecount(self, directory):
    print(os.getcwd())
    if 'cogs' in os.getcwd():
      os.chdir('..')
    os.chdir(directory)
    names=[]
    for fn in glob.glob('*.py'):
      with open(fn) as f:
        names.append(sum(1 for line in f if line.strip() and not line.startswith('#')))

    return sum(names)

  @property
  def filecount(self):
    if 'cogs' in os.getcwd():
      os.chdir('..')
    x = [
      len([i for i in os.listdir('.') if not i.startswith('.')]),
      len([i for i in os.listdir('cogs') if not i.startswith('.')]),
      # len([i for i in os.listdir('templates') if not i.startswith('.')])
    ]
    return sum(x)

  @property
  def linecount(self):
    x = [
      self.getlinecount('.'),
      self.getlinecount('./cogs')
    ]
    return sum(x)

client = customBot(command_prefix=get_prefix, case_insensitive=True)


@tasks.loop(seconds=30)
async def change_status():
  try:
    activity1 = discord.Activity(name=f'{len(client.users)} users | {len(client.guilds)} servers', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity1)
    await asyncio.sleep(30)
    await client.change_presence(activity=discord.Game(name=";help"))
  except Exception as e:
    print(e)



#initialises the bot
#the token is stored in an .env file. If you fork this, you have to recreate that with the token inside
token_file = open("token.txt", "r")
token_string = token_file.read()
token = "".join(token_string.split())
client.run(token, bot=True, reconnect=True)
