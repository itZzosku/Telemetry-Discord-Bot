import discord
import lichess.api
from discord.ext import commands


class Challenge(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['chal', 'haaste'])
    async def challenge(self, ctx):
        print("TODO")


def setup(client):
    client.add_cog(Challenge(client))
