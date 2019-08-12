import asyncio
from discord.ext import commands
import PIL
from io import BytesIO
import aiohttp


async def process_url(ctx, argument):
    if argument is None:
        is_found = False
        for att in ctx.message.attachments:
            if att.height is not None and not is_found:
                url = att.proxy_url
                is_found = True
        if not is_found:
            url = str(ctx.author.avatar_url_as(format="png", size=1024))
    else:
        try:
            url = str(
                (await commands.MemberConverter().convert(ctx, argument)).avatar_url_as(format="png", size=1024)
            )
        except commands.BadArgument:
            try:
                url = str(
                    (await commands.UserConverter().convert(ctx, argument)).avatar_url_as(format="png", size=1024)
                )
            except commands.BadArgument:
                url = argument

    try:
        async with ctx.bot.http2.get(url) as resp:
            try:
                img = PIL.Image.open(BytesIO(await resp.content.read())).convert("RGB")
            except OSError:
              if ctx.command.qualified_name == "sort":
                return #error handler caught it
              else:
                await ctx.send(":x: That URL is not an image.")
                return
    except aiohttp.InvalidURL:
      if ctx.command.qualified_name == "sort":
        return #error handler caught it
      else:
        await ctx.send(":x: That URL is invalid.")
        return

    return img