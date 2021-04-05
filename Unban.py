import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="<Prefix>")

@bot.command(description="Unbans ppl who have been banned")
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member: discord.Member):
    await ctx.guild.unban(member)
