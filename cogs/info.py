import discord
from discord.ext import commands
from discord_interactive import Page, Help
import time
import datetime

class counter:
  start_time = datetime.datetime.now()
c = counter()

class InfoCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def invite(self, ctx):
    print("Advertising Start!")
    name = ctx.message.author.display_name
    avy = str(ctx.message.author.avatar_url)
    embed=discord.Embed(title="Invite YashBot 3001", description="", color=0x00ff00)
    embed.add_field(name="YashBot3001", value="[Invite YashBot3001](https://yashbot3001--yashkarandikar.repl.co/invite)", inline=False)
    embed.add_field(name="Uno Reverse Card", value="[Invite Uno Reverse Card](https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=565565207326490624)", inline=False)
    embed.add_field(name="Testing Server", value="[Join the Testing Server](https://discord.gg/hG6RDZz)")
    embed.set_thumbnail(url="https://t7.rbxcdn.com/68430bd256a968981b749621ef547fec")
    embed.set_author(name=name, icon_url=avy)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  @commands.command()
  async def info(self, ctx):
    name = ctx.message.author.display_name
    avy = str(ctx.message.author.avatar_url)
    users = len(self.client.users)
    servers = len(self.client.guilds)
    embed=discord.Embed(title="", description="", color=0x00ff00)
    embed.add_field(name="YashBot3001 info", value="This bot was made by Yash Karandikar. It has 1015 lines of code, is written in Python 3.7, and uses discord.py 1.1.1.\nEnjoy!", inline=False)
    embed.add_field(name="Prefix", value=";", inline=False)
    embed.add_field(name="Changelog", value="[Check out the changelog here!](https://tinyurl.com/YashBot3001)", inline=False)
    embed.add_field(name="Users", value="This bot can see {} users and {} servers.".format(users, servers))
    embed.set_thumbnail(url="https://t7.rbxcdn.com/68430bd256a968981b749621ef547fec")
    embed.set_author(name=name, icon_url=avy)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

  


  @commands.command()
  async def help(self, ctx):
    root = Page("Welcome to YashBot3001!\nPing Y45HK4R4ND1K4R#9565 on the testing server if you have any issues. Use the reactions to navigate through this menu!")
    page1 = Page("**YashBot3001 Help**\nFun:\n`;8ball [question]`\n`;bully <target>`\n`;kill <target>`\n`;cat`\n`;dice`\n`;dog`\n`;fight <challenger1> <challenger2>`\n`;hamster`\n`;hello`\n`;ping`\n`;rps [choice]`\n`;song`\n`;thanos <target>`\n`;coin`\n**Anything in [] is required. Anything in <> is optional.**")
    page2 = Page("**YashBot3001 Help**\nMath:\n`;add [number1] [number2]`\n`;cos [number]`\n`;divide [number1] [number2]`\n`;exp [number1] [number2]`\n`;factorial [number]`\n`;multiply [number1] [number2]`\n`;root [number]`\n`;sine [number]`\n`;square [number]`\n`;subtract [number1] [number2]`\n`;tan [number]`\n**Anything in [] is required. Anything in <> is optional.**")
    page3 = Page("**YashBot3001 Help**\nInfo:\n`;help`\n`;info`\n`;invite`\n`;uptime`\n`;source`\n`;guilds`\n`;users`\n**Anything in [] is required. Anything in <> is optional.**")
    page4 = Page("**YashBot3001 Help**\nText Manipulation:\n`;secret <message>`\n`;echo <message>`\n`;embed <message>`\n`;upper <message>`\n`;lower <message>`\n`;reverse <message>`\n`;tts <message>` <------ Works best on computer\n`;ascii <message>` <------ Works best with short message\n**Anything in [] is required. Anything in <> is optional.**")
    page5 = Page("**YashBot3001 Help**\nImage Manipulation:\n`;kirby [message]`\n`;lisa [message]`\n`;pewds [message]`\n`;gru [message]`\n`;linus [message]`\n`;trump [message]`\n`;elon [message]`\n**Anything in [] is required. Anything in <> is optional.**")
    page6 = Page("**YashBot3001 Help**\nTesting Server Only Commands:\n*These commands only work in the testing server. Join it here: https://discord.gg/hG6RDZz*\n`;subscribe`\n`;polls`\n`;unsubscribe`\n**Anything in [] is required. Anything in <> is optional.**")
    page7 = Page("**YashBot3001 Help**\nWeb:\n`;google [query]`\n`;youtube [query]`\n**Anything in [] is required. Anything in <> is optional.**")
    page8 = Page("**YashBot3001 Help**\nOther:\n`;bros`\n`;dyt`\n`;enigma`\n`;evrst`\n`;nerdstep`\n**Anything in [] is required. Anything in <> is optional.**")
    root.link(page1, description="Fun", reaction=u"\U0001F3AE")
    root.link(page2, description="Math", reaction=u"\U0001F522")
    root.link(page3, description="Info", reaction=u"\U0001F5DE")
    root.link(page4, description="Text Manipulation", reaction=u"\U0001F520")
    root.link(page5, description="Image Manipulation", reaction=u"\U0001F5BC")
    root.link(page6, description="Testing Server Only", reaction=u"\U0001F6E0")
    root.link(page7, description="Web", reaction=u"\U0001F4BB")
    root.link(page8, description="Other", reaction=u"\u2753")
    h = Help(self.client, root)
    await ctx.send(f"Check your DM's, {ctx.message.author.mention}!")
    await h.display(ctx.message.author)

  
  @commands.command()
  async def source(self, ctx):
    await ctx.send("My code can be found here: https://github.com/nerdstep710/YashBot3001")

  @commands.command()
  async def uptime(self, ctx):
    command_time = datetime.datetime.now()
    ut = command_time - c.start_time
    await ctx.send(f"This bot has been alive for {ut}")

  @commands.command()
  async def guilds(self, ctx):
    server_count = len(self.client.guilds)
    await ctx.send(f"I am in **{server_count}** guilds!")

  @commands.command()
  async def users(self, ctx):
    user_count = len(self.client.users)
    await ctx.send(f"I can see **{user_count}** users!")

def setup(client):
  client.add_cog(InfoCog(client))
