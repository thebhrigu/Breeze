import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks

class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_activity.start()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.update_activity()
    
    @tasks.loop(seconds=10)
    async def update_activity(self):
        if self.bot.is_ready():
            activity1 = discord.CustomActivity(name="Stay active buddy!")
            activity2 = discord.CustomActivity(name="Enjoy your stay here.")
            activity3 = discord.CustomActivity(name="Wanna drink some coffee?")
            activity4 = discord.CustomActivity(name="Watching Citadel.")
            await self.bot.change_presence(activity=activity1)
            await asyncio.sleep(2)
            await self.bot.change_presence(activity=activity2)
            await asyncio.sleep(2)
            await self.bot.change_presence(activity=activity3)
            await asyncio.sleep(2)
            await self.bot.change_presence(activity=activity4)
            await asyncio.sleep(2)

def setup(bot):
    bot.add_cog(Activity(bot))
