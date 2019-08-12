import discord
from discord.ext import commands

class SanitizationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.Cog.listener()
    async def on_message(message):
        print("this is the second instance: "+ str(message.author.id))

def setup(bot):
    bot.add_cog(SanitizationCog(bot))
