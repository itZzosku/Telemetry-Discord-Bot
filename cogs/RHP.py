import discord
from discord.ext import commands


class RHP(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['RHP', 'rippe', 'Rippe'])
    async def rhp(self, ctx):
        await ctx.send('Rippe Has Problems!')


def setup(client):
    client.add_cog(RHP(client))
