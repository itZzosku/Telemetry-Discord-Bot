import discord
from discord.ext import commands


class Pong(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f'Ping! {round(self.client.latency * 1000)} ms')


def setup(client):
    client.add_cog(Pong(client))
