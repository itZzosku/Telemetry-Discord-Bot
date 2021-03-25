import discord
import lichess.api
from discord.ext import commands


class Ratings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['rating', 'rate'])
    async def ratings(self, ctx):

        user1 = lichess.api.user('itzzosku')
        blitz_rating1 = (user1['perfs']['blitz']['rating'])
        blitz_games1 = (user1['perfs']['blitz']['games'])
        rapid_rating1 = (user1['perfs']['rapid']['rating'])
        rapid_games1 = (user1['perfs']['rapid']['games'])
        puzzle_rating1 = (user1['perfs']['puzzle']['rating'])
        puzzle_games1 = (user1['perfs']['puzzle']['games'])

        user2 = lichess.api.user('Loctifas')
        blitz_rating2 = (user2['perfs']['blitz']['rating'])
        blitz_games2 = (user2['perfs']['blitz']['games'])
        rapid_rating2 = (user2['perfs']['rapid']['rating'])
        rapid_games2 = (user2['perfs']['rapid']['games'])
        puzzle_rating2 = (user2['perfs']['puzzle']['rating'])
        puzzle_games2 = (user2['perfs']['puzzle']['games'])

        user3 = lichess.api.user('RIPPEROONI')
        blitz_rating3 = (user3['perfs']['blitz']['rating'])
        blitz_games3 = (user3['perfs']['blitz']['games'])
        rapid_rating3 = (user3['perfs']['rapid']['rating'])
        rapid_games3 = (user3['perfs']['rapid']['games'])
        puzzle_rating3 = (user3['perfs']['puzzle']['rating'])
        puzzle_games3 = (user3['perfs']['puzzle']['games'])

        user4 = lichess.api.user('Intoilija')
        blitz_rating4 = (user4['perfs']['blitz']['rating'])
        blitz_games4 = (user4['perfs']['blitz']['games'])
        rapid_rating4 = (user4['perfs']['rapid']['rating'])
        rapid_games4 = (user4['perfs']['rapid']['games'])
        puzzle_rating4 = (user4['perfs']['puzzle']['rating'])
        puzzle_games4 = (user4['perfs']['puzzle']['games'])

        user5 = lichess.api.user('valdote')
        blitz_rating5 = (user5['perfs']['blitz']['rating'])
        blitz_games5 = (user5['perfs']['blitz']['games'])
        rapid_rating5 = (user5['perfs']['rapid']['rating'])
        rapid_games5 = (user5['perfs']['rapid']['games'])
        puzzle_rating5 = (user5['perfs']['puzzle']['rating'])
        puzzle_games5 = (user5['perfs']['puzzle']['games'])

        embedvar = discord.Embed(title="Ratings of the players.", color=0xbc0057)
        embedvar.add_field(name="Ossey", value=f'Blitz Rating: {blitz_rating1} \n Blitz Games: {blitz_games1} \n Rapid Rating: {rapid_rating1} \n Rapid Games: {rapid_games1} \n Puzzle Rating: {puzzle_rating1} \n Puzzles: {puzzle_games1}', inline=True)
        embedvar.add_field(name="JP", value=f'Blitz Rating: {blitz_rating2} \n Blitz Games: {blitz_games2} \n Rapid Rating: {rapid_rating2} \n Rapid Games: {rapid_games2} \n Puzzle Rating: {puzzle_rating2} \n Puzzles: {puzzle_games2}', inline=True)
        embedvar.add_field(name="Rippe", value=f'Blitz Rating: {blitz_rating3} \n Blitz Games: {blitz_games3} \n Rapid Rating: {rapid_rating3} \n Rapid Games: {rapid_games3} \n Puzzle Rating: {puzzle_rating3} \n Puzzles: {puzzle_games3}', inline=True)
        embedvar.add_field(name="Vallu", value=f'Blitz Rating: {blitz_rating4} \n Blitz Games: {blitz_games4} \n Rapid Rating: {rapid_rating4} \n Rapid Games: {rapid_games4} \n Puzzle Rating: {puzzle_rating4} \n Puzzles: {puzzle_games4}', inline=True)
        embedvar.add_field(name="Valte", value=f'Blitz Rating: {blitz_rating5} \n Blitz Games: {blitz_games5} \n Rapid Rating: {rapid_rating5} \n Rapid Games: {rapid_games5} \n Puzzle Rating: {puzzle_rating5} \n Puzzles: {puzzle_games5}', inline=True)
        await ctx.send(embed=embedvar)


def setup(client):
    client.add_cog(Ratings(client))
