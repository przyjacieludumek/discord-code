import discord
import random
from bot_logic import gen_emodji
from bot_logic import flip_coin

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')
    for guild in client.guilds:
        channel = guild.system_channel
        if channel is not None:
            await channel.send("Cześć!")

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/Cześć'):
        await message.channel.send("Witaj!")
    elif message.content.startswith('/Pa'):
        await message.channel.send("Papa")
    elif message.content.startswith('/Smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('/Moneta'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('/G.hasła'):
        await message.channel.send(gen_pass(10))   
    else:
        await message.channel.send()
    

client.run("MTE3NzkyMjQzNTM0NjA5MjA3Mg.Gry07v.rhmhsIB6ez_7SYfiR6ujZ6JreRYosDMOpS-_Vo")
