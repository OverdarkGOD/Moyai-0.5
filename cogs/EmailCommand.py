from ctypes.wintypes import MSG
from email.mime.text import MIMEText
import errno
import smtplib
import ssl
import discord
import random 
import os 
import json 
import asyncio 
from discord.ext import commands, tasks

class EmailCommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mail(self, ctx, body):
        msg1 = MIMEText(body)
        msg1['Subject'] = "Test Email"
        server = smtplib.SMTP('smtp.outlook.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user="jackson.boone3@outlook.com", password="Moyai19!1234")
        server.send_message(from_addr="jackson.boone3@outlook.com", to_addrs="jacksonboone3@gmail.com", msg=msg1)
        print("Mail Send")

    
    


def setup(client):
	client.add_cog(EmailCommand(client))

