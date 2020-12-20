import discord
import requests
from decimal import Decimal
from discord.ext import commands


class Temperature(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['temp', 't'])
    async def temperature(self, ctx):
        url = 'http://osseyman.duckdns.org/Latest_Measurements.json'
        r = requests.get(url)
        r_temp = r.json()
        temperaturelong = Decimal(r_temp['Temperature'])
        humiditylong = Decimal(r_temp['Humidity'])
        pressurelong = Decimal(r_temp['Pressure'])

        timestamp = (r_temp['Time'])

        temperature = round(temperaturelong, 1)
        humidity = round(humiditylong, 0)
        pressure = round(pressurelong, 2)

        embedvar = discord.Embed(title="Telemetry from Osseys place :D", color=0xbc0057)
        embedvar.add_field(name="Temperature:", value=f'{temperature} °C', inline=True)
        embedvar.add_field(name="Humidity:", value=f'{humidity} %', inline=True)
        embedvar.add_field(name="Pressure:", value=f'{pressure} hPa', inline=True)
        embedvar.add_field(name="Time from measurement: TODO", value=f'{timestamp}', inline=False)
        await ctx.send(embed=embedvar)


def setup(client):
    client.add_cog(Temperature(client))
