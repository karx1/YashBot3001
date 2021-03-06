import traceback

import discord
from discord.ext import commands
import random
import datetime
import asyncio
from random import getrandbits
from ipaddress import IPv4Address, IPv6Address
from random import randint
import typing
import aiohttp


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        print("oh hello")
        await ctx.send("Hi!")

    @commands.command(aliases=["8ball"])
    async def ball(self, ctx, *, question):
        """Answers a yes or no question"""
        possible_responses = [
            "That is a resounding no.",
            "It is not looking likely.",
            "Too hard to tell.",
            "It is quite possible",
            "That is a definite yes!",
            "Maybe.",
            "There's a good chance.",
        ]
        name = str(ctx.message.author.display_name)
        answer = random.choice(possible_responses)
        avy = str(ctx.message.author.avatar_url)
        embed = await self.client.embed()
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=answer, inline=False)
        embed.set_thumbnail(
            url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png"
        )
        embed.set_author(name=name, icon_url=avy)
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=embed)

    @commands.command()
    async def fight(self, ctx, challenger1="", challenger2=""):
        print("Ready... FIGHT!!!")
        if challenger1 == "":
            challenger2 = ctx.author.mention
        if challenger2 == "":
            challenger2 = ctx.author.mention
        possible_responses = [f"{challenger1} has won!", f"{challenger2} has won!"]
        winner = random.choice(possible_responses)
        await ctx.send(winner)

    @commands.command()
    async def choose(self, ctx, *args):
        """Chooses between a number of choices. For multiple-word choices wrap the choice in quotes, like this: ;choose quoteless "with quotes\""""
        choice = random.choice(args)
        await ctx.send(f"I choose {choice}!")

    @commands.command()
    async def kill(self, ctx, *, target=""):
        print("R.I.P " + str(target))
        if target == "":
            target = ctx.message.author.display_name
        await ctx.send(f"{target} was killed!")

    @commands.command()
    async def bully(self, ctx, *, target=""):
        print("Get him!")
        if target == "":
            target = ctx.message.author.display_name
        await ctx.send(f"I bullied {target}!")

    @commands.command()
    async def eat(self, ctx, *, meal=None):
        await ctx.send(f"{meal} was eaten by {ctx.message.author.display_name}!")

    @commands.command()
    async def tell(
        self, ctx, member: typing.Union[discord.Member, discord.User], *, message
    ):
        await ctx.send(f'{ctx.author.mention} said "{message}" to {member.mention}!')

    @commands.command()
    async def rate(self, ctx, *, member: discord.Member = None):
        if member == None:
            member = ctx.message.author
        possible_responses = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        rating = random.choice(possible_responses)
        await ctx.send(f"I rate {member.mention} {rating} out of 10!")

    @commands.command()
    async def coin(self, ctx):
        print("Coinflip!")
        possible_responses = ["heads", "tails"]
        flipped_value = random.choice(possible_responses)
        await ctx.send(f"You got {flipped_value}!")

    @commands.command()
    async def dice(self, ctx):
        print("Roll!")
        possible_responses = ["1", "2", "3", "4", "5", "6"]
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
        embed = await self.client.embed(
            title="Pong!", description=f"Latency is {w} ms."
        )
        embed.colour = 0x00FF00
        embed.set_image(url="https://media.giphy.com/media/pWncxUrrNHdny/giphy.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def thanos(self, ctx, *, target=""):
        if target == "":
            target = ctx.message.author.display_name
        possible_responses = [
            f"{target} was spared by the great titan Thanos.",
            f"{target} was sacrificed for the greater good of the universe. Perfectly balanced, as all things should be.",
        ]
        answer = random.choice(possible_responses)
        await ctx.send(answer)

    @commands.command()
    async def song(self, ctx):
        print("Have some tunes!")
        possible_responses = [
            "The Superstar - https://www.youtube.com/watch?v=fdYh8TC5TdA",
            "Slide - https://www.youtube.com/watch?v=88qwvurm4SU",
            "Alone Remix - https://www.youtube.com/watch?v=QdEtsRW48jE",
            "Supernova - https://www.youtube.com/watch?v=6l6EZQJFadQ",
            "The Dark - https://www.youtube.com/watch?v=_zeZXThhtAI",
            "Hip Hop Bop - https://www.youtube.com/watch?v=T6FyYIVr9MQ",
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def rps(self, ctx, choice):
        choice = choice.lower()
        possible_choices = ["rock", "paper", "scissors"]
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
        embed = await self.client.embed(description="Rock Paper Scissors!")
        embed.add_field(name=f"{name}'s Choice", value=choice, inline=False)
        embed.add_field(name="My Choice", value=var1, inline=False)
        embed.add_field(name="Results:", value=winner, inline=False)
        embed.set_thumbnail(url=thumb)
        embed.set_author(name=name, icon_url=avy)
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=embed)

    @commands.command()
    async def hack(self, ctx, *, target: discord.Member = None):
        if target is None:
            target = ctx.message.author
        v = 4
        if v == 4:
            bits = getrandbits(32)  # generates an integer with 32 random bits
            addr = IPv4Address(bits)  # instances an IPv4Address object from those bits
            a = str(addr)  # get the IPv4Address object's string representation
        elif v == 6:
            bits = getrandbits(128)  # generates an integer with 128 random bits
            addr = IPv6Address(bits)  # instances an IPv6Address object from those bits
            # .compressed contains the short version of the IPv6 address
            # str(addr) always returns the short address
            # .exploded is the opposite of this, always returning the full address with all-zero groups and so on
            a = addr.compressed

        async def random_with_N_digits(n):
            range_start = 10 ** (n - 1)
            range_end = (10 ** n) - 1
            return randint(range_start, range_end)

        f = await random_with_N_digits(4)
        b = target.name.lower()
        b = b.replace(" ", "")
        j = await random_with_N_digits(5)
        if j > 65535:
            j = 65535
        message = await ctx.send("```css\nHacking...```")
        await asyncio.sleep(2)
        await message.edit(content="```css\nHacking...\nMember found!```")
        await asyncio.sleep(2)
        await message.edit(
            content="```css\nHacking...\nMember found!\nGetting ip...```"
        )
        await asyncio.sleep(2)
        await message.edit(
            content="```css\nHacking...\nMember found!\nGetting ip...\nip found```"
        )
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address```"
        )
        await asyncio.sleep(2)
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...```"
        )
        await asyncio.sleep(2)
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com```"
        )
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******```"
        )
        await asyncio.sleep(2)
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...```"
        )
        await asyncio.sleep(2)
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.```"
        )
        await asyncio.sleep(2)
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...```"
        )
        await asyncio.sleep(2)
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...\nConnection Closed.```"
        )
        await message.edit(
            content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...\nConnection Closed.\nExited port {j}```"
        )
        await asyncio.sleep(2)
        await ctx.send(f"Finished hacking user **{target.display_name}**.")

    @commands.command()
    async def maze(self, ctx):
        """Maze Game!"""
        m = await ctx.send("Welcome to MAZE GAME!\ntype `start` to continue.")

        def check(m):
            return m.content.lower() == "start"

        msg = await self.client.wait_for("message", check=check)
        await m.delete()
        m = await ctx.send(
            f"Welcome {msg.author.mention}!\nYou are in a dark cavern. you can go forward or right."
        )

        def check(m):
            return m.content.lower() == "forward"

        msg = await self.client.wait_for("message", check=check)
        if msg.content.lower() == "forward":
            await m.delete()
            m = await ctx.send(
                "you went forward and came out of the cave. There you see a sword. Will you pick it up? Type `yes` or `no`."
            )

            def check(m):
                return m.content.lower() == "yes"

            msg = await self.client.wait_for("message", check=check)
            if msg.content.lower() == "yes":
                await m.delete()
                await ctx.send("You picked up the sword!")
                m = await ctx.send(
                    "After wandering around for a while, you encountered a dragon! will you `fight` or `flee`?"
                )

                def check(m):
                    return m.content.lower() == "fight"

                msg = await self.client.wait_for("message", check=check)
                if msg.content.lower() == "fight":
                    await m.delete()
                    await ctx.send(
                        "You fought with your best efforts and vanquished the dragon!"
                    )
                else:
                    await m.delete()
                    await ctx.send(
                        "You decide to run away, but the dragon is much faster. It eats you up in one massive gulp and files away."
                    )
            else:
                await m.delete()
                await ctx.send(
                    "You decided not to pick up the sword. This may have been a mistake."
                )

    @commands.command()
    async def bitcoin(self, ctx):
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.json(content_type="application/javascript")
            await ctx.send(f"Bitcoin price is: ${response['bpi']['USD']['rate']}")

    @commands.command(name="bot")
    async def _bot(self, ctx, member: typing.Union[discord.Member, discord.User], *, message: str):
        name = member.nick or member.name
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=name)
        await webhook.send(content=message, avatar_url=str(member.avatar_url))
        await webhook.delete()

    @_bot.error
    async def _bot_error(self, ctx, error):
        # await ctx.send(error.__class__)
        # await ctx.send(error)
        if isinstance(error, commands.MissingRequiredArgument):
            if "member" in error.param.name:
                return await ctx.send("You forgot to provide a member!")
            elif "message" in error.param.name:
                return await ctx.send("You forgot to provide something to say!")
        elif isinstance(error, commands.CommandInvokeError):
            # await ctx.send(error.original.__class__)
            if isinstance(error.original, discord.errors.Forbidden):
                return await ctx.send("I can't complete that command here, because I'm not allowed to!")
        elif isinstance(error, commands.BadUnionArgument):
            return await ctx.send("That user does not exist!")


def setup(client):
    client.add_cog(Fun(client))
