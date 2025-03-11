import discord
from discord.ext import commands
from discord import ApplicationContext, Option

class RoleAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="role-all",
        description="Assign a role to all members in the server"
    )

    async def role_all(self, ctx: ApplicationContext, role: Option(discord.Role, "The role to assign to all members")):
        if not ctx.author.guild_permissions.manage_roles:
            await ctx.respond("You do not have permission to user this command.", ephemeral=True)
            return

        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.respond("I do not have permission to manage roles", ephemeral=True)
            return

        if ctx.guild.me.top_role <= role:
            await ctx.respond("I cannot assign this role because it is higher than my role", ephemeral=True)
            return

        await ctx.respond("Assining the role to all members...")
        members = await ctx.guild.fetch_members().flatten()
        for member in members:
            try:
                if not member.bot:
                    await member.add_roles(role)
            except discord.Forbidden:
                await ctx.send(f"Failed to assign role ${member.display_name} due to permissions.")
            except discord.HTTPException as e:
                await ctx.send(f"Failed to assign role! {e}")

        await ctx.send(f"The role **{role.name}** has been assigned to all members.")

    @discord.slash_command(
        name="role-all-remove",
        description="Remove a role from all members in the server"
    )
    async def role_all_remove(self, ctx: ApplicationContext, role: Option(discord.Role, "The role to remove from all members")): 
        if not ctx.author.guild_permissions.manage_roles:
            await ctx.respond("You do not have permission", ephemeral=True)
            return
        
        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.respond("I do not have permissions to manage roles", ephemeral=True)
            return

        if ctx.guild.me.top_role <= role:
            await ctx.respond("I cannot assign role because this role is higher than mine.", ephemeral=True)
            return

        await ctx.respond("Removing the role from all members...")
        members = await ctx.guild.fetch_members().flatten()
        for member in members:
            try:
                if not member.bot:
                    await member.remove_roles(role)
            except discord.Forbidden:
                await ctx.send(f"Failed to remove role")
            except discord.HTTPException as e:
                await ctx.send(f"Failed {e}")

        await ctx.send(f"The role **{role.name}** has been removed from all members.")
    
def setup(bot):
    bot.add_cog(RoleAll(bot))
