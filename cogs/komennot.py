import discord
from discord.ext import commands


class Komennot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['list', 'ls'])
    async def komennot(self, ctx):
        embedvar = discord.Embed(title="List of all the commands to TheOsseyBottey", description="!cat, !challenge, !chesstv, !fakecat, "
                                                                               "!jp, !korva, !komennot, !pong, !putki, "
                                                                               "!ranks, !rating, !RHP, !snapshot, "
                                                                               "!temperature", color=0x1abaff)
        await ctx.send(embed=embedvar)


def setup(client):
    client.add_cog(Komennot(client))
