import discord
from discord.ext.commands import Bot
from keep_alive import keep_alive
import os



async def get_prefix(client, message):
  if message.guild is None:
    return [";", ""]
  else:
    return ";"

client = Bot(command_prefix=get_prefix, case_insensitive=True)
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
  'cogs.help',
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
  await client.change_presence(activity=discord.Game(name=f"{user_count} users | {server_count} servers"))
  print("Existing Servers:")
  async for guild in client.fetch_guilds():
    print(guild.name)


#initialises the bot
keep_alive()
#the token is stored in an .env file. If you fork this, you have to recreate that with the token inside
code = os.environ.get("BOT_TOKEN")
client.run(code)
