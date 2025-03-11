import discord
from discord.ext import commands

class EnlargeEmoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="enlarge",
        description="Get a larger version of a custom emoji",
        options=[
            discord.Option(
                str,
                name="emoji",
                description="The custom emoji to enlarge",
                required=True
            )
        ]
    )

    async def enlarge(self, ctx: discord.ApplicationContext, emoji: str):
        emoji_id = None
        if emoji.startswith("<:") and emoji.endswith(">"):
            name_id = emoji.split(":")[2]
            emoji_id = name_id[:-1]

        if emoji_id:
            try:
                emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.png"
                embed = discord.Embed(title="Enlarge Emoji", color=discord.Color.gold())
                embed.set_image(url=emoji_url)
                await ctx.respond(embed=embed)
            except Exception as e:
                await ctx.respond(f"An error occured: {e}", ephemeral=True)
        else:
            await ctx.respond("Invalid emoji provided.", ephemeral=True)

def setup(bot):
    bot.add_cog(EnlargeEmoji(bot))