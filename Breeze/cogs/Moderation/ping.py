import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="ping", description="Check the bot's latency")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.respond(f"Pong! 🎾 Latency is {latency}ms")

def setup(bot):
    bot.add_cog(Ping(bot))