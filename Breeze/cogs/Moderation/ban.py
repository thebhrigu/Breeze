import discord
from discord.ext import commands

class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="ban",
        description="Ban a member from the server"
    )

    async def Ban(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str = None):
        if not ctx.author.guild_permissions.ban_members:
            await ctx.respond("You do not have permissions to use this command.", ephemeral=True)        
            return
        try:
            await member.ban(reason=reason)
            await ctx.respond(f"Successfully banned **{member}** from the server.")
        except discord.Forbidden:
            await ctx.respond(f"I do not have permission to ban this member", ephemeral=True)
        except discord.HTTPException as e:
            await ctx.respond(f"Failed to ban {member}. Error: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(Ban(bot))