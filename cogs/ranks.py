import discord
import requests
import datetime
from decimal import Decimal
from discord.ext import commands
from requests_html import HTMLSession


class Ranks(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['rank'])
    async def ranks(self, ctx):
        session = HTMLSession()

        r = session.get('https://eune.op.gg/summoner/userName=Rippe98')

        rippe_desc = r.html.xpath('//meta[@name="description"]/@content')
        # print(rippe_desc)

        r = session.get('https://eune.op.gg/summoner/userName=Valte')

        valte_desc = r.html.xpath('//meta[@name="description"]/@content')
        # print(valte_desc)

        r = session.get('https://eune.op.gg/summoner/userName=Ahri%20Abuser')

        tuukka_desc = r.html.xpath('//meta[@name="description"]/@content')
        # print(tuukka_desc)

        r = session.get('https://eune.op.gg/summoner/userName=Veli%20valte')

        korva_desc = r.html.xpath('//meta[@name="description"]/@content')
        # print(korva_desc)

        r = session.get('https://eune.op.gg/summoner/userName=zukoqq')

        korva2_desc = r.html.xpath('//meta[@name="description"]/@content')
        # print(tuukka_desc)

        r = session.get('https://eune.op.gg/summoner/userName=Naikou99')

        naikou_desc = r.html.xpath('//meta[@name="description"]/@content')
        # print(korva_desc)

        embedvar = discord.Embed(title="Ranks of the players.", color=0xbc0057)
        embedvar.add_field(name="\u200b", value=f'{rippe_desc}', inline=False)
        embedvar.add_field(name="\u200b", value=f'{valte_desc}', inline=False)
        embedvar.add_field(name="\u200b", value=f'{korva_desc}', inline=False)
        embedvar.add_field(name="\u200b", value=f'{korva2_desc}', inline=False)
        embedvar.add_field(name="\u200b", value=f'{tuukka_desc}', inline=False)
        embedvar.add_field(name="\u200b", value=f'{naikou_desc}', inline=False)
        await ctx.send(embed=embedvar)


def setup(client):
    client.add_cog(Ranks(client))
