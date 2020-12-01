import discord
from discord.ext import commands


class Jp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jp(self, ctx):
        await ctx.send('https://vitsionline.com/jp.jpg')


def setup(client):
    client.add_cog(Jp(client))
