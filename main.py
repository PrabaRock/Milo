import discord
from discord.ext import commands
from discord import Bot
import os
import datetime
import json 
import asyncio

# Initial Extensions(cogs)
initial_extensions = ['cogs.owner']
                                    
# Loads the cogs here
if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)

bot = commands.Bot(command_prefix="*")
bot.remove_command('help')

@bot.event
async def on_ready():
	print('Logged in', bot.user.name)
	print('Version - 1.0.0')
	print('Creator - PrabaRock7#3945')
	print('Release Version - v01')
	print('ᎷᎨᏝᎾ')
	await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="*help | MiloBot™"))
	
@bot.event
async def on_member_join(member):
	print(f"{member} has joined the server.")
	
@bot.event
async def on_member_remove(member):
	print(f"{member} has left the server.")

@bot.command()
async def help(ctx):
	
	embed = discord.Embed(title="List Of Commands", colour=discord.Colour(0xff0000))
	
	embed.set_thumbnail(url="https://i.imgur.com/cUrQeXr.png")
	embed.set_footer(text=f"Command Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
	
	embed.add_field(name="**Fun**", value="*hello, *ping")
	embed.add_field(name="**Bot Related Commands**", value="*botinfo, *botsource,  *botsupportserver")
	embed.add_field(name="**Mathematics**", value="*square, *bitcoin")
	embed.add_field(name="**Moderation**", value="*clear, *kick, *ban, *unban, *avatar, *useravatar")
	await ctx.send(embed=embed)
	
@bot.command()
async def hello(ctx):
	await ctx.send("Hello!" + ", " + ctx.message.author.mention)
	
@bot.command()
async def ping(ctx):
	
	embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=ctx.message.created_at)
	embed.set_author(name="Ping")
	embed.add_field(name=f"*Pong*", value=f"**:ping_pong: {round(bot.latency * 1000)}ms**")
	embed.set_footer(text=f"Req By {ctx.author}", icon_url=ctx.author.avatar_url)
	await ctx.send(embed=embed)

@bot.command()
async def botinfo(ctx):
	
	embed = discord.Embed(colour=discord.Colour(0x00ffff), description="Milo Bot info")
	embed.set_thumbnail(url="https://i.imgur.com/cUrQeXr.png")
	
	embed.add_field(name="Bot Info", value=f"Hello {ctx.author}, thanks for showing intrest to get info about me :grin:. Im Coded using Python. For list of commnads please type -help. My Owner is <@589647651939549206>. Im a simple bot i don't have advanced commands, that's a fault.")
	embed.add_field(name="External Links", value="[Patreon](https://patreon.com/PrabaRock7), [Ko-Fi](https://ko-fi.com/prabarock7)")
	await ctx.send(embed=embed)
	
@bot.command()
async def botsupportserver(ctx):
	
	embed = discord.Embed(title="Support server")
	embed.add_field(name="Server Link", value="Touch the below link to join the server")
	await ctx.send(content="https://discord.gg/FeD6RUs", embed=embed)
	
@bot.command()
async def avatar(ctx):
	show_avatar = discord.Embed(
	
	         color = discord.Color.blue()
	)
	show_avatar.set_image(url="{}".format(ctx.author.avatar_url))
	await ctx.send(embed=show_avatar)
	
@bot.command()
async def useravatar(ctx, member : discord.Member):
	show_avatar = discord.Embed(
	
	         color = discord.Color.dark_blue()
	)
	show_avatar.set_image(url="{}".format(member.avatar_url))
	await ctx.send(embed=show_avatar)
	
@useravatar.error
async def useravatar_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"Please specify a **member** to show his/her *avatar* {ctx.author.mention}")

@bot.command()
async def botsource(ctx):
	await ctx.send("https://github.com/PrabaRock/Milo-Bot")
	
@bot.command()
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " squared is " + str(squared_value))

@bot.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.botSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await bot.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

bot.run(os.getenv('TOKEN'))
