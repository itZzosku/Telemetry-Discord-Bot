import discord
import requests
import datetime
from decimal import Decimal
from discord.ext import commands


class Temperature(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['temp', 't'])
    async def temperature(self, ctx):
        url = 'https://osseyman.duckdns.org/Latest_Measurements.json'
        r = requests.get(url)
        r_temp = r.json()
        sensor = (r_temp['Sensor'])
        temperaturelong = Decimal(r_temp['Temperature'])
        humiditylong = Decimal(r_temp['Humidity'])
        pressurelong = Decimal(r_temp['Pressure'])

        timestamp_string = (r_temp['Time'])
        timestamp_object = int(timestamp_string)

        cutime = datetime.datetime.now()
        seconds_since_epoch = int(cutime.timestamp())

        dtime = seconds_since_epoch - timestamp_object

        temperature = round(temperaturelong, 1)
        humidity = round(humiditylong, 0)
        pressure = round(pressurelong, 2)

        embedvar = discord.Embed(title="Telemetry from Osseys place", color=0xbc0057)
        embedvar.add_field(name="Sensor:", value=f'{sensor}', inline=False)
        embedvar.add_field(name="Temperature:", value=f'{temperature} °C', inline=True)
        embedvar.add_field(name="Humidity:", value=f'{humidity} %', inline=True)
        embedvar.add_field(name="Pressure:", value=f'{pressure} hPa', inline=True)
        embedvar.add_field(name="Time from measurement:", value=f'{dtime} Seconds', inline=False)
        await ctx.send(embed=embedvar)


def setup(client):
    client.add_cog(Temperature(client))
