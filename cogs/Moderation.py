import discord 
import asyncpg
import asyncio 
import re
import datetime 
import json 
from discord import Forbidden
from discord import Member
from discord import TextChannel
from discord import Role 
from discord import utils
from discord.ext import commands
from discord.ext import tasks 


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, arg: str=None):
        if arg == None:
            embed = discord.Embed(
                title='You must specify the amount you want to purge.'

            )
            await ctx.send(embed=embed)
        try: 
            if int(arg) > 400:
                embed = discord.Embed(
                    title = "I can not purge over 400 messages.",
                    colour = discord.Colour.red() 
                )
                await ctx.send(embed=embed)

            if int(arg) < 401: 
                purge = int(arg) + 1
                await ctx.channel.purge(limit=purge)
                embed = discord.Embed(
                    title = str(arg) + 'Messages were purged!',
                    colour = discord.Colour.green()
                )
                await ctx.send(embed=embed, delete_after=3)
        except:
            await ctx.send(":x: Failed to purge messages.")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await member.ban(reason = reason)

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, *, member): 
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unabn(user)
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return 

def setup(client):
	client.add_cog(Moderation(client))