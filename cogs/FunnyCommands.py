from ast import Return
from asyncio.log import logger
from email.mime import image
from inspect import Parameter
from re import sub
from unittest import result
from urllib.parse import ParseResult
import aiohttp
import pingparsing
import subprocess
import platform 
import functools
import smtplib
import ssl 
import urbandict
import config
import logging
from googlesearch import lucky, search
from textwrap import dedent 
from unittest.mock import call
from urllib import response
import discord, os, sys, json, requests, datetime, numpy, random, base64, codecs
from discord.ext import commands, tasks
from colorama import Fore, init
from random import randint
init()

class FunnyCommands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def em(self, ctx, *, args):
        await ctx.message.delete()
        em = discord.Embed(description = f'{args}', colour = 0x0000)
        await ctx.send(embed=em)

    @commands.command()
    async def av(self, ctx, member: discord.User = None):
        await ctx.message.delete()
        if member is None:
            member = ctx.message.author
        em = discord.Embed(description="Avatar", colour=0x0000)
        em.set_author(name = f"{member.name}#{member.discriminator}")
        em.set_image(url = member.avatar_url)
        await ctx.send(embed=em)
        return

    @commands.command()
    async def spam(self, ctx, amount: int, *, message):
        await ctx.message.delete()
        for _i in range(amount):
            await ctx.send(message)

    @commands.command()
    async def ping(self, ctx, message):
        ping_parser = pingparsing.PingParsing()
        transmitter = pingparsing.PingTransmitter()
        transmitter.destination = (f"{message}")
        transmitter.count = 5
        transmitter.packet_size = 32 
        result = transmitter.ping()
        await ctx.send(json.dumps(ping_parser.parse(result).as_dict(), indent=4))

    @commands.command()
    async def google(self, ctx, message):
        query = (f"{message}")
        for i in search(query, tld="co.in", num=2, stop=2, pause=2):
            await ctx.send(i)

    @commands.command()
    async def urban(self, ctx, *msg):
        try:
            word = ' '.join(msg)
            api = "http://api.urbandictionary.com/v0/define"
            logger.info("Making request to" + api)
            response = requests.get(api, params=[("term", word)]).json()
            embed = discord.Embed(description="No results found!", colour=0xFF0000)
            if len(response["list"]) == 0:
                return await ctx.send(embed=embed)
            embed = discord.Embed(title="Word", description=word, colour=embed.colour)
            embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
            embed.add_field(name="Examples:", value=response['list'][0]['example'])
            await ctx.send(embed=embed)
        except: 
            await ctx.send(config.err_mesg_generic)



def setup(client):
    client.add_cog(FunnyCommands(client))