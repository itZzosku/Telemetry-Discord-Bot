import discord
from discord.ext import commands


class List(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['list', 'ls'])
    async def list(self, ctx):
        embedvar = discord.Embed(title="List of all the commands", color=0xbc0057)
        embedvar.add_field(name="List of all the commands:", value=f"!cat, !challenge, !chesstv, !fakecat, !jp, !korva, !list, !pong, !putki, !ranks, !rating, !RHP, !snapshot, !temperature", inline=True)
        await ctx.send(embed=embedvar)


def setup(client):
    client.add_cog(List(client))
