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
    async def champrot(self, user : discord.Member):
        """Champion rotation LoL"""

        #Your code will go here
        response = requests.get("https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations")
        await self.bot.say(response.status_code)
    

def setup(bot):
    bot.add_cog(Mycog(bot))