import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="*")

@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
	
@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f"cogs.{filename[:-3]}")

@client.command()
async def ping(ctx):
	
	embed = discord.Embed(color=discord.Color.blue(), title=f"Pong :ping_pong: {ctx.author}", description=f"{round(client.latency * 1000)} ms")
	await ctx.send(embed=embed)
	
@client.command()
async def botinfo(ctx):
	
	embed = discord.Embed(colour=discord.Colour(0x00ffff), description="Milo Bot info")
	embed.set_thumbnail(url="https://i.imgur.com/cUrQeXr.png")
	
	embed.add_field(name="Bot Info", value=f"Hello {ctx.author}, thanks for showing intrest to get info about me :grin:. Im Coded using Python. For list of commnads please type -help. My Owner is <@589647651939549206>. Im a simple bot i don't have advanced commands, that's a fault.")
	embed.add_field(name="External Links", value="[Patreon](https://patreon.com/PrabaRock7), [Ko-Fi](https://ko-fi.com/prabarock7)")
	await ctx.send(embed=embed)
	
@client.command()
async def botsupportserver(ctx):
	
	embed = discord.Embed(title="Support server")
	embed.add_field(name="Server Link", value="Touch the below link to join the server")
	await ctx.send(content="https://discord.gg/FeD6RUs", embed=embed)
		
client.run(os.getenv("TOKEN"))
