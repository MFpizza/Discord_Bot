import discord
import json
import random
from discord.ext import commands

import os

with open('setting.json', mode='r', encoding='utf-8') as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.channel.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.channel.send(f'unLoaded {extension} done.')
    
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.channel.send(f'reLoaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(jdata['TOKEN'])     