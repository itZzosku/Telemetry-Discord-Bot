import discord
import os
import requests
from discord.ext import commands


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Loaded Cog")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Unloaded Cog")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Reloaded Cog")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[0:-3]}')

client.run(token)
