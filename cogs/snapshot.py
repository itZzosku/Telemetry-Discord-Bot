import discord
import requests
import os
from discord.ext import commands


class Snapshot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['snap'])
    async def snapshot(self, ctx):
        url = 'http://192.168.1.5:4080/webcam/?action=snapshot'
        r = requests.get(url, allow_redirects=True)
        open('snapshot.jpg', 'wb').write(r.content)
        file = discord.File("/home/pi/Telemetry-Discord-Bot/snapshot.jpg", filename="snapshot.jpg")
        await ctx.send(file=file)
        os.remove("snapshot.jpg")


def setup(client):
    client.add_cog(Snapshot(client))
