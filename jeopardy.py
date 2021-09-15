import discord
import os
import random
from random import shuffle, choice
from discord.ext import commands
from discord.utils import get
import string
import fuzzywuzzy
from fuzzywuzzy import fuzz


"""  

a sort of abstract: a jeopardy discord bot cog, a la protobowl's implementation. 
leaderboard will be based on compounded money earned per question
questions will be read at random from a csv file. to avoid a large number of dead 
questions,  measures have been taken so that all questions come from the earliest showing 
within the 21st century (1/3/00 to 1/27/12). context for the question will be provided 
in the form of the date of the question. 

"""

class Jeopardy(commands.Cog):

    """ bot initialization """
    def __init__(self, bot):
        self.bot = bot 
        self.channel = None
        self.running = False
        
        self.questions = []
        self.asked = []

        self.players = {}
        self.scores = {}
        self.ready = 0
        self.first = None

    def nextRound(self):
        self.round+=1
    
    def numPlayers(self):
        return len(self.players)

    def gameOver(self):
        self.running = False

    @commands.command(aliases = ['j'])
    async def jeopardy(self, ctx):
        if self.running:
            await ctx.send('A Jeopardy! game is currently in process.')
        else:
            self.running = True

            self.server = ctx.guild
            self.channel = ctx.channel
            
            embed = discord.Embed(color=0x060CE9)
            embed.set_author(name="Welcome to Jeopardy!", icon_url="https://pbs.twimg.com/profile_images/1437160590623985665/vtYqQghe_400x400.jpg")
            embed.add_field(name="Rules", value="Type your answer in the form of a question", inline=False)
            
        


    """ randomizer """
    filesize = os.path.getsize('/Users/joeyquismorio/namethattunebot/cogs/jeopardy.tsv')
    offset = random.randrange(filesize)

    f = open('/Users/joeyquismorio/namethattunebot/cogs/jeopardy.tsv')
    f.seek(offset)
    f.readline()
    q = f.readline()
    categories = q.split("\t")
    value = categories[0]
    double = categories[1]
    category = categories[2]
    comments = categories[3]
    question = categories[4]
    answer = categories[5]
    date = categories[6]

    if len(q) == 0:
        f.seek(0)
        q = f.readline()
        categories = q.split("\t")
        value = categories[0]
        double = categories[1]
        category = categories[2]
        comments = categories[3]
        question = categories[4]
        answer = categories[5]
        date = categories[6]


