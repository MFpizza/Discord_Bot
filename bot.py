import discord
import json
from discord.ext import commands

with open('setting.json', mode='r', encoding='utf-8') as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(690824514325708840)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(690824514325708840)
    await channel.send(f'{member} leave!')

@bot.command()
async def speak(ctx):
    await ctx.channel.send('吳宗翰傻逼')

@bot.command()
async def MeowMeow(ctx):
    await ctx.channel.send('整天打Valorant是打爽沒?')

@bot.command()
async def 吳宗翰(ctx):
    await ctx.channel.send('這人一定是傻逼')

@bot.command()
async def 膝蓋(ctx):
    await ctx.channel.send('你沒有妹妹')

@bot.command()
async def 夜雨落(ctx):
    await ctx.channel.send('上次跟我一起吃毒\n讓我知道他是史上最會開趴之人')
    pic = discord.File(jdata['Picture']+'1552499367332.jpg')
    await ctx.channel.send(file=pic)

@bot.command()
async def all(ctx):
    await ctx.channel.send('我說在座的各位都是垃圾')
    pic = discord.File(jdata['Picture']+'maxresdefault.jpg')
    await ctx.channel.send(file=pic)

bot.run(jdata['TOKEN'])