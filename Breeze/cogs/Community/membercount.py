import discord
from discord.ext import commands
from discord import ApplicationContext

class MemberCount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="membercount",
        description="Get detailed member count of the server"
    )
    async def membercount(self, ctx: ApplicationContext):
        guild = ctx.guild
        if guild is None:
            await ctx.respond("This command is only be used in a server", ephemeral=True)
            return

        total_members = guild.member_count
        bot_count = sum(1 for member in guild.members if member.bot)
        user_count = total_members - bot_count

        embed = discord.Embed(
            title="Server Member Count",
            color=discord.Color.gold()
        )
        embed.add_field(name="Total Members", value=total_members, inline=False)
        embed.add_field(name="Users", value=user_count, inline=True)
        embed.add_field(name="Bots", value=bot_count, inline=True)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else discord.Embed.Empty)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(MemberCount(bot))
