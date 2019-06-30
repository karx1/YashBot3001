import discord
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageFilter, ImageOps
import textwrap
import matplotlib.pyplot as pp
from concurrent.futures import ThreadPoolExecutor
from .utils import async_executor
import numpy as np
import copy
import typing

def link(arr, arr2):
    rgb1 = arr.reshape((arr.shape[0] * arr.shape[1], 3))
    rgb2 = list(map(tuple, arr2.reshape((arr2.shape[0] * arr2.shape[1], 3))))
    template1 = {x: [0, []] for x in rgb2}
    for x, y in zip(rgb2, rgb1):
        template1[x][1].append(y)
    return template1

def reset_template(template):
    for v in template.values():
        v[0] = 0

def process_sorting(img, img2):
    arr = np.array(img)
    arr2 = np.array(img2)

    shape = arr.shape
    npixs = shape[0] * shape[1]
    valid = []
    for i in range(1, npixs + 1):
        num = npixs / i
        if num.is_integer():
            valid.append((int(num), i))

    frames = []
    way_back = []
    for v in valid:
        arr = arr.reshape((v[0], v[1], shape[2]))
        arr.view("uint8,uint8,uint8").sort(order=["f2"], axis=1)
        arr2 = arr2.reshape((v[0], v[1], shape[2]))
        arr2.view("uint8,uint8,uint8").sort(order=["f2"], axis=1)
        new = Image.fromarray(arr.reshape(shape))
        frames.append(new)
        ar2 = copy.copy(arr2)
        way_back.append(ar2)

    template = link(arr, arr2)

    for way in reversed(way_back):
        for i, z in enumerate(way[:, :, ]):
            for x, rgb in enumerate(z):
                thing = template[tuple(rgb)]
                way[:, :, ][i][x] = thing[1][thing[0]]
                thing[0] += 1
        new = Image.fromarray(way.reshape(shape))
        frames.append(new)
        reset_template(template)

    for i in range(5):
        frames.insert(0, frames[0])
        frames.append(frames[-1])
    frames += list(reversed(frames))
    return frames

@async_executor()
def process_transform(img1, img2):
    img1 = img1.resize((256, 256), Image.NEAREST)
    if img1.mode != "RGB":
        img1 = img1.convert("RGB")
    img2 = img2.resize((256, 256), Image.NEAREST)
    if img2.mode != "RGB":
        img2 = img2.convert("RGB")
    frames = process_sorting(img1, img2)

    buff = BytesIO()
    frames[0].save(
            buff,
            "gif",
            save_all=True,
            append_images=frames[1:] + frames[-1:] * 5,
            duration=125,
            loop=0
        )
    buff.seek(0)
    return buff

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
  async def deepfry(self, ctx, *, member: typing.Union[discord.Member, discord.User] = None):
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
  async def sad(self, ctx, *, member: typing.Union[discord.Member, discord.User] = None):
    member = member or ctx.message.author
    i = member.avatar_url_as(format='png')
    j = await i.read()
    io = BytesIO(j)
    img = Image.open(io).convert('L')
    img.save('cogs/data/out/out.png')
    await ctx.send(file=discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def emboss(self, ctx, *, member: typing.Union[discord.Member, discord.User] = None):
    member = member or ctx.message.author
    i = member.avatar_url_as(format='png')
    j = await i.read()
    io = BytesIO(j)
    img = Image.open(io)
    im1 = img.filter(ImageFilter.EMBOSS)
    im1.save('cogs/data/out/out.png')
    await ctx.send(file=discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def invert(self, ctx, *, member: typing.Union[discord.Member, discord.User] = None):
    member = member or ctx.message.author
    i = member.avatar_url_as(format='png')
    j = await i.read()
    io = BytesIO(j)
    image = Image.open(io)
    def isync(image=image):
      if image.mode == 'RGBA':
        r,g,b,a = image.split()
        rgb_image = Image.merge('RGB', (r,g,b))
        inverted_image = ImageOps.invert(rgb_image)
        inverted_image.save('cogs/data/out/out.png')
      else:
        im1 = ImageOps.invert(image)
        im1.save('cogs/data/out/out.png')
    async with ctx.typing():
      await self.client.loop.run_in_executor(ThreadPoolExecutor(), isync)
      await ctx.send(file=discord.File('cogs/data/out/out.png'))

  @commands.command()
  async def transform(
          self, ctx,
          user: typing.Union[discord.Member, discord.User],
            *, other: typing.Union[discord.Member, discord.User] = None):
        """Transform the avatar of one user to that of another and back. Credit goes to Capn#0001"""

        other = other or ctx.author

        # Save bandwidth
        im1 = Image.open(BytesIO(await user.avatar_url_as(format="png", size=256).read()))
        im2 = Image.open(BytesIO(await other.avatar_url_as(format="png", size=256).read()))
        async with ctx.typing():

            if other.id == ctx.author.id:
                buff = await process_transform(im1, im2)
            else:
                buff = await process_transform(im2, im1)


            await ctx.send(file=discord.File(buff, "out.gif"))



def setup(client):
  client.add_cog(ImageCog(client))
