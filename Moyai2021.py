from distutils import extension
import discord, os, sys, requests, colorama, base64
import psutil, time, json, datetime, asyncio
import smtplib
import logging
import platform
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from colorama import Fore, init
from itertools import cycle
from email.message import EmailMessage
init()

if not os.path.isfile("config.py"):
	sys.exit("'config.py' not found! Please add it and try again.")

else:
	import config
	from setup import ver

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=config.logfile, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = Bot(description=config.des, command_prefix=config.pref)

print("Connecting!")

@client.event 
async def on_ready():
	print("Bot is online!\n")
	print("Running on:", platform.system(), platform.release(), "(" + os.name + ")")
	print("Moyai version:", ver)
	print("Name : {}".format(client.user.name))
	print("Client ID : {}".format(client.user.id))
	print("Currently active on " + str(len(client.guilds)) + " server(s).\n")
	logger.info("Bot started successfully.")

cool = "```xl\n{0}\n```"
prefix = config.pref

@client.command()
async def info_help(ctx):
	info = f'''`{prefix}ping` - Shows the client latency.
`{prefix}info` - Shows information about the bot.
`{prefix}status` - Shows client latency, API latency, uptime, and Discord/Python versions.
`{prefix}whois` - shows information about a user.'''
	em = discord.Embed(title = "Info Commands", description = f'`{prefix}info_help` - shows this command', colour = discord.Color.random())
	em.add_field(name = 'Info', value = info, inline = True)
	em.set_footer(text = "If there is an issue, report the issue to OverdarkGOD#8542.")
	await ctx.send(embed=em)

@client.command()
async def fun_help(ctx): 
	Fun = f'''`{prefix}em` - embeds the message.
`{prefix}av` - shows the avatar of a user pinged. 
`{prefix}spam` - Spam a message you want to send with the amount after the message.
`{prefix}email` - Send an email an email address.
`{prefix}ping` - Ping an IP or DNS.
`{prefix}google` - Google Search
`{prefix}urban` - Search the Urban Dictionary'''
	em = discord.Embed(title = "Fun Commands", description = f'`{prefix}fun_help` - shows this command', colour = discord.Color.random())
	em.add_field(name = 'Fun', value = Fun, inline = True)
	em.set_footer(text = "If there is an issue, report the issue to OverdarkGOD#8542.")
	await ctx.send(embed=em)


@client.command()
async def music_help(ctx):
	Music = f'''`{prefix}join` - The bot will join the voice channel you are currently in.
	`{prefix}leave` - The bot will leave the voice channel.
	`{prefix}resume` - The bot will resume the current song. 
	`{prefix}pause` - The bot will pause the current song.
	`{prefix}queue` - The bot will queue the requested song.
	`{prefix}now` - The bot will show what song is currently playing.
	`{prefix}shuffle` - The bot will play a random song. 
	`{prefix}loop` - The bot will forever loop a song. To stop it, re-enter the command.'''
	em = discord.Embed(title = "Music Commands", description = f'`{prefix}Mhelp` - shows this command', colour = discord.Color.random())
	em.add_field(name = 'Music', value = Music, inline = True)
	em.set_footer(text = "If there is an issue, report the issue to OverdarkGOD#8542.")
	await ctx.send(embed=em)

@client.command()
async def load(ctx):
	if __name__ == "__main__":
		for extension in config.startup_extensions:
			try: 
				client.load_extension(extension)
				print("loaded extension '{0}'".format(extension))
				logger.info("Loaded extension '{0}'".format(extension))
			except Exception as e: 
				exc = '{0}: {1}'.format(type(e).__name__, e)
				print('Failed to load extension {0}\nError: {1}'.format(extension, exc))
				logger.info('Failed to load extension {0}\nError: {1}'.format(extension, exc))

if __name__ == "__main__": 
	if not config.startup_extensions:
		print("No extensions enabled!")
	else:
		print("Loading extensions!")

	for extension in config.startup_extensions:
			try: 
				client.load_extension(extension)
				print("loaded extension '{0}'".format(extension))
				logger.info("Loaded extension '{0}'".format(extension))
			except Exception as e: 
				exc = '{0}: {1}'.format(type(e).__name__, e)
				print('Failed to load extension {0}\nError: {1}'.format(extension, exc))
				logger.info('Failed to load extension {0}\nError: {1}'.format(extension, exc))

if __name__ == "__main__":

	client.run(config.bbtoken)