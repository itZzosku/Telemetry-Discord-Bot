import discord
import requests
from discord.ext import commands


class Cat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        url = 'https://aws.random.cat/meow'
        r = requests.get(url)
        r_dict = r.json()
        # print(r_dict['file'])
        await ctx.send(r_dict['file'])


def setup(client):
    client.add_cog(Cat(client))
