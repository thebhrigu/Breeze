import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="kick",
        description="Kick a member from the server"
    )
    async def kick(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str = None):
        if not ctx.author.guild_permissions.kick_members:
            await ctx.respond("You do not have permissions to use this command.", ephemeral=True)
            return
        try:
            await member.kick(reason=reason)
            await ctx.respond(f"Successfully kicked **{member}** from the server.")
        except discord.Forbidden:
            await ctx.respond(f"I dont have permissions to kick this member.", ephemeral=True)
        except discord.HTTPException as e:
            await ctx.respond(f"Failed to kick {member}. Error: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(Kick(bot))
