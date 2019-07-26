import discord 
from discord.ext import commands

class Mod(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f"{member} has been kick out by {ctx.author}")
		
def setup(client):
	client.add_cog(Mod(client))
