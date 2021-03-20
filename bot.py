import discord
from f1api import constructors_championship, drivers_championship, last_race

client = discord.Client()

@client.event
async def on_ready():
        print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return     

    if message.content.startswith('!help'):
            await message.channel.send('Use !wdc for current Driver Standings. !constructors for current Constructor Standings and !lastrace to get the results of the last race.')

    if message.content.startswith('!constructors'):
            await message.channel.send('\n'.join(constructors_championship))

    if message.content.startswith('!wdc'):
            await message.channel.send('\n'.join(drivers_championship))

    if message.content.startswith('!lastrace'):
            await message.channel.send('\n'.join(last_race))


client.run('Token')