import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import nltk
import discord
from discord.ui import Select, View
from discord.ext import commands
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

#Your path for chrome webdriver
browser = webdriver.Chrome(executable_path="")

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True #v2
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix = "!", intents=intents)
@bot.command()
async def start(ctx):
    start = 39

    while True:
        browser.get('https://announcement.ekgamesserver.com/?ppk=42f47521-f47a-496b-9e90-af01f0f10c37&l=en')
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.findAll('tr')
        i = 0

        for result in results:
            i += 1
            print("https://announcement.ekgamesserver.com" + result.a['href'])
            print(i)
        if i > start:
            start += 1
            browser.get('https://announcement.ekgamesserver.com' + results[0].a['href'])
            html2 = browser.page_source
            soup2 = BeautifulSoup(html2, 'html.parser')
            text2 = soup2.get_text()
            await ctx.send(text2 + "\n @everyone")
            time.sleep(3600)

bot.run(BOT_TOKEN)