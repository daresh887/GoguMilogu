import discord
import matplotlib.pyplot as plt
import random
import asyncio
import imageio
import os
from dotenv import load_dotenv
from discord.ext import commands
import requests

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready as {bot.user}')

def bubble_sort_gif(data, gif_filename='bubble_sort.gif'):
    images = []
    n = len(data)
    
    fig, ax = plt.subplots()

    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            
            ax.clear()
            ax.bar(range(len(data)), data, color='blue')
            plt.title(f"Pasul {i * (n - i - 1) + j + 1}")
            
            frame_filename = f"frame_{i}_{j}.png"
            plt.savefig(frame_filename)
            images.append(imageio.imread(frame_filename))
            
            os.remove(frame_filename)

    imageio.mimsave(gif_filename, images, fps=2)

@bot.command()
async def bubble_sort(ctx):
    data = [random.randint(1, 100) for _ in range(10)]
    await ctx.send(f"Sirul: {data}")

    gif_filename = 'bubble_sort.gif'
    bubble_sort_gif(data, gif_filename)

    await ctx.send(file=discord.File(gif_filename))

    os.remove(gif_filename)
    
def get_random_image():
    url = "https://random.imagecdn.app/500/150"
    response = requests.get(url, allow_redirects=True)
    final_url = response.url
    return final_url

@bot.command()
async def imagine(ctx):
    random_image_url = get_random_image()
    await ctx.send(random_image_url)



bot.run(TOKEN)

