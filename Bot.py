import discord
from  discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
#0x4c12f5
Bot = commands.Bot(command_prefix="!")


@Bot.command()
async def say(ctx,arg):
    await ctx.send(arg)

@Bot.command()
async def info(ctx,member:discord.Member):
    emb = discord.Embed(title='Информация о пользователе',color=0xff0000)
    emb.add_field(name="Когда присоединился:",value=member.joined_at,inline=False)
    emb.add_field(name='Никнейм:',value=member.display_name,inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx,member:discord.Member,time:int,reason):
    channel = Bot.get_channel(748663806883921931)
    muterole = discord.utils.get(ctx.guild.roles,id=748656736013123724)
    emb = discord.Embed(title="Мут",color=0xff0000)
    emb.add_field(name='Пользователь',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.add_field(name="Время",value=time,inline=False)
    await member.add_roles(muterole)
    await channel.send(embed = emb)
    await asyncio.sleep(time * 60)
    await member.remove_roles(muterole)

    #0xff0000
    #15158332



token = os.environ.get('BOT_TOKEN')