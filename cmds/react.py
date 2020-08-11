import discord
from discord.ext import commands
from cor.classes import Cog_core
import json
import random

with open('setting.json', mode='r', encoding='utf-8') as jFile:
    jdata = json.load(jFile)

class React(Cog_core):
    @commands.command()
    async def 夜雨落(self,ctx): # 當輸入 ~夜雨落 會觸發的
        await ctx.channel.send('上次跟我一起吃毒\n讓我知道他是史上最會開趴之人') 
        pic = discord.File(jdata['Picture']+'1552499367332.jpg')
        await ctx.channel.send(file=pic)

    @commands.command()
    async def react(self,ctx, keyword):
        if keyword == '抱抱':
            await ctx.channel.send('抱抱')
        else:
            await ctx.send('錯誤指令')
    @commands.command()
    async def 抽(self,ctx): # ~抽 可以抽 對 就冰淇淋女孩的那個
        rand = random.choice([0,1,2,3,4,5,6,7,8,9])
        pic = discord.File(jdata['Pic2']+str(rand)+').jpg')
        await ctx.channel.send(file=pic)

def setup(bot): # Cog 用的
    bot.add_cog(React(bot))