import discord
from discord.ext import commands
from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup

class WebCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def google(self, ctx, *, query=""):
    name = str(ctx.message.author)
    name_plain = ctx.message.author.display_name
    if query is "":
      await ctx.send("You must provide a search term, {}!".format(name_plain))
      return
    await ctx.trigger_typing()
    for j in search(query, tld="com", num=1, stop=1):
      print("{} has searched for '{}' and it returned {}".format(name, query, j))
      await ctx.send(j)

  @commands.command()
  async def youtube(self, ctx, *, query=""):
    r = 0
    if query == "":
      await ctx.send("You must provide a search term, {}!".format(ctx.author.mention))
    async with ctx.typing():
      search = urllib.parse.quote(query)
      url = "https://www.youtube.com/results?search_query={}".format(search)
      response = urllib.request.urlopen(url)
      html = response.read()
      soup = BeautifulSoup(html, 'html.parser')
      for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        while r == 0:
          await ctx.send('https://www.youtube.com{}'.format(vid['href']))
          print("{} has searched for '{}'.".format(str(ctx.message.author), query))
          r = r + 1

def setup(client):
  client.add_cog(WebCog(client))
