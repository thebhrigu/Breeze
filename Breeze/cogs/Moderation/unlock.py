import discord
from discord import ApplicationContext, Option
from discord.ext import commands

class Unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="unlock",
        description="Unlock a locked Channel"
    )
    @commands.has_permissions(manage_channels=True)
    async def unlock(
        self,
        ctx: ApplicationContext,
        channel: Option(discord.TextChannel, "Select a channel to unlock", required=True)
    ):
        if not ctx.author.guild_permissions.manage_channels:
            await ctx.respond("You do not have permissions to use this command.", ephemeral=True)
            return

        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond(f"Channel {channel.mention} is now unlocked.", ephemeral=True)

def setup(bot):
    bot.add_cog(Unlock(bot))