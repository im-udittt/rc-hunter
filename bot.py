import os
import requests
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.streaming, name="Udxt-labs!", url="https://youtube.com/@udxt")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def find(ctx, rc_number):

    if not rc_number:
        await ctx.send("The correct useage of the command is **`!find <rc_number>`**")
        return

    url = "https://vehicle-rc-verification-advanced.p.rapidapi.com/v3/tasks/sync/verify_with_source/ind_rc_plus"

    payload = {
        "task_id": os.getenv('TASK_ID'),
        "group_id": os.getenv('GROUP_ID'),
        "data": { "rc_number": rc_number }
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv('X-RAPIDAPI-KEY'),
        "X-RapidAPI-Host": os.getenv('X-RAPIDAPI-HOST')
    }

    response = requests.post(url, json=payload, headers=headers)

    # Set the filename to the value of "rc_number" in the payload
    filename = f"{payload['data']['rc_number']}.json"

    # Write the JSON response to a new file with the rc_number as the filename
    with open(filename, 'w') as f:
        json.dump(response.json(), f)

    # Upload the file to Discord
    with open(filename, 'rb') as f:
        # Create an embed message
        embed = discord.Embed(title=f"**Result for RC number `{rc_number}`**", color=0x00ff00)
        await ctx.send(embed=embed)
        await ctx.send(file=discord.File(f))

bot.run(os.getenv('TOKEN'))
