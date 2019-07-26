import discord 
from discord.ext import commands

class Mod(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.bot_has_permissions(kick_member=True)
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f"{member} has been kick out by {ctx.author} for the reason {reason}")
		
def setup(client):
	client.add_cog(Mod(client))
