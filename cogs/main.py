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
		await ctx.send("Pong")

        @commands.command()
	async def myavatar(self, ctx):
		show_avatar = discord.Embed(
		
		         color = discord.Color.dark_blue()
		)
		show_avatar.set_image(url="{}".format(ctx.author.avatar_url))
		await ctx.send(embed=show_avatar)
		
	@commands.command()
        async def useravatar(self, ctx, member : discord.Member):
                show_avatar = discord.Embed(
      
                         color = discord.Color.blue()
                )
                show_avatar.set_image(URL="{}".format(member.avatar_url))
                await ctx.send(embed=show_avatar)

def setup(client):
	client.add_cog(Main(client))
