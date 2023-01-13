import json #Used for reading the json files
import time #Used for the /uptime command
import random #Used for the random chance, and random messages
import math #Used for flooring the time in /uptime
import discord #Main discord library 
from discord import app_commands #Discord library for command tree
from textblob import TextBlob #Sentiment analysis

#Set intents and stuff
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
startTime = time.time()

#Load initial token from json
#Also all of the other json functions, such as writing
with open('config.json', 'r') as f:
    data = json.load(f)

def checkAdmin(user):
    if data['adminrole'] == 0:
        return True
    elif data['adminrole'] != 0:
        if data['adminrole'] in [role.id for role in user.roles]:
            return True
        else:
            return False

#Changing the chance of a random message
def write_chance(new_data, filename='config.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["chance"] = new_data
        file.seek(0)
        json.dump(file_data, file, indent = 4)

#Add a new message
def write_msg(new_data, count, filename='config.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["random_msg"][str(count)] = new_data
        file_data["randomtotal"] = count
        file.seek(0)
        json.dump(file_data, file, indent = 4)

#Add a new bad response
def write_bad(new_data, count, filename='config.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["badmsg"][str(count)] = new_data
        file_data["badtotal"] = count
        file.seek(0)
        json.dump(file_data, file, indent = 4)

#Add a good response
def write_good(new_data, count, filename='config.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["goodmsg"][str(count)] = new_data
        file_data["goodtotal"] = count
        file.seek(0)
        json.dump(file_data, file, indent = 4)


#Main commands
@tree.command(name = "cmds", description = "commands") 
async def thrid_cmd(interaction):
    embed = discord.Embed(title="Commands", description="View the commands [here](https://docs.google.com/document/d/1s1WaFZJ32MibsfDf4sYifXd84n55ymBpLoIxw8LPeZ8/edit?usp=sharing)", color=3145631)
    await interaction.response.send_message(embed=embed)

@tree.command(name = "info", description = "basic bot info") 
async def first_command(interaction):
    embed = discord.Embed(title="Info", description="This is a crappy bot by <@745118326715580448> \nIdk what else to put. It was coded in 1 night by a sleep deprived trans girl in python \nIt has some cool things like sentiment analysis and rng", color=3145631)
    await interaction.response.send_message(embed=embed)

@tree.command(name = "uptime", description = "Gets the bot's uptime") 
async def first_oucommand(interaction):
    embed = discord.Embed(title="Uptime", description=f"Started: <t:{math.floor(startTime)}:t> (<t:{math.floor(startTime)}:R>)", color=3420915) #Use math module to floor numbers for discord
    embed.set_footer(text="Resets each update. The time is in your current timezone")
    await interaction.response.send_message(embed=embed)

@tree.command(name = "analysis", description = "Preforms a sentiment analysis on the provided string") 
async def first_oucommand(interaction, sentence: str = "None"):
    edu = TextBlob(sentence)
    x = edu.sentiment.polarity

    global goodBad
    pol = str(x)
    if x<0:
        goodBad = "Bad"
    elif x == 0:
        goodBad = "Cant tell"
    elif x>0 and x <=1:
        goodBad = "Good"
    embed = discord.Embed(title="Result", description=f"The string ```{sentence}``` was classified as **{goodBad}** by the [TextBlob](https://textblob.readthedocs.io/en/dev/) analysis \n\n```POLARITY: {pol}```", color=3145631)
    await interaction.response.send_message(embed=embed)
    


@tree.command(name = "rate", description = "Change the % (I.E, 50 would be 1 in 50%)") 
async def rthwrthwrf(interaction, rate: int = 50):
    if checkAdmin(interaction.user) == True: #Bit jenky, but works
        if rate < 200 and rate > 0:
            write_chance(rate)
            embed = discord.Embed(title="", description=f"Successfully changed the chance to 1 in {str(rate)} \n\n```200: WROTE TO JSON SUCCESSFULLY```", color=3145631)
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="", description="Please add a valid rate from 1-200", color=16724547)
            await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="No perms???", description="You don't have perms to run this. \n\nL+BOZO", color=16724547)
        await interaction.response.send_message(embed=embed)

@tree.command(name = "switch", description = "Toggle the bot on or off") 
async def hrh(interaction):
    with open('config.json', 'r') as f:
        data = json.load(f)
    game = discord.Game(data['status']) #Set the status if its turned back on
    if 1062265524739919924 in [role.id for role in interaction.user.roles] or 1062520629607272598 in [role.id for role in interaction.user.roles]:
        if data['on'] == 1:
            with open('config.json','r+') as file:
                file_data = json.load(file)
                file_data["on"] = 0
                file.seek(0)
                json.dump(file_data, file, indent = 4)
            embed = discord.Embed(title="", description=f"Successfully disabled the bot \n\n```200: WROTE TO JSON SUCCESSFULLY```", color=3145631)
            await interaction.response.send_message(embed=embed)
            await client.change_presence(status=discord.Status.idle, activity=game) #Set to idle
        else:
            with open('config.json','r+') as file:
                file_data = json.load(file)
                file_data["on"] = 1
                file.seek(0)
                json.dump(file_data, file, indent = 4)
            embed = discord.Embed(title="", description=f"Successfully enabled the bot \n\n```200: WROTE TO JSON SUCCESSFULLY```", color=3145631)
            await interaction.response.send_message(embed=embed)
            await client.change_presence(status=discord.Status.online, activity=game)
    else:
        embed = discord.Embed(title="No perms???", description="You don't have perms to run this. \n\nL+BOZO", color=16724547)
        await interaction.response.send_message(embed=embed)



@tree.command(name = "addbadword", description = "Adds a bad prase") 
async def rthrth(interaction, phrase: str="Hello"):
    if checkAdmin(interaction.user) == True:
        with open('config.json', 'r') as f:
            data = json.load(f)
        count = data['badtotal']+1
        write_bad(phrase, count)
        embed = discord.Embed(title="", description=f"Successfully added {phrase} as a bad phrase! \n\n```200: WROTE TO JSON SUCCESSFULLY```", color=3145631)
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="No perms???", description="You don't have perms to run this. \n\nL+BOZO", color=16724547)
        await interaction.response.send_message(embed=embed)


@tree.command(name = "addword", description = "Adds a phrase") 
async def rthwh(interaction, phrase: str="Hello"):
    if checkAdmin(interaction.user) == True:
        with open('config.json', 'r') as f:
            data = json.load(f)
        count = data['randomtotal']+1
        write_msg(phrase, count)
        embed = discord.Embed(title="", description=f"Successfully added {phrase} as a  phrase! \n\n```200: WROTE TO JSON SUCCESSFULLY```", color=3145631)
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="No perms???", description="You don't have perms to run this. \n\nL+BOZO", color=16724547)
        await interaction.response.send_message(embed=embed)

