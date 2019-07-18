import discord
from discord.ext import commands
import math


class Math(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def square(self, ctx, number):
	  squared_value = float(number) * float(number)
	  await ctx.send(f"{number}² is {squared_value}")

  @commands.command()
  async def root(self, ctx, number):
	  answer = math.sqrt(float(number))
	  await ctx.send(f"The square root of {number} is {answer}")
  
  @commands.command()
  async def multiply(self, ctx, number1, number2):
	  multiplied_value = float(number1) * float(number2)
	  await ctx.send(f"{number1} multiplied by {number2} is {multiplied_value}")
  
  @commands.command(aliases=["fact"])
  async def factorial(self, ctx, number):
    number = int(number)
    if number > 802:
      await ctx.send("Sorry, but your number is too big! We don't want Discord getting mad at us, after all.")
      return
    answer = math.factorial(number)
    await ctx.send(f"{number} factorial is {answer}")

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

def setup(client):
  client.add_cog(Math(client))