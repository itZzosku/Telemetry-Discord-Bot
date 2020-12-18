import discord
import requests
import os
from discord.ext import commands


class Fakecat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fakecat(self, ctx):
        url = 'https://thiscatdoesnotexist.com'
        r = requests.get(url, allow_redirects=True)
        open('fakecat.jpg', 'wb').write(r.content)
        file = discord.File("/home/pi/IOTstack/volumes/python/app/fakecat.jpg", filename="fakecat.jpg")
        await ctx.send(file=file)
        os.remove("fakecat.jpg")


def setup(client):
    client.add_cog(Fakecat(client))
