import discord
from discord.ext import commands

class Cog_core(commands.Cog): # 當作 最核心的 class 來繼承 免得每次繼承 commands.Cog 都還要打一次下一行的 init
    def __init__(self,bot):
        self.bot=bot
