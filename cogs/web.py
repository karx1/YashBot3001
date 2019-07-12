import discord
from discord.ext import commands
from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import wikipedia
import aiohttp
import textwrap



class WebCog(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command()
  async def google(self, ctx, *, q=""):
    def gsync(query=q):
      name = str(ctx.message.author)
      name_plain = ctx.message.author.display_name
      if query is "":
        return f"You must provide a search term, {name_plain}!"
      for j in search(query, tld="com", num=1, stop=1):
        print(f"{name} has searched for '{query}' and it returned {j}")
        return j
    async with ctx.typing():
      gasync = await self.client.loop.run_in_executor(ThreadPoolExecutor(), gsync)
      await ctx.send(gasync)

      

  @commands.command()
  async def youtube(self, ctx, *, q=""):
    def ytsync(query=q):
      r = 0
      if query == "":
        return f"You must provide a search term, {ctx.author.mention}!"
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
  async def wiki(self, ctx, *, query=""):
    if query is "":
      await ctx.send("You must provide a search term, {ctx.message.author.mention}!")
    c = wikipedia.summary(query)
    content = f"{c}"
    if len(content) > 2000:
      h = "\n".join(textwrap.wrap(content, width=143))
      async with aiohttp.ClientSession() as session:
        resp = await session.post('https://mystb.in/documents', data=h.encode())
        f = await resp.json()
        url = f'https://mystb.in/{f["key"]}'
        await ctx.send(f"Your result was too long for discord, so I put it here instead! {url}")
    else:
      await ctx.send(content)

  @commands.command()
  async def reddit(self, ctx, query):
    query = query.replace(" ", "%20")
    await ctx.send(f"https://www.reddit.com/r/{query}")

def setup(client):
  client.add_cog(WebCog(client))
