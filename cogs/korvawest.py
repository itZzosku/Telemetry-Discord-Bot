import discord
from discord.ext import commands


class Korvawest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def korvawest(self, ctx):
        await ctx.send('https://euw.op.gg/multi/query=maxiumsfriend%2Caridenso%2C31231513513%2CPALT0S')


def setup(client):
    client.add_cog(Korvawest(client))
