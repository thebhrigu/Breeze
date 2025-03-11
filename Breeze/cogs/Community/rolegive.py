import discord
from discord.ext import commands
from discord import ApplicationContext, Option

class RoleAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="role",
        description="Give a role to the user",
        options=[
            Option(
                discord.User,
                name="user",
                description="The user to give the role",
                required=True
            ),
            Option(
                discord.Role,
                name="role",
                description="The role to give to the user",
                required=True
            )
        ]
    )
    
    async def role_give(self, ctx: ApplicationContext, user: discord.Member, role: discord.Role):
        if not ctx.author.guild_permissions.manage_roles:
            await ctx.respond("You do not have permission to use this command.", ephemeral=True)
            return

        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.respond("I do not have permission to manage roles.", ephemeral=True)
            return

        if ctx.guild.me.top_role <= role:
            await ctx.respond("I cannot assign this role because it is higher than my role.", ephemeral=True)
            return

        await user.add_roles(role, reason=f"Role added by {ctx.author}")
        await ctx.respond(f"Role **{role.name}** given to **{user.display_name}**")

def setup(bot):
    bot.add_cog(RoleAdd(bot))
