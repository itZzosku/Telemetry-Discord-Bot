import discord
from discord.ext import commands


class Korva(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def korva(self, ctx):
        await ctx.send('https://eune.op.gg/multi_old/query=velivalte%2Chibana%2Coots%C3%B6pis%2Cs%C3%B6pis%2Ckorvameister%2Cidontcarelol%2Ckorva%2Calejandroabuser%2Cadmiredgame%2Crod0')


def setup(client):
    client.add_cog(Korva(client))
