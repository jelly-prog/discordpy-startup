from discord.ext import commands

import os
import traceback
import discord

from grouping import MakeTeam

intents = discord.Intents.all()  # デフォルトのIntentsオブジェクトを生成
bot = commands.Bot(command_prefix='/', intents=intents)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
# メンバー数が均等になるチーム分け
@bot.command()
async def team(ctx, specified_num=2):
    make_team = MakeTeam()
    remainder_flag = 'true'
    msg = make_team.make_party_num(ctx, specified_num, remainder_flag)
    await ctx.channel.send(msg)

# メンバー数が均等にはならないチーム分け
@bot.command()
async def team_norem(ctx, specified_num=2):
    make_team = MakeTeam()
    msg = make_team.make_party_num(ctx, specified_num)
    await ctx.channel.send(msg)

# メンバー数を指定してチーム分け
@bot.command()
async def group(ctx, specified_num=1):
    make_team = MakeTeam()
    msg = make_team.make_specified_len(ctx, specified_num)
    await ctx.channel.send(msg)
    
"""テストコマンド"""
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
