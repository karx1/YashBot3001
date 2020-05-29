import discord
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageFilter, ImageOps
import textwrap
from cogs.utils import async_executor
import numpy as np
import copy
import typing
import os
from cogs.utils import process_url


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
        for i, z in enumerate(way[:, :,]):
            for x, rgb in enumerate(z):
                thing = template[tuple(rgb)]
                way[:, :,][i][x] = thing[1][thing[0]]
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
        loop=0,
    )
    buff.seek(0)
    return buff


@async_executor()
def do_deepfry(im2):
    contrast = ImageEnhance.Contrast(im2)
    im2 = contrast.enhance(1000)
    sharpness = ImageEnhance.Sharpness(im2)
    im2 = sharpness.enhance(1000)
    color = ImageEnhance.Color(im2)
    im2 = color.enhance(1000)
    brightness = ImageEnhance.Brightness(im2)
    im2 = brightness.enhance(1000)
    io = BytesIO()
    im2.save(io, format="png")
    io.seek(0)
    return io


@async_executor()
def do_invert(ctx, image):
    bio = BytesIO()
    with ctx.typing():
        if image.mode == "RGBA":
            r, g, b = image.split()
            rgb_image = Image.merge("RGB", (r, g, b))
            inverted_image = ImageOps.invert(rgb_image)
            inverted_image.save(bio, format="png")
        else:
            im1 = ImageOps.invert(image)
            im1.save(bio, format="png")
        bio.seek(0)
        return bio


@async_executor()
def do_emboss(img):
    im1 = img.filter(ImageFilter.EMBOSS)
    io = BytesIO()
    im1.save(io, format="png")
    io.seek(0)
    return io


@async_executor()
def do_sort(img):
    arr = np.array(img)
    arr = np.sort(arr, axis=1, kind="heapsort")
    im1 = Image.fromarray(arr)
    bio = BytesIO()
    im1.save(bio, format="png")
    bio.seek(0)
    return bio


@async_executor()
def do_outline(img):
    img = img.filter(ImageFilter.FIND_EDGES)
    io = BytesIO()
    img.save(io, format="png")
    io.seek(0)
    return io


@async_executor()
def do_sobel(ctx, img):
    img = img.filter(ImageFilter.FIND_EDGES)
    io = BytesIO()
    with ctx.typing():
        if img.mode == "RGBA":
            r, g, b = img.split()
            rgb_image = Image.merge("RGB", (r, g, b))
            inverted_image = ImageOps.invert(rgb_image)
            inverted_image.save(io, format="png")
        else:
            im1 = ImageOps.invert(img)
            im1.save(io, format="png")

    io.seek(0)
    return io


class Image_(commands.Cog, name="Image"):
    def __init__(self, client):
        self.client = client

    async def cog_before_invoke(self, ctx):
        if 'cogs' in os.getcwd():
            os.chdir("..")

    @commands.command()
    async def kirby(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/birby.png")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(100, 100),
            text="\n".join(textwrap.wrap(sent, width=25)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def lisa(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/lisa.png")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(200, 100),
            text="\n".join(textwrap.wrap(sent, width=19)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command(aliases=["pewdiepie", "felix"])
    async def pewds(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/pewds.jpg")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 18)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(210, 50),
            text="\n".join(textwrap.wrap(sent, width=6)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def gru(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/gru.png")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 18)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(180, 50),
            text="\n".join(textwrap.wrap(sent, width=10)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def linus(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/linus.png")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 72)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(575, 100),
            text="\n".join(textwrap.wrap(sent, width=15)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def trump(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/frump.jpg")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(375, 300),
            text="\n".join(textwrap.wrap(sent, width=16)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def elon(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/elonian.png")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(225, 100),
            text="\n".join(textwrap.wrap(sent, width=11)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command(aliases=["sponge", "bob"])
    async def spongebob(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/spongboi.png")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 92)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(710, 95),
            text="\n".join(textwrap.wrap(sent, width=10)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command(aliases=["board"])
    async def billboard(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"cogs/data/billboard.jpg")
        font = ImageFont.truetype("cogs/data/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(30, 75),
            text="\n".join(textwrap.wrap(sent, width=32)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def supreme(self, ctx, *, text="Supreme"):
        text = text.replace(" ", "%20")
        url = f"https://api.alexflipnote.dev/supreme?text={text}"
        img = await process_url(ctx, url)
        io = BytesIO()
        img.save(io, format="png")
        io.seek(0)
        await ctx.send(file=discord.File(io, "out.png"))

    @commands.command()
    async def deepfry(self, ctx, *, url=None):
        m = await process_url(ctx, url)
        buff = await do_deepfry(m)
        await ctx.send(file=discord.File(buff, "out.png"))

    @commands.command(aliases=["gs", "greyscale"])
    async def grayscale(self, ctx, *, url=None):
        im1 = await process_url(ctx, url)
        img = im1.convert("L")
        buff = BytesIO()
        img.save(buff, format="png")
        buff.seek(0)
        await ctx.send(file=discord.File(buff, "out.png"))

    @commands.command()
    async def emboss(self, ctx, *, url=None):
        img = await process_url(ctx, url)
        buff = await do_emboss(img)
        await ctx.send(file=discord.File(buff, "out.png"))

    @commands.command()
    async def invert(self, ctx, *, url=None):
        image = await process_url(ctx, url)
        buff = await do_invert(ctx, image)
        await ctx.send(file=discord.File(buff, "out.png"))

    @commands.command()
    async def transform(
        self,
        ctx,
        user: typing.Union[discord.Member, discord.User],
        *,
        other: typing.Union[discord.Member, discord.User] = None,
    ):
        """Transform the avatar of one user to that of another and back. Credit to Capn#0001"""

        other = other or ctx.author

        # Save bandwidth
        im1 = Image.open(
            BytesIO(await user.avatar_url_as(format="png", size=256).read())
        )
        im2 = Image.open(
            BytesIO(await other.avatar_url_as(format="png", size=256).read())
        )
        async with ctx.typing():

            if other.id == ctx.author.id:
                buff = await process_transform(im1, im2)
            else:
                buff = await process_transform(im2, im1)

            await ctx.send(file=discord.File(buff, "out.gif"))

    @commands.command()
    async def sort(self, ctx, url=None):
        async with ctx.typing():
            img = await process_url(ctx, url)
            buff = await do_sort(img)
            await ctx.send(file=discord.File(buff, "out.png"))

    @commands.command()
    async def outline(self, ctx, url=None):
        """Finds the edged of an image"""
        img = await process_url(ctx, url)
        io = await do_outline(img)
        await ctx.send(file=discord.File(io, "out.png"))

    @commands.command()
    async def sobel(self, ctx, url=None):
        """Applies a 'sobel filter' to an image"""
        img = await process_url(ctx, url)
        io = await do_sobel(ctx, img)
        await ctx.send(file=discord.File(io, "out.png"))


def setup(client):
    client.add_cog(Image_(client))
