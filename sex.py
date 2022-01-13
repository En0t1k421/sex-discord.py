import discord
from discord.ext import commands, tasks
import asyncio
import datetime


@client.command()
async def sex(ctx, member: discord.Member = None):
    if member == ctx.author:
        return await ctx.send(embed = discord.Embed(description = 'Ты не можешь заняться кексом с собой!'))
 
    if member == None:
        return await ctx.send(embed = discord.Embed(description = 'Обязательно укажи пользователя!'))
 
    sex1 = ['https://i.gifer.com/Q0Cn.gif']
 
    embed1 = discord.Embed(description = f'{ctx.author.mention} предложил заняться кексом {member.mention}')
    embed1.set_image(url=random.choice(sex1))
 
    check_h = await ctx.send(embed = embed1)
    await check_h.add_reaction('💚')
    await check_h.add_reaction('💔')
    def check(reaction, user):
        return user == member and reaction.emoji in '💚💔:'
 
    try:
        reaction, user = await client.wait_for('reaction_add', check = check, timeout = 30)
    except asyncio.TimeoutError:
        await ctx.send(embed = discord.Embed(description = f'{member.mention} Время вышло.') )
        return
 
    if reaction.emoji == '💚':
 
        sex2 = ['https://i.gifer.com/8Sbz.gif','https://i.gifer.com/8LDU.gif']
 
        embed = discord.Embed(description = f'{member.mention}  занялся кексом с {ctx.author.mention}')
    
        embed.set_image(url=random.choice(sex2))
    
 
        await ctx.send(embed = embed)
        
    if reaction.emoji == '💔':
 
        gif = ['https://i.gifer.com/5bT.gif', 'https://i.gifer.com/6U4H.gif', 'https://i.gifer.com/3DC.gif']
        krik = [f'{member.mention} послал  {ctx.author.mention}, он такой страшный..']
 
        embed = discord.Embed(description = random.choice(krik))
 
        embed.set_image(url = random.choice(gif))
 
        await ctx.send(embed = embed)


"""BY EN0T1K421"""
