import discord
from discord.ext import commands, tasks

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send('Kicked User!')
