import discord
import youtube_dl
import asyncio
import os
import pdb
from discord.ext import commands

token = os.environ["brewbot_token"]

#class MyClient(discord.Client):
#    async def on_ready(self):
#        print('Logged on as', self.user)
#
#    async def on_message(self, message):
#        # don't respond to ourselves
#        if message.author == self.user:
#            return

#        if message.content == 'ping':
#            await message.channel.send('pong')




#client = MyClient()
#client.run(token)

# Bot Example

bot = commands.Bot(command_prefix='?')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
        print('Logged on as', bot.user.name)

@bot.command()
async def voice(ctx):
    channel = ctx.author.voice.channel
    voiceClient = await channel.connect()
    player = voiceClient.play(discord.FFmpegPCMAudio('./yas.mp4'))
    url = "https://youtu.be/Q0o8H7oDHB0"
#    youtube_dl.

bot.run(token)


#    while not voiceClient.is_playing():
#        await voiceClient.disconnect()
