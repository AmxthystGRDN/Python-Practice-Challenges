from typing import Optional

from discord import Member
from discord.ext.commands import Bot
from discord.ext.commands.converter import Greedy
from discord.ext.commands.core import bot_has_permissions, has_permissions
from discord.ext.commands.errors import CheckFailure

bot = Bot(command_prefix = "=", description = 'A secondary bot of FRX')

@bot.event
async def on_ready():
    print("FRX Bot is online!")

@bot.command(name = "kick")
@bot_has_permissions(kick_members = True)
@has_permissions(kick_members = True)
async def kick_command(ctx, targets: Greedy[Member], *, reason: Optional[str] = "No reason provided."):
    if not len(targets):
        await ctx.send("One of more required arguments is missing.")

    else:
        for target in targets:
            if (ctx.guild.me.top_role.position > target.top_role.position and not target.guild_permissions.administrator):
                await target.kick(reason = reason)

                await ctx.send("Action complete.")

@kick_command.error
async def kick_command_error(ctx, exc):
    if isinstance(exc, CheckFailure):
        await ctx.send("Insufficient permissions to perform that task.")

bot.run("TOKEN")

# This code is from a main file