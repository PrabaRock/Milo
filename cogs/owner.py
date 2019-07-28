import discord
from discord.ext import commands

class Owner(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.command(hidden=True)
	@commands.is_owner()
	async def cog_load(self, ctx, *, cog: str):
		"""Loads the cogs of Milo Bot"""
		
		try:
			self.client.load_extension(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`**{type(e).__name__} - {e}')
		else:
			await ctx.send('**`Successfully loaded`**')
			
	@commands.command(hidden=True)
	@commands.is_owner()
	async def cog_unload(self, ctx, *, cog: str):
		"""Unload a Module"""
		
		try:
			self.client.unload_extensio(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`**{type(e).__name__ - {e}')
		else:
			await ctx.send('**`Successfully unloaded`**')
			
	@commands.command(hidden=True)
	@commands.is_owner()
	async def cog_reload(self, ctx, *, cog: str):
		# Reloads the cog
		
		try:
			self.client.load_extension(cog)
			self.client.unload_extension(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`**{type(e).__name__ - {e}')
		else:
			await ctx.send('**`Successfully reloaded`**)
			
def setup(client):
	client.add_cog(Owner(client))
		
