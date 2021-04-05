import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="<Prefix>")

@bot.command(description="bans a user with specific reason (only admins)") #ban
@commands.has_permissions(administrator=True)
async def ban (ctx, member:discord.User=None, reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot ban yourself!""") 
    else:
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        print(member)
        print(reason)
        await ctx.channel.send(f"{member} is banned!")
 except:
    await ctx.send(f"Error banning user {member} (cannot ban owner or bot)")
