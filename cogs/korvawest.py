import discord
from discord.ext import commands


class Korvawest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def korvawest(self, ctx):
        await ctx.send('maxiumsfriend,aridenso,31231513513,PALT0S')


def setup(client):
    client.add_cog(Korvawest(client))
