import discord
from discord.ext import commands
import os
import json

bot = commands.Bot(command_prefix="<Prefix>")

#@bot.command makes a command.
@bot.command
#async def <NAme of the command>
#ctx = Context
async def Hello(ctx):
#await ctx.send("The bots response")
  await ctx.send("hi there")
  
#Full Command:
@bot.command
async def Hello(ctx):
  await ctx.send("hi there")
