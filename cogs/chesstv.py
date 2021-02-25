import discord
from discord.ext import commands


class Chesstv(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['tv', 'chess'])
    async def chesstv(self, ctx):
        embedvar = discord.Embed(title="Lichess TVs of the major players.", color=0xEFDAB5)
        embedvar.add_field(name="Trollit team page", value=f'{"https://lichess.org/team/trollit"}', inline=False)
        embedvar.add_field(name="JP", value=f'{"https://lichess.org/@/loctifas/tv"}', inline=False)
        embedvar.add_field(name="Ossey", value=f'{"https://lichess.org/@/itZzosku/tv"}', inline=False)
        embedvar.add_field(name="Rippe", value=f'{"https://lichess.org/@/RIPPEROONI/tv"}', inline=False)
        embedvar.add_field(name="Valte", value=f'{"https://lichess.org/@/valdote/tv"}', inline=False)
        embedvar.add_field(name="Vallu", value=f'{"https://lichess.org/@/Intoilija/tv"}', inline=False)
        embedvar.add_field(name="Ietu", value=f'{"https://lichess.org/@/ietu66/tv"}', inline=False)
        await ctx.send(embed=embedvar)


def setup(client):
    client.add_cog(Chesstv(client))
