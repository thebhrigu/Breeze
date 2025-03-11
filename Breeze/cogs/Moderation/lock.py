import discord
from discord import ApplicationContext, Option
from discord.ext import commands

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="lock",
        description="Lock a channel to prevent members from sending messages"
    )
    @commands.has_permissions(manage_channels=True)
    async def lock(
        self,
        ctx: ApplicationContext,
        channel: Option(discord.TextChannel, "Select the channel to lock", required=True)
    ):
        if not ctx.author.guild_permissions.manage_channels:
            await ctx.respond("You do not have permissions to use this command", ephemeral=True)
            return

        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond(f"Channel {channel.mention} is now locked.", ephemeral=True)

def setup(bot):
    bot.add_cog(Lock(bot))