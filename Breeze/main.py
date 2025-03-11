import discord
import os
import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
welcome_channel = 1340400477719760916
log_channel = 1340525133021974530

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond("⌛ This command is currently on cooldown! Please wait a bit before trying again.", ephemeral=True)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.respond("🔒 You do not have the required permissions to run this command!", ephemeral=True)
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.respond("🔒 I do not have enough permissions to do this!", ephemeral=True)
    elif isinstance(error, commands.NSFWChannelRequired):
        await ctx.respond("❌ This command can only be used in an NSFW channel!", ephemeral=True)
    else:
        await ctx.respond("🙄 An unexpected error occurred while processing the command.", ephemeral=True)
    raise error

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Watching Citadel..."))
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="info", description="A little bit about me")
async def info(ctx: discord.ApplicationContext):
    await ctx.respond("I am Breeze! The Guard 🛡 of the Citadel Discord Server. I perform administrative tasks of this server.")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel)
    welcome_message = f"Hi **{member.mention}**, Welcome to the **Citadel**! 🏰 \nWe're thrilled to have you as a part of our stronghold of friendship and fun. Dive right in and make yourself at home!"
    role_member = discord.utils.get(member.guild.roles, name='Member')
    await member.add_roles(role_member)
    await channel.send(welcome_message)

@bot.event
async def on_message_delete(message):
    del_message = bot.get_channel(log_channel)
    embed = discord.Embed(
        title=f"{message.author}'s Message was deleted", 
        description=f"Deleted Message: {message.content}\nAuthor: {message.author.mention}\nLocation: {message.channel.mention}", 
        timestamp=datetime.datetime.now(), 
        color=discord.Color.gold()
    )
    await del_message.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
    edit_message = bot.get_channel(log_channel)
    embed = discord.Embed(
        title=f"{before.author} Edited their message", 
        description=f"Before: {before.content}\nAfter: {after.content}\nAuthor: {before.author.mention}\nLocation: {before.channel.mention}", 
        timestamp=datetime.datetime.now(), 
        color=discord.Color.gold()
    )
    await edit_message.send(embed=embed)

def load_extensions(bot, directory="cogs"):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py"):
                ext_path = os.path.join(root, filename)
                module_name = ext_path.replace(os.sep, ".")[:-3]
                bot.load_extension(module_name)
                print(f"Loaded {module_name}")

load_extensions(bot)
bot.run(os.getenv('token'))
