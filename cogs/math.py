import discord
from discord.ext import commands
import math

class MathCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def square(self, ctx, number=None):
	  if number is None:
	  	await ctx.send("You must provide a number to square.")
	  squared_value = float(number) * float(number)
	  await ctx.send("{}² is {}".format(number, squared_value))

  @commands.command()
  async def root(self, ctx, number=None):
	  if number is None:
	  	await ctx.send("You must provide a number.")
	  	return
	  answer = math.sqrt(float(number))
	  await ctx.send("The square root of {} is {}".format(number, answer))
  
  @commands.command()
  async def multiply(self, ctx, number1=None, number2=None):
	  if number1 is None or number2 is None:
	  	await ctx.send("You must provide two numbers to multiply, separated by a space.")
	  multiplied_value = float(number1) * float(number2)
	  await ctx.send("{} multiplied by {} is {}".format(number1, number2, multiplied_value))
  
  @commands.command()
  async def factorial(self, ctx, number=None):
    if number is None:
      await ctx.send("You must provide a number!")
      return
    number = int(number)
    answer = math.factorial(number)
    await ctx.send("{} factorial is {}".format(number, answer))

  @commands.command()
  async def exp(self, ctx, number1=None, number2=None):
    if number1 is None or number2 is None:
      await ctx.send("You must provide two numbers, separated with a space.")
    answer = float(number1) ** float(number2)
    await ctx.send("{} to the power of {} is {}".format(number1, number2, answer))

  @commands.command()
  async def sine(self, ctx, number=None):
    if number is None:
      await ctx.send("You must provide a number!")
      return
    answer = math.sin(float(number))
    await ctx.send("The sine of {} is {}".format(number, answer))

  @commands.command()
  async def cos(self, ctx, number=None):
    if number is None:
      await ctx.send("You must provide a number!")
      return
    answer = math.cos(float(number))
    await ctx.send("The cosine of {} is {}".format(number, answer))

  @commands.command()
  async def tan(self, ctx, number=None):
    if number is None:
      await ctx.send("You must provide a number!")
      return
    answer = math.tan(float(number))
    await ctx.send("The tangent of {} is {}".format(number, answer))

  @commands.command()
  async def divide(self, ctx, number1=None, number2=None):
    if number1 is None or number2 is None:
      await ctx.send("You must provide two numbers to divide, separated by a space.")
      return  
    answer = float(number1) / float(number2)
    await ctx.send("{} divided by {} is {}".format(number1, number2, answer))

  @commands.command()
  async def add(self, ctx, number1=None, number2=None):
	  if number1 is None or number2 is None:
	  	await ctx.send("You must provide two numbers to add, separated by a space.")
	  	return 
	  added_value = float(number1) + float(number2)
	  await ctx.send("{} + {} is {}".format(number1, number2, added_value))

  @commands.command()
  async def subtract(self, ctx, number1=None, number2=None):
	  if number1 is None or number2 is None:
		  await ctx.send("You must provide two numbers to subtract, separated by a space.")
		  return  
	  subtracted_value = float(number1) - float(number2)
	  await ctx.send("{} - {} is {}".format(number1, number2, subtracted_value))

def setup(client):
  client.add_cog(MathCog(client))
