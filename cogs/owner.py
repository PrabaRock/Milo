import discord
from discord.ext import commands

class Owner(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(hidden=True)
	@commands.is_owner()
	async def cog_load(self, ctx, *, cog: str):
		"""Loads the cogs of Milo Bot"""
		
		try:
			self.bot.load_extension(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`**{type(e).__name__} - {e}')
		else:
			await ctx.send('**`Successfully loaded`**')
			
	@commands.command(hidden=True)
	@commands.is_owner()
	async def cog_unload(self, ctx, *, cog: str):
		"""Unload a Module"""
		
		try:
			self.bot.unload_extensio(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`**{type(e).__name__ - {e}')
		else:
			await ctx.send('**`Successfully unloaded`**')
			
	@commands.command(hidden=True)
	@commands.is_owner()
	async def cog_reload(self, ctx, *, cog: str):
		# Reloads the cog
		
		try:
			self.bot.load_extension(cog)
			self.bot.unload_extension(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`**{type(e).__name__ - {e}')
		else:
			await ctx.send('**`Successfully reloaded`**)
			
def setup(bot):
	bot.add_cog(Owner(bot))