@tree.command(name = "addgoodword", description = "Adds a good phrase") 
async def thwrtt(interaction, phrase: str="Hello"):
    if checkAdmin(interaction.user) == True:
        with open('config.json', 'r') as f:
            data = json.load(f)
        count = data['goodtotal']+1
        write_good(phrase, count)
        embed = discord.Embed(title="", description=f"Successfully added {phrase} as a good phrase! \n\n```200: WROTE TO JSON SUCCESSFULLY```", color=3145631)
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="No perms???", description="You don't have perms to run this. \n\nL+BOZO", color=16724547)
        await interaction.response.send_message(embed=embed)

async def messageChecks(message, data):
    if data['on'] == 1:
        ran = random.randint(1, data['chance'])
        if ran == 1:
            #Python experts look away now (as if this was not already bad enough LOL)
            rn = random.randint(1, data['randomtotal'])
            msg = data['random_msg'][str(rn)]
            await message.reply(msg)
        
        #check for pings
        if client.user.mentioned_in(message):

            #Use sentiment analysis to determine the content and tone
            #ADD CODE TO REMOVE THE @BOT LATER
            edu = TextBlob(message.content.lower())
            x = edu.sentiment.polarity

            if x<0:
                rn = random.randint(1, data['badtotal'])
                msg = data['badmsg'][str(rn)]
                await message.reply(msg)
            elif x == 0:
                #If it cant tell, reply with set message
                await message.reply("What are you even saying")
            elif x>0 and x <=1:
                rn = random.randint(1, data['goodtotal'])
                msg = data['goodmsg'][str(rn)]
                await message.reply(msg)


#Random/ping messages
@client.event
async def on_message(message):
    with open('config.json', 'r') as f:
        data = json.load(f)

    #Checking if its on a set channel
    if data['allowedchannel'] != 0:
        if message.channel.id == data['allowedchannel']:
            await messageChecks(message, data)
    elif data['allowedchannel'] == 0:
        await messageChecks(message, data)

#Log in/on ready
@client.event
async def on_ready():
    await tree.sync()
    with open('config.json', 'r') as f:
        data = json.load(f)
    game = discord.Game(data['status'])
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Logged in and ready!")
client.run(data['token'])
