import discord
from  discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
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
    
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx,member:discord.Member,reason):
    channel = Bot.get_channel(748663806883921931)
    muterole = discord.utils.get(ctx.guild.roles,id=748656736013123724)
    emb = discord.Embed(title="Анмут",color=0xff0000)
    emb.add_field(name='Пользователь',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Замученый',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await channel.send(embed = emb)
    await member.remove_roles(muterole)
    
@Bot.command()
async def dfg(ctx, arg):
    import random
    a = random.randint(0, 2)
    print(a)
    if arg == "камень" and a == 0:
        emb = discord.Embed(title = "ВЫПАЛ КАМЕНЬ", description = "вы выбрали камень. У бота выпал камень!", colour = 0xF0E68C)
        emb.add_field(name = "ИТОГ", value = "У вас ничья!")
        await ctx.send(embed = emb)
    if arg == "камень" and a == 1:
        emb = discord.Embed(title = "ВЫПАЛИ НОЖНИЦЫ", description = "вы выбрали камень. У бота выпали ножницы!", colour = 0xD3D3D3)
        emb.add_field(name = "ИТОГ", value = "Вы выйграли!")
        await ctx.send(embed = emb)
    if arg == "камень" and a == 2:
        emb = discord.Embed(title = "ВЫПАЛА БУМАГА", description = "вы выбрали камень. У бота выпала бумага!", colour = 0xFFD700)
        emb.add_field(name = "ИТОГ", value = "Вы проиграли!")
        await ctx.send(embed = emb)
    if arg == "ножницы" and a == 0:
        emb = discord.Embed(title = "ВЫПАЛ КАМЕНЬ", description = "вы выбрали ножницы. У бота выпал камень!", colour = 0xF0E68C)
        emb.add_field(name = "ИТОГ", value = "Вы проиграли!")
        await ctx.send(embed = emb)
    if arg == "ножницы" and a == 1:
        emb = discord.Embed(title = "ВЫПАЛИ НОЖНИЦЫ", description = "вы выбрали ножницы. У бота выпали ножницы!", colour = 0xD3D3D3)
        emb.add_field(name = "ИТОГ", value = "У вас ничья!")
        await ctx.send(embed = emb)
    if arg == "ножницы" and a == 2:
        emb = discord.Embed(title = "ВЫПАЛА БУМАГА", description = "вы выбрали ножницы. У бота выпала бумага!", colour = 0xFFD700)
        emb.add_field(name = "ИТОГ", value = "Вы выйграли!")
        await ctx.send(embed = emb)
    if arg == "бумага" and a == 0:
        emb = discord.Embed(title = "ВЫПАЛ КАМЕНЬ", description = "вы выбрали бумагу. У бота выпал камень!", colour = 0xF0E68C)
        emb.add_field(name = "ИТОГ", value = "Вы выйграли!")
        await ctx.send(embed = emb)
    if arg == "бумага" and a == 1:
        emb = discord.Embed(title = "ВЫПАЛИ НОЖНИЦЫ", description = "вы выбрали бумагу. У бота выпали ножницы!", colour = 0xD3D3D3)
        emb.add_field(name = "ИТОГ", value = "Вы проиграли!")
        await ctx.send(embed = emb)
    if arg == "бумага" and a == 2:
        emb = discord.Embed(title = "ВЫПАЛА БУМАГА", description = "вы выбрали бумагу. У бота выпала бумага!", colour = 0xFFD700)
        emb.add_field(name = "ИТОГ", value = "У вас ничья!")
        await ctx.send(embed = emb)

@Bot.command()
async def orr(ctx, arg):
    import random
    a = random.randint(0, 30)
    print(a)
    if arg == "help":
        await ctx.channel.purge(limit = 1)
        emb = discord.Embed(title = "солнце или луна?", description = "суть игры: выпадет или солнце🌕, или луна🌑.", colour = 0x00FF7F)
        emb.add_field(name = "#orr flip", value = 'подбрасывает "монетку"')
        emb.add_field(name = "#orr help", value = "показывает эту команду")
        await ctx.send(embed = emb)
    if arg == "flip":
        await ctx.channel.purge(limit = 1)
        emb = discord.Embed(title = "ПОДБРАСЫВАНИЕ🌗", description = f"{ctx.message.author.mention} подбросил монету", colour = 0xEEDD82)
        emb.add_field(name = "ПОДБРАСЫВАНИЕ", value = "идёт подбрасывание...")
        emb.set_image(url = "https://acegif.com/wp-content/gifs/coin-flip-16.gif")
        await ctx.send(embed = emb)
        b = random.randint(0, 10)
        time = 3
        print(b)
        await asyncio.sleep(time)
        if b > 0:
            if a > 20:
                emb = discord.Embed(title = "ВЫПАЛА ЛУНА🌑", description = f"выпала луна!", colour = 0xD3D3D3)
                await ctx.send(embed = emb)
            elif a < 20:
                emb = discord.Embed(title = "ВЫПАЛО СОЛНЦЕ🌕", description = f"выпало солнце!", colour = 0xFFD700)
                await ctx.send(embed = emb)
            if a == 1:
                await ctx.channel.purge(limit = 1)
                emb = discord.Embed(title = "МОНЕТА ВСТАЛА НА РЕБРО", description = f"монета {ctx.message.author.mention} встала на ребро!", colour = 0xEE82EE)
                await ctx.send(embed = emb)
        elif b == 0:
            emb = discord.Embed(title = "МОНЕТА УПАЛА", description = f"{ctx.message.author.mention} не успел поймать монету, и она упала на пол", colour = 0xCD5C5C)
            await ctx.send(embed = emb)
            
@Bot.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount : int):
    time = 1.30
    await ctx.channel.purge(limit = amount + 1)
    await ctx.send(f"удалено {amount} сообщений")
    await asyncio.sleep(time)
    await ctx.channel.purge(limit = 1)


            
@Bot.event
async def on_ready():
    print( 'BOT connected' )

    await Bot.change_presence (status = discord.Status.online, activity = discord.Game( '𝐌𝐢𝐧𝐞𝐖𝐨𝐖𝐂𝐫𝐚𝐟𝐭' ) )

    #0xff0000
    #15158332



token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
