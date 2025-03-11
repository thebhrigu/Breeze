import discord
from discord import ApplicationContext, Option
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(
        name="avatar",
        description="Get the avatar of an user",
        option=[
            Option(
                discord.User,
                name="user",
                description="The user whose avatar you want to see",
                required=False
            )
        ]
    )

    async def avatar(self, ctx: ApplicationContext, user: discord.User = None):
        user = user or ctx.author
        embed = discord.Embed(title=f"{user}'s Avatar", color=discord.Color.gold())
        embed.set_image(url=user.avatar.url)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))