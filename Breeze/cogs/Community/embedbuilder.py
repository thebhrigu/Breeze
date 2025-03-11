import discord
from discord.ext import commands
from discord.commands import slash_command

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Create an Embed")
    @discord.default_permissions(administrator=True)
    @discord.guild_only()
    async def embed(self, ctx):
        if ctx.author.guild_permissions.administrator:
            modal = Modal(bot=self.bot, title="Create an Embed")
            await ctx.send_modal(modal)
        else:
            await ctx.response.send_message("Error: You do not have permission to execute this command", ephemeral=True)

def setup(bot):
    bot.add_cog(Embed(bot))

class Modal(discord.ui.Modal):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        super().__init__(
            discord.ui.InputText(label="Embed Title", placeholder="Enter Title"),
            discord.ui.InputText(
                label="Embed Description",
                placeholder="Enter text",
                style=discord.InputTextStyle.long,
            ),
            discord.ui.InputText(
                label="Embed Thumbnail",
                placeholder="Enter thumbnail URL (optional)",
                style=discord.InputTextStyle.short,
                required=False
            ),
            discord.ui.InputText(
                label="Embed Image",
                placeholder="Enter Thumbnail URL (optional)",
                style=discord.InputTextStyle.short,
                required=False
            ),
            discord.ui.InputText(
                label="Channel ID",
                placeholder="Enter Channel ID",
                style=discord.InputTextStyle.short,
            ),
            *args,
            **kwargs,
        )

    async def callback(self, interaction):
        embed = discord.Embed(
            title=self.children[0].value,
            description=self.children[1].value,
            color=discord.Color.gold()
        )

        thumbnail_url = self.children[2].value
        image_url = self.children[3].value
        channel_id = int(self.children[4].value)
        channel = self.bot.get_channel(channel_id)

        if thumbnail_url:
            if self.is_valid_url(thumbnail_url):
                embed.set_thumbnail(url=thumbnail_url)
            else:
                await interaction.response.send_message("Invalid thumbnail URL.", ephemeral=True)
                return

        if image_url:
            if self.is_valid_url(image_url):
                embed.set_image(url=image_url)
            else:
                await interaction.response.send_message("Invalid image URL.", ephemeral=True)
                return

        await channel.send(embed=embed)
        await interaction.response.send_message(
            f"Embed Successfully Created and sent to {channel.mention}!",
            ephemeral=True
        )

    def is_valid_url(self, url: str) -> bool:
        # Basic URL validation
        import re
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
            r'localhost|' # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None
