import discord
import json
import random
from discord.ext import commands
from cor.classes import Cog_core

with open('setting.json', mode='r', encoding='utf-8') as jFile:
    jdata = json.load(jFile)


class Event(Cog_core):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(690824514325708840)
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(690824514325708840)
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword=['pie','pen','abc']
        if msg.content == 'apple' and msg.author != self.bot.user:
            await msg.channel.send('hi')
            print(msg)
        elif msg.content == '夜雨落':
            await msg.channel.send('可憐哪')
        elif msg.content in keyword and msg.author!=self.bot.user:
            await msg.channel.send(msg.content)


def setup(bot):
    bot.add_cog(Event(bot))
