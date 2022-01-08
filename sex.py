import discord
from discord.ext import commands, tasks
import asyncio
import datetime


@client.command (pass_context = True)
@commands.has_permissions(ban_members = True)
async def ban (ctx, member: discord.Member, *, reason):
    channel = client.get_channel(817829676772360192)
    await ctx.channel.purge(limit = 1)
    lol = discord.Embed(title = 'Пользователь забанен!', color = 0xc25151 )
    lol.add_field(name = 'Модератор / админ:', value = ctx.message.author.mention, inline = False)
    lol.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
    lol.add_field(name= 'Причина:', value = reason, inline = False)
    lol.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/813129913409601550/817735685841747978/08e7aac43809d99b.png')
    lol.set_footer (text = f'Вызвано: {ctx.message.author}', icon_url = ctx.message.author.avatar_url)
    await channel.send(embed = lol)
    await member.send(f'Вы забанены по причине "{reason}"!')
    await member.ban( reason = reason)






@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} получил разбан")
    return





@ban.error
async def ban_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            emb = discord.Embed(title = f"Ошибка!", description = f'Пользователь не найден.', colour = 0xce0000)
            emb.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = emb)
        else:
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(embed = discord.Embed(title = f"❌ в доступе отказано!", description = f"{ctx.author.name}, у вас нету нужных прав!" , color = ERROR))
            else:
                if isinstance(error, commands.MissingRequiredArgument):
                    await ctx.send(embed = discord.Embed(title = f"Ошибка!", description = f" {ctx.author.name}, укажите аргумент!" , color = ERROR ))



"""BY EN0T1K421"""