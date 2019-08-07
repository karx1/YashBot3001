import discord
from discord.ext import commands
from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import wikipedia
import aiohttp
from io import BytesIO


class Web(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def google(self, ctx, *, query):
    """Searches Google"""
    def gsync(query=query):
      name = str(ctx.message.author)
      for j in search(query, tld="com", num=1, stop=1):
        print(f"{name} has searched for '{query}' and it returned {j}")
        return j
    async with ctx.typing():
      gasync = await self.client.loop.run_in_executor(ThreadPoolExecutor(), gsync)
      await ctx.send(gasync)

    
  @commands.command()
  async def youtube(self, ctx, *, query):
    def ytsync(query=query):
      """Searches YouTube"""
      r = 0
      search = urllib.parse.quote(query)
      url = f"https://www.youtube.com/results?search_query={search}"
      response = urllib.request.urlopen(url)
      html = response.read()
      soup = BeautifulSoup(html, 'html.parser')
      for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        while r == 0:
          return f"https://www.youtube.com{vid['href']}"
          r = r + 1
    async with ctx.typing():
      ytasync = await self.client.loop.run_in_executor(ThreadPoolExecutor(), ytsync)
      await ctx.send(ytasync)


  @commands.command(aliases=["wikipedia", "define"])
  async def wiki(self, ctx, *, query):
    """Searches Wikipedia"""
    c = wikipedia.summary(query)
    content = f"{c}"
    if len(content) > 2000:
      try:
        url = await self.client.post_to_mystbin(content)
        await ctx.send(f"Your result was too long for discord, so I put it here instead! {url}")
      except (aiohttp.ContentTypeError, AssertionError):
        fp = discord.File(BytesIO(str(content).encode("utf-8")), "out.txt")
        await ctx.send("Your result was too long for discord, so I put it here instead!", file=fp)
    else:
      await ctx.send(content)

  @commands.group(invoke_without_command=True, aliases=['r'])
  async def reddit(self, ctx):
    """Searches reddit for a subreddit or user"""
    await ctx.send_help(ctx.command)

  @reddit.command(aliases=['s'])
  async def subreddit(self, ctx, query):
    """Command for subreddit"""
    query = query.lower().replace(" ", "%20")
    await ctx.send(f"https://www.reddit.com/r/{query}/")
  
  @reddit.command(aliases=['u'])
  async def user(self, ctx, query):
    """Command for user"""
    query = query.replace(" ", "%20")
    await ctx.send(f"https://www.reddit.com/user/{query}")

def setup(client):
  client.add_cog(Web(client))