import discord
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
import textwrap


class ImageCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def kirby(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/birby.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (100,100),text = "\n".join(textwrap.wrap(sent, width=25)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def lisa(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/lisa.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (200,100),text = "\n".join(textwrap.wrap(sent, width=19)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def pewds(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/pewds.jpg')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 18)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (210, 50),text = "\n".join(textwrap.wrap(sent, width=6)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def gru(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/gru.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 18)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (180, 50),text ="\n".join(textwrap.wrap(sent, width=10)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def linus(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/linus.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 72)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (575, 100),text="\n".join(textwrap.wrap(sent, width=15)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def trump(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/frump.jpg')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (375, 300),text="\n".join(textwrap.wrap(sent, width=16)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def elon(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/elonian.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (225, 100),text="\n".join(textwrap.wrap(sent, width=11)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))


  @commands.command(aliases=['sponge', 'bob'])
  async def spongebob(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/spongboi.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 92)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (710, 95),text="\n".join(textwrap.wrap(sent, width=10)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command(aliases=['board'])
  async def billboard(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/billboard.jpg')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (30, 75),text="\n".join(textwrap.wrap(sent, width=32)),fill = (0,0,0), font = font)
    save = image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

def setup(client):
  client.add_cog(ImageCog(client))
