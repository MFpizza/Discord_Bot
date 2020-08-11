import discord
import json
import random
from discord.ext import commands #算是一種導入 class 或 function 的方法
import os

with open('setting.json', mode='r', encoding='utf-8') as jFile: #用來開啟 json 檔案用的
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='~') #輸入指令前必須先輸入 ~ 字元

@bot.event
async def on_ready(): # 當 bot 開機後
    print(">> Bot is online <<")


@bot.command()
async def load(ctx,extension): #  因為有 Cog 所以可以 ~load / unload / reload  各 py 用
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

for filename in os.listdir('./cmds'): # 用來把 cmds 資料夾裡面的所有 py 檔 輸入進來
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__': #進入點? 還不太懂 python
    bot.run(jdata['TOKEN'])     