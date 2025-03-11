import discord
from discord.ext import commands
from discord.commands import slash_command, option

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="unban",
        description="Unban a member from the server"
    )
    @discord.default_permissions(ban_members=True)
    @option(
        name="user_id",
        description="The user ID of the member to unban",
        type=str,
        required=True
    )
    @option(
        name="reason",
        description="The reason for unbanning the member",
        type=str,
        required=False
    )
    async def unban_(self, ctx: discord.ApplicationContext, user_id: str, reason: str = None):
        if not ctx.author.guild_permissions.ban_members:
            await ctx.respond("You do not have permissions to use this command.", ephemeral=True)
            return
        try:
            user_id = int(user_id)
            user = await self.bot.fetch_user(user_id)
            await ctx.guild.unban(user)
            await ctx.respond(f"Successfully unbanned **{str(user)}** from the server.")
        except discord.Forbidden:
            await ctx.respond(f"I do not have permissions to unban this member.", ephemeral=True)
        except discord.HTTPException as e:
            await ctx.respond(f"Failed to unban {str(user)}. Error: {e}", ephemeral=True)
        except ValueError:
            await ctx.respond(f"Invalid User ID provided.", ephemeral=True)
    
def setup(bot):
    bot.add_cog(Unban(bot))