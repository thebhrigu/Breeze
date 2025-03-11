import discord 
from discord import ApplicationContext, Option
from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="purge",
        description="Delete a specified number of messages from the channel"
    )

    @commands.has_permissions(manage_messages=True)
    async def purge(
        self,
        ctx: ApplicationContext,
        amount: Option(int, "Number of messages to delete", required=True)
    ):
        if amount <= 0:
            await ctx.repond("Please specify a positive number of messages to delete.", ephemeral=True)
            return

        deleted = await ctx.channel.purge(limit=amount)
        await ctx.respond(f"Deleted {len(deleted)} message(s).", ephemeral=True)

def setup(bot):
    bot.add_cog(Purge(bot))