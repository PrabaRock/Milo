import discord
from discord.ext import commands

class Main(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.Cog.listener()
	async def on_ready(self):
		print("Bot is Online :)")
		
	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f"Pong {round(self.latency * 1000)} ms")

def setup(client):
	client.add_cog(Main(client))
