import discord
from discord.ext import commands
import random
import datetime

class FunCog(commands.Cog):
  def __init__(self, client):
    self.client = client
  

  @commands.command()
  async def hello(self, ctx):
    print("oh hello")
    await ctx.send("Hi!")

  @commands.command(aliases=["8ball"])
  async def ball(self, ctx, *, question=""):
    if question is "":
      await ctx.send("You must ask a question!")
      return
    elif '?' not in question:
      await ctx.send("You must ask a question!")
      return
    possible_responses = [
      'That is a resounding no.',
      'It is not looking likely.',
      'Too hard to tell.',
      'It is quite possible',
      'That is a definite yes!',
	  	"Maybe.",
	  	"There's a good chance."
    ]
    name = str(ctx.message.author.display_name)
    answer = random.choice(possible_responses)
    avy = str(ctx.message.author.avatar_url)
    embed=discord.Embed(title="", description="", color=0x00ff00)
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_author(name=name, icon_url=avy)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)


  @commands.command()
  async def fight(self, ctx, challenger1="", challenger2=""):
    print("Ready... FIGHT!!!")
    if challenger1 == "":
      challenger2 = ctx.author.mention
    elif challenger2 == "":
      challenger2 = ctx.author.mention
    possible_responses = [
      f'{challenger1} has won!',
      f'{challenger2} has won!'
    ]    
    winner = random.choice(possible_responses)
    await ctx.send(winner)


  @commands.command()
  async def kill(self, ctx, *, target=""):
    print("R.I.P " + str(target))
    if target is "":
      target = ctx.message.author.display_name
    await ctx.send(f'{target} was killed!')


  @commands.command()
  async def bully(self, ctx, *, target=""):
    print("Get him!")
    if target is "":
      target = ctx.message.author.display_name
    await ctx.send(f"{target} was killed!")

  @commands.command()
  async def rate(self, ctx):
    possible_responses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    rating = random.choice(possible_responses)
    await ctx.send(f"I rate {ctx.author.mention} {rating} out of 10!")


  @commands.command()
  async def coin(self, ctx):
    print("Coinflip!")
    possible_responses = [
      'heads',
      'tails'
    ]
    flipped_value = random.choice(possible_responses)
    await ctx.send(f"You got {flipped_value}!")


  @commands.command()
  async def dice(self, ctx):
    print("Roll!")
    possible_responses = [
      '1',
      '2',
      '3',
      '4',
      '5',
      '6'
    ]
    rolled_value = random.choice(possible_responses)
    await ctx.send(f"You rolled a {rolled_value}!")


  @commands.command()
  async def cat(self, ctx):
    await ctx.send("https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif")


  @commands.command()
  async def dog(self, ctx):
    await ctx.send("https://media.giphy.com/media/fnlXXGImVWB0RYWWQj/giphy.gif")


  @commands.command()
  async def hamster(self, ctx):
    await ctx.send("https://media.giphy.com/media/HrB1MUATg24Ra/giphy.gif")


  @commands.command()
  async def ping(self, ctx):
    w = self.client.latency
    w = w * 1000
    w = round(w, 4)
    m = await ctx.send("Pong!")
    await m.edit(content=f"Pong! Latency is {w} ms.\nhttps://media.giphy.com/media/pWncxUrrNHdny/giphy.gif")


  @commands.command()
  async def thanos(self, ctx, *, target=""):
    if target is "":
      target = ctx.message.author.display_name
    possible_responses = [
      f'{target} was spared by the great titan Thanos.',
      f'{target} was sacrificed for the greater good of the universe. Perfectly balanced, as all things should be.'
    ]
    answer = random.choice(possible_responses)
    await ctx.send(answer)

  @commands.command()
  async def song(self, ctx):
    print("Have some tunes!")
    possible_responses = [
        'The Superstar - https://www.youtube.com/watch?v=fdYh8TC5TdA',
        'Slide - https://www.youtube.com/watch?v=88qwvurm4SU',
        'Alone Remix - https://www.youtube.com/watch?v=QdEtsRW48jE',
        'Supernova - https://www.youtube.com/watch?v=6l6EZQJFadQ',
        'The Dark - https://www.youtube.com/watch?v=_zeZXThhtAI',
        'Hip Hop Bop - https://www.youtube.com/watch?v=T6FyYIVr9MQ',
    ]
    await ctx.send(random.choice(possible_responses))

  @commands.command()
  async def rps(self, ctx, choice=""):
    choice = choice.lower()
    possible_choices = [
      'rock',
      'paper',
      'scissors'
    ]
    avy = str(ctx.message.author.avatar_url)
    name = ctx.message.author.display_name
    var1 = random.choice(possible_choices)
    if choice == "rock":
      thumb = "https://pngimg.com/uploads/stone/stone_PNG13545.png"
      if var1 == "paper":
        winner = "Yay! I won!"
      elif var1 == "rock":
        winner = "It's a tie!"
      elif var1 == "scissors":
        winner = f"{name} wins!"
      else:
        winner = "woahhhhh"
    elif choice == "paper":
      thumb = "https://cdn.pixabay.com/photo/2017/10/07/21/57/pape-2828083_960_720.png"
      if var1 == "rock":
        winner = f"{name} wins!"
      elif var1 == "paper":
        winner = "It's a tie!"
      elif var1 == "scissors":
        winner = "Yay! I win!"
      else:
        winner = "woahhhhh"
    elif choice == "scissors":
      thumb = "https://pngimg.com/uploads/scissors/scissors_PNG25.png"
      if var1 == "rock":
        winner = "Yay! I won!"
      elif var1 == "paper":
        winner = f"{name} wins!"
      elif var1 == "scissors":
        winner = "It's a tie!"
    else:
      await ctx.send("You must either say rock, paper, or scissors!")
      return
    embed=discord.Embed(title="", description="Rock Paper Scissors!", color=0x00ff00)
    embed.add_field(name=f"{name}'s Choice", value=choice, inline=False)
    embed.add_field(name="My Choice", value=var1, inline=False)
    embed.add_field(name="Results:", value=winner, inline=False)
    embed.set_thumbnail(url=thumb)
    embed.set_author(name=name, icon_url=avy)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(FunCog(client))
