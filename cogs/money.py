import discord
from discord.ext import commands
import json
import random
from pathlib import Path
import asyncio

class MoneyCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def work(self, ctx):
    salary = random.randint(50, 100)
    filepath = Path(f"cogs/data/bank/{ctx.message.author.name}.json")
    filepath.touch(exist_ok=True)
    with open(filepath, 'r') as f:
      bank = json.load(f)
      old_bal = bank["balance"]
    new_bal = old_bal + salary
    depo = {
      "owner": ctx.message.author.name,
      "balance": new_bal
    }
    with open(filepath, 'w') as f:
      json.dump(depo, f)
    await ctx.send(f"Congratgulations {ctx.message.author.display_name}! You made {salary} coins!")
  
  @commands.command(aliases=["bal", "wallet", "money"])
  async def balance(self, ctx):
    filepath = Path(f"cogs/data/bank/{ctx.message.author.name}.json")
    filepath.touch(exist_ok=True)
    with open(filepath, 'r') as f:
      bank = json.load(f)
    x = bank["balance"]
    await ctx.send(f"You have {x} coins, {ctx.message.author.mention}!")

  @commands.command()
  async def start(self, ctx):
    await ctx.send("Warning: If you already have data, this command will restart all your progress! Would you like to continue?")
    def check(m):
      return m.content == 'yes' and m.channel == ctx.message.channel
    try:
      accept = await self.client.wait_for('message', timeout=30.0, check=check)
    except asyncio.TimeoutError:
      await ctx.send("I guess not, then.")
    else:
      depo = {
        "owner": ctx.message.author.name,
        "balance": 0
      }
      filepath = Path(f"cogs/data/bank/{ctx.message.author.name}.json")
      filepath.touch(exist_ok=True)
      with open(filepath, 'w') as f:
        json.dump(depo, f)
      await ctx.send(f"{ctx.message.author.mention} has begun their journey!")

def setup(client):
  client.add_cog(MoneyCog(client))
