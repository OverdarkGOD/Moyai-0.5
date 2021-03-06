import discord, requests, json, asyncio, os
import platform
import time
import re
import datetime 
from discord.ext import commands, tasks
from urllib import parse
from discord import Forbidden 


start_time = datetime.datetime.utcnow()


class InfoCommands(commands.Cog):

	def __init__(self, client):
		self.client = client

	@staticmethod
	def _getRoles(roles):
		string = ''
		for role in roles[::-1]:
			if not role.is_default():
				string += f'{role.mention},'
		if string == '':
			return 'None'
		else:
			return string[:-2]

	@commands.command()
	async def Hey(self, ctx):
		await ctx.send('Hello!')

	@commands.command()
	async def peeng(self, ctx):
		await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title=f"{ctx.guild.name}", description="Moyai a Discord bot!", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
		embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
		embed.add_field(name="Version", value=f"Version 0.5")
		embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
		embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
		await ctx.send(embed=embed)

	@commands.command(aliases=['uptime', 'up'])
	async def status(self, ctx):
		uptime = datetime.datetime.utcnow() - start_time 
		uptime = str(uptime).split('.')[0]
		information = '''
		Guilds: `{:,}`
		Users: `{:,}`'''.format(len(self.client.guilds), len(self.client.users))
		em = discord.Embed(title = 'Nerd Stats', description = information, colour = discord.Color.random())
		em.set_author(name = 'Nerd Stats')
		em.add_field(name = 'Nerd', value = 'Latency: `{}ms`\nAPI Latency: **Checking...**\nUptime: `{}`'.format(round(self.client.latency * 1000), uptime), inline = True)
		em.set_footer(text = "Made in discord.py version {}".format(discord.__version__))
		em.add_field(name = "Python Version", value=platform.python_version(), inline = True)
		em.add_field(name = "OperatingSystem", value=f'{platform.system()} {platform.release()} {platform.version()}', inline = False)
		before_check = datetime.datetime.utcnow()
		send_me = await ctx.send(embed=em)
		after_check = datetime.datetime.utcnow()
		api_latency = after_check - before_check
		new_embed = discord.Embed(description = information, colour = discord.Color.random())
		new_embed.set_author(name = 'Nerd Stats')
		new_embed.add_field(name = 'Nerd', value = 'Latency: `{}ms`\nAPI Latency: `{}ms`\nUptime: `{}`'.format(round(self.client.latency * 1000), str(api_latency).split(".")[1] [:-3], uptime), inline = True)
		new_embed.set_footer(text = "Made in discord.py version {}".format(discord.__version__))
		new_embed.add_field(name = "Python Version", value=platform.python_version(), inline = False)
		new_embed.add_field(name = "Operating System", value=f'{platform.system()} {platform.release()} {platform.version()}', inline = False)
		await send_me.edit(embed=new_embed)

	@commands.command()
	async def whois(self, ctx, member: discord.Member=None):
		if member ==None:
			member = ctx.author

		if member.top_role.is_default():
			topRole = 'everyone' #to prevent @everyone spam
			topRoleColour = '#000000'
		else:
			topRole = member.top_role
			topRoleColour = member.top_role.colour

		if member is not None:
			embed = discord.Embed(color=member.top_role.colour)
			embed.set_footer(text=f'UserID: {member.id}')
			embed.set_thumbnail(url=member.avatar_url)
			if member.name != member.display_name:
				fullName = f'{member} ({member.display_name})'
			else:
				fullName = member
			embed.add_field(name=member.name, value=fullName, inline=False)
			embed.add_field(name='Joined Discord on', value='{}\n(Days since then: {})'.format(member.created_at.strftime('%d.%m.%Y'), (datetime.datetime.now()-member.created_at).days), inline=True)
			embed.add_field(name='Joined Server on', value='{}\n(Days since then: {})'.format(member.joined_at.strftime('%d.%m.%Y'), (datetime.datetime.now()-member.joined_at).days), inline=True)
			embed.add_field(name='Avatar Link', value=member.avatar_url, inline=False)
			embed.add_field(name="Roles", value=self._getRoles(member.roles), inline=True)
			embed.add_field(name='Role color', value='{} ({})'.format(topRoleColour, topRole), inline=True)
			embed.add_field(name='Status', value=member.status, inline=True)
			await ctx.send(embed=embed)
		else:
			await ctx.send("Specify a Discord User.")

def setup(client):
	client.add_cog(InfoCommands(client))