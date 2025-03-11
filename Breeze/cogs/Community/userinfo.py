import discord
from discord.ext import commands
from discord import ApplicationContext, Option

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="userinfo",
        description="Get information about a user",
        options=[
            Option(
                discord.User,
                name="user",
                description="The user whose information you want to see.",
                required=False
            )
        ]
    )

    async def userinfo(self, ctx: ApplicationContext, user: discord.User = None):
        user = user or ctx.author
        embed = discord.Embed(title=f"{user}'s information", color=discord.Color.gold())
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Bot?", value=user.bot, inline=True)
        embed.add_field(name="Created At", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        if isinstance(user, discord.Member):
            embed.add_field(name="Joined At", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(UserInfo(bot))