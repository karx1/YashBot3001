import discord
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageFilter
import textwrap
import matplotlib.pyplot as pp


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
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def lisa(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/lisa.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (200,100),text = "\n".join(textwrap.wrap(sent, width=19)),fill = (0,0,0), font = font)
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command(aliases=["pewdiepie", 'felix'])
  async def pewds(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/pewds.jpg')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 18)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (210, 50),text = "\n".join(textwrap.wrap(sent, width=6)),fill = (0,0,0), font = font)
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def gru(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/gru.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 18)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (180, 50),text ="\n".join(textwrap.wrap(sent, width=10)),fill = (0,0,0), font = font)
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def linus(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/linus.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 72)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (575, 100),text="\n".join(textwrap.wrap(sent, width=15)),fill = (0,0,0), font = font)
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def trump(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/frump.jpg')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (375, 300),text="\n".join(textwrap.wrap(sent, width=16)),fill = (0,0,0), font = font)
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def elon(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/elonian.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (225, 100),text="\n".join(textwrap.wrap(sent, width=11)),fill = (0,0,0), font = font)
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))


  @commands.command(aliases=['sponge', 'bob'])
  async def spongebob(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/spongboi.png')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 92)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (710, 95),text="\n".join(textwrap.wrap(sent, width=10)),fill = (0,0,0), font = font)
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command(aliases=['board'])
  async def billboard(self, ctx, *, sent: commands.clean_content):
    bio = BytesIO()
    image = Image.open(r'cogs/data/billboard.jpg')
    font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
    draw = ImageDraw.Draw(image)
    photo = draw.text(xy = (30, 75),text="\n".join(textwrap.wrap(sent, width=32)),fill = (0,0,0), font = font)
    image.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def supreme(self, ctx, *, text=""):
    c = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(title="", description="", colour=c)
    text = text.replace(" ", "%20")
    url = f"https://api.alexflipnote.dev/supreme?text={text}"
    embed.set_image(url=url)
    await ctx.send(embed=embed)

  @commands.command()
  async def deepfry(self, ctx, *, member: discord.Member = None):
    member = member or ctx.message.author
    m = member.avatar_url_as(format='png')
    m = await m.read()
    im = pp.imread(BytesIO(m), 'RGBA')
    im2 = Image.fromarray(im)
    contrast = ImageEnhance.Contrast(im2)
    im2 = contrast.enhance(1000)
    sharpness = ImageEnhance.Sharpness(im2)
    im2 = sharpness.enhance(1000)
    color = ImageEnhance.Color(im2)
    im2 = color.enhance(1000)
    brightness = ImageEnhance.Brightness(im2)
    im2 = brightness.enhance(1000)
    im2.save('cogs/data/out/out.png')
    await ctx.send(file = discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def sad(self, ctx, *, member: discord.Member = None):
    member = member or ctx.message.author
    i = member.avatar_url_as(format='png')
    j = await i.read()
    io = BytesIO(j)
    img = Image.open(io).convert('L')
    img.save('cogs/data/out/out.png')
    await ctx.send(file=discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def emboss(self, ctx, member: discord.Member = None):
    member = member or ctx.message.author
    i = member.avatar_url_as(format='png')
    j = await i .read()
    io = BytesIO(j)
    img = Image.open(io)
    im1 = img.filter(ImageFilter.EMBOSS)
    im1.save('cogs/data/out/out.png')
    await ctx.send(file=discord.File('cogs/data/out/out.png'))

def setup(client):
  client.add_cog(ImageCog(client))
