import discord
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="serverinfo",
        description="Shows info about the server"
    )

    async def serverinfo(self, ctx: discord.ApplicationContext):
        guild = ctx.guild
        embed = discord.Embed(title=f"{guild.name}'s Information", color=discord.Colour.gold())
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.add_field(name="Server Name", value=guild.name, inline=True)
        embed.add_field(name="Server ID", value=guild.id, inline=True)
        embed.add_field(name="Owner", value=guild.owner, inline=True)
        embed.add_field(name="Member Count", value=guild.member_count, inline=True)
        embed.add_field(name="Text Channels", value=len(guild.text_channels), inline=True)
        embed.add_field(name="Voice Channels", value=len(guild.voice_channels), inline=True)
        embed.add_field(name="Roles", value=len(guild.roles), inline=True)
        embed.add_field(name="Boose Level", value=guild.premium_tier, inline=True)
        embed.add_field(name="Boost Count", value=guild.premium_subscription_count, inline=True)
        embed.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ServerInfo(bot))