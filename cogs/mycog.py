import discord
import requests
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

    @commands.command()
    async def punch(self, user : discord.Member):
        """I will punch anyone! >.<"""

        #Your code will go here
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

    @commands.command()
    async def champrot(self):
        """Champion rotation LoL"""

        #Your code will go here
        response = requests.get("https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations", headers={"X-Riot-Token": "RGAPI-023389fb-6947-4684-ab86-0259ae9cbaf6"})
        await self.bot.say(response.content)
    
    @commands.command()
    async def lol(self, naam):
        """Champion rotation LoL"""

        #Your code will go here
        response = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + naam , headers={"X-Riot-Token": "RGAPI-023389fb-6947-4684-ab86-0259ae9cbaf6"})
        await self.bot.say(response.content)
    

def setup(bot):
    bot.add_cog(Mycog(bot))