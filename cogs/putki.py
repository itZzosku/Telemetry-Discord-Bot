import discord
from discord.ext import commands


class Putki(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def putki(self, ctx):
        await ctx.send('https://vitsionline.com/putki.png')


def setup(client):
    client.add_cog(Putki(client))
