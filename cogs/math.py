import discord
from discord.ext import commands
import math
from io import BytesIO
from .utils import async_executor
from discord.ext.commands.cooldowns import BucketType
import aiohttp

@async_executor()
def factorial(ctx, n):
  with ctx.typing():
      f = 1
      while (n > 0):
        f = f * n
        n = n - 1
      return f


class Math(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def square(self, ctx, number):
	  square = lambda x: float(x)**2
	  await ctx.send(f"{number}² is {square(number)}")

  @commands.command()
  async def root(self, ctx, number):
    """Shows the square root of a number"""
    answer = math.sqrt(float(number))
    await ctx.send(f"The square root of {number} is {answer}")
  
  @commands.command()
  async def multiply(self, ctx, number1, number2):
	  multiplied_value = float(number1) * float(number2)
	  await ctx.send(f"{number1} multiplied by {number2} is {multiplied_value}")
  
  @commands.command()
  @commands.cooldown(1,15,BucketType.default) 
  async def factorial(self, ctx, number: int):
    if number > 99999:
      await ctx.send("Sorry, but this command is capped at 99999. Maybe try again?")
      return
    answer = await factorial(ctx, number)
    if len(str(answer)) > 2000:
      try:
        url = await ctx.bot.post_to_mystbin(answer)
        await ctx.send(f"Your result was too long for discord, so I put it here instead! {url}")
      except (aiohttp.ContentTypeError, AssertionError):
        fp = discord.File(BytesIO(str(answer).encode("utf-8")), "out.txt")
        await ctx.send("Your result was too long for discord, so I put it here instead!", file=fp)
    else:
      await ctx.send(answer)

  @commands.command()
  async def exp(self, ctx, number1, number2):
    answer = float(number1) ** float(number2)
    await ctx.send(f"{number1} to the power of {number2} is {answer}")

  @commands.command()
  async def sine(self, ctx, number):
    answer = math.sin(float(number))
    await ctx.send(f"The sine of {number} is {answer}")

  @commands.command()
  async def cos(self, ctx, number):
    answer = math.cos(float(number))
    await ctx.send(f"The cosine of {number} is {answer}")

  @commands.command()
  async def tan(self, ctx, number):
    answer = math.tan(float(number))
    await ctx.send(f"The tangent of {number} is {answer}")

  @commands.command()
  async def divide(self, ctx, number1, number2):
    answer = float(number1) / float(number2)
    await ctx.send(f"{number1} divided by {number2} is {answer}")

  @commands.command()
  async def add(self, ctx, number1, number2):
	  added_value = float(number1) + float(number2)
	  await ctx.send(f"{number1} + {number2} is {added_value}")

  @commands.command()
  async def subtract(self, ctx, number1, number2):
	  subtracted_value = float(number1) - float(number2)
	  await ctx.send(f"{number1} - {number2} is {subtracted_value}")

  @commands.command()
  async def average(self, ctx, *args: int):
    await ctx.send(f"The average is {sum(args) / len(args)}")

def setup(client):
  client.add_cog(Math(client))
