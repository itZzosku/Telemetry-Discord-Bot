import discord
from discord.ext import commands
import random


class Roll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['random'])
    async def roll(self, ctx):
        n = random.randint(1, 999)
        await ctx.send(n)


def setup(client):
    client.add_cog(Roll(client))
