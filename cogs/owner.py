import discord
from discord.ext import commands

class Owner(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.command(name="reload", hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
    	"""Command which Reloads a Module.
    	Remember to use dot path. e.g: cogs.owner"""
    	
    	try:
    		self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

def setup(client):
    client.add_cog(Owner(client))
