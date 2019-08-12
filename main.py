import asyncio
import os

import discord
import youtube_dl
#import redis
from discord.ext import commands

token = os.environ["brewbot_token"]
bot = commands.Bot(command_prefix='?')
initial_extensions = ['cogs.sanitization']

#if __name__ == '__main__':
#    for extension in initial_extensions:
#        bot.load_extension(extension)

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
    wait(20000)
#    player = voiceClient.play(discord.FFmpegPCMAudio('./yas.mp4'))
#    voiceClient.play(discord.FFmpegPCMAudio('spikes.webm'))
#
#    queue = ['https://youtu.be/Q0o8H7oDHB0']
#    ydl_opts = {'outtmpl':'-'}
#    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        player = voiceClient.play(
#            discord.FFmpegPCMAudio(
#                ydl.download(queue), pipe=True
#            )
#        )

#@bot.event
#async def on_message(message):
#    print("this is the first instance: "+str(message.author.id))



bot.run(token)
