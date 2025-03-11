import discord
from discord.ext import commands

class BotStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="botstats",
        description="Display the bot statistics"
    )

    async def stats(self, ctx: discord.ApplicationContext):
        total_guilds = len(self.bot.guilds)
        total_users = len(set(self.bot.get_all_members()))
        total_channels = sum(1 for _ in self.bot.get_all_channels())

        embed = discord.Embed(
            title="Bot Stats",
            description="Here are some statistics about the bot",
            color=discord.Color.gold()
        )
        embed.add_field(name="Total Servers", value=total_guilds)
        embed.add_field(name="Total Users", value=total_users)
        embed.add_field(name="Total Channels", value=total_channels)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        view = discord.ui.View()
        support_button = discord.ui.Button(label="Support Server", url="https://discord.gg/YJCgDwFsyK", style=discord.ButtonStyle.link)

        view.add_item(support_button)

        await ctx.respond(embed=embed, view=view)

def setup(bot):
    bot.add_cog(BotStats(bot))