from discord.ext.commands import Bot
from keep_alive import keep_alive
import os
import discord


BOT_PREFIX = (";")
client = Bot(command_prefix=BOT_PREFIX, case_insensitive=True)
commands = discord.ext.commands

client.remove_command('help')


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
]

if __name__ == '__main__':
  for e in extensions:
    client.load_extension(e)


#the discord game activity
@client.event
async def on_ready():
  user_count = len(client.users)
  server_count = len(client.guilds)
  await client.change_presence(activity=discord.Game(name=f"{user_count} | ;help"))
  print("Existing Servers:")
  async for guild in client.fetch_guilds():
    print(guild.name)


#initialises the bot
keep_alive()
#the token is stored in an .env file. If you fork this, you have to recreate that with the token inside
code = os.environ.get("BOT_TOKEN")
client.run(code)
