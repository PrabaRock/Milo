import discord 
from discord.ext import commands

class Mod(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f"{member} has been kick out by {ctx.author} for the reason {reason}")
		
	@commands.command()
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		await memeber.ban(reason=reason)
		await ctx.send(f"{member} has been banned successfully by {ctx.author}")
		
	@commands.command()
	async def clear(self, ctx, amount : int):
		await ctx.channel.purge(limit=amount)
		await ctx.send(f"{amount} of messages has been deleted, the message was deleted by {ctx.author}")
	
def setup(client):
	client.add_cog(Mod(client))
