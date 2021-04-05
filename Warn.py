import discord
from discord.ext import commands, tasks
import os
import json

bot = commands.Bot(command_prefix="<Prefix>")

@client.command(pass_context = True)
@has_permissions(manage_roles=True, ban_members=True)
async def warn(ctx,user:discord.User,*reason:str):
  if not reason:
    await client.say("Please provide a reason")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)
