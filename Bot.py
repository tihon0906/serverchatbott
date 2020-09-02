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
    async def coin( self, ctx, userchoice ):
        choices = [ 'Орел', 'Решка', 'Монетка упала ребром' ]
        color = discord.Color.green()
        choiced = random.choice(choices)
        if userchoice == 'Орел' or userchoice == 'орёл' or userchoice == 'орел' or userchoice == 'Орёл':
            if choiced == userchoice:
                embed = discord.Embed(title = '🥇 Подбрасывание:', description = f'💰 `Вы выбрали:` **{userchoice}**, когда ✅ `выпало:` **Орёл!**\n\n💬 `Итог:` **Вы выиграли!**', colour = color)
                embed.set_author( name = ctx.author, icon_url = ctx.author.avatar_url )
                embed.set_footer( text = f'{self.client.user.name} © 2020 | Все права под защитой', icon_url = self.client.user.avatar_url )
                await ctx.send(embed = embed)
                print(f'[LOGS </>] [+] {ctx.author} used {prefix}coin command!')
            elif choiced == 'Монетка упала ребром':
                embed = discord.Embed(title = '🥇 Подбрасывание:', description = f'💰 `Вы выбрали:` **{userchoice}**, когда ✅ `выпало:` **Решка!**\n\n💬 `Итог:` **Проиграли :c**', colour = color)
                embed.set_author( name = ctx.author, icon_url = ctx.author.avatar_url )
                embed.set_footer( text = f'{self.client.user.name} © 2020 | Все права под защитой', icon_url = self.client.user.avatar_url )
                await ctx.send(embed = embed)
                print(f'[LOGS </>] [+] {ctx.author} used {prefix}coin command!')
            else:
                embed = discord.Embed(title = '🥇 Подбрасывание:', description = '❌ **Упс... Похоже, что можетка упала ребром!**', colour = color)
                embed.set_author( name = ctx.author, icon_url = ctx.author.avatar_url )
                embed.set_footer( text = f'{self.client.user.name} © 2020 | Все права под защитой', icon_url = self.client.user.avatar_url )
                await ctx.send(embed = embed)
                print(f'[LOGS </>] [+] {ctx.author} used {prefix}coin command!')
        elif userchoice == 'решка' or userchoice =='Решка':
            if choiced == 'Орел':
                embed = discord.Embed(title = '🥇 Подбрасывание:', description = f'💰 `Вы выбрали:` **{userchoice}**, когда ✅ `выпало:` **Орел!**\n\n💬 `Итог:` **Проиграли :c**', colour = color)
                embed.set_author( name = ctx.author, icon_url = ctx.author.avatar_url )
                embed.set_footer( text = f'{self.client.user.name} © 2020 | Все права под защитой', icon_url = self.client.user.avatar_url )
                await ctx.send(embed = embed)
                print(f'[LOGS </>] [+] {ctx.author} used {prefix}coin command!')
            elif choiced == 'Решка':
                embed = discord.Embed(title = '🥇 Подбрасывание:', description = f'💰 `Вы выбрали:` **{userchoice}**, когда ✅ `выпало:` **Решка!**\n\n💬 `Итог:` **Вы выиграли!**', colour = color)
                embed.set_author( name = ctx.author, icon_url = ctx.author.avatar_url )
                embed.set_footer( text = f'{self.client.user.name} © 2020 | Все права под защитой', icon_url = self.client.user.avatar_url )
                await ctx.send(embed = embed)
                print(f'[LOGS </>] [+] {ctx.author} used {prefix}coin command!')
            else:
                embed = discord.Embed(title = '🥇 Подбрасывание:', description = '❌ **Упс... Похоже, что можетка упала ребром!**', colour = discord.Color.orange())
                embed.set_author( name = ctx.author, icon_url = ctx.author.avatar_url )
                embed.set_footer( text = f'{self.client.user.name} © 2020 | Все права под защитой', icon_url = self.client.user.avatar_url )
                await ctx.send(embed = embed)
                print(f'[LOGS </>] [+] {ctx.author} used {prefix}coin command!')
        else:
            embed = discord.Embed( title = '❌ Упс... Произошла ошибка...', description = f'📃 `Неверные аргументы!` | **Испосльзуйте** `{ prefix }coin (sign (Орел или Решка))!`', colour = discord.Color.red() )
            embed.set_author( name = ctx.author, icon_url = ctx.author.avatar_url )
            embed.set_footer(text = f'{self.client.user.name} © 2020 | Все права под защитой', icon_url = self.client.user.avatar_url)
            await ctx.send( embed = embed )
            print( f'[LOGS </>] [-] { ctx.author } doesnt use arguments to use { prefix }coin command!' )

    #0xff0000
    #15158332



token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
