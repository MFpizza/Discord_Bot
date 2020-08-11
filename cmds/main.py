import discord
from discord.ext import commands
from cor.classes import Cog_core

class Main(Cog_core):
    def __init__(self,bot): #好像是類似 C++ 的 constructer
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.channel.send(F'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hey(self,ctx): #沒啥
        await ctx.channel.send('yo')

    @commands.command()
    async def sayd(self, ctx, *, msg): # *後面類似把所有argv[i]直接當成 msg 類似把自己說的話讓機器人說出來
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self,ctx,num: int): # ~clean 10 : 清除 10 則這個頻道的文字訊息
        await ctx.channel.purge(limit = num + 1)

def setup(bot):
    bot.add_cog(Main(bot))