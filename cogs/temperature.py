import discord
import requests
from decimal import Decimal
from discord.ext import commands


def read_keys():
    with open("keys.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


keys = read_keys()


class Temperature(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['temp', 't'])
    async def temperature(self, ctx):
        payload = {'api_key': keys, 'timezone': 'Europe/Helsinki'}
        url1 = 'https://api.thingspeak.com/channels/1241589/feeds/last.json?'
        url2 = 'https://api.thingspeak.com/channels/1241589/feeds/last_data_age.json?'
        r1 = requests.get(url1, params=payload)
        r2 = requests.get(url2, params=payload)
        r_temp = r1.json()
        r_time = r2.json()
        temperaturelong = Decimal(r_temp['field1'])
        humiditylong = Decimal(r_temp['field2'])
        pressurelong = Decimal(r_temp['field3'])

        temperature = round(temperaturelong, 1)
        humidity = round(humiditylong, 0)
        pressure = round(pressurelong, 2)

        last_data_age = (r_time['last_data_age'])
        last_data_age_units = (r_time['last_data_age_units'])

        embedvar = discord.Embed(title="Telemetry from Osseys place :D", color=0xbc0057)
        embedvar.add_field(name="Temperature:", value=f'{temperature} °C', inline=True)
        embedvar.add_field(name="Humidity:", value=f'{humidity} %', inline=True)
        embedvar.add_field(name="Pressure:", value=f'{pressure} hPa', inline=True)
        embedvar.add_field(name="Time from measurement:", value=f'{last_data_age} {last_data_age_units} ', inline=False)
        await ctx.send(embed=embedvar)


def setup(client):
    client.add_cog(Temperature(client))
