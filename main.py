import discord,os,re

#TO do
# Give roles
# Respond to questions
# alert mods
# bug reporting

client = discord.Client()

sentreports = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):    
    if isinstance(message.channel, discord.TextChannel):
        if message.channel.name == "bot-commands":
            if message.content.startswith('`lulw'):
                channel = message.channel
                await channel.send('Sick meme bruh')

            if message.content.startswith('`creator'):
                channel = message.channel
                await channel.send('I am created by Hawkeye. You can find more about me here: https://github.com/H4wki/SyntaxrBot/tree/master')

            if message.content.startswith('`clear'):
                channel = message.channel
                await channel.purge()#change this to not be 

            if message.content.startswith('`help'):
                target = message.author
                await target.send("Hi there, I hear you are looking for some instructions on my instructions. You can find a list of commands here: https://github.com/H4wki/SyntaxrBot/blob/master/currentCommands",delete_after=60)

            if message.content.startswith('`report'):
                if message.channel.name != "bug-report":#can get refactored not to look for the channel #hardcodeforlyfe
                    for i in client.get_all_channels():
                        if i.name == "bug-report":
                            problem = re.split(r'\w\s', message.content, 1)
                            #await i.send('\033[1m'+'Reportee:'+'\033[0m'+' {0}\nTime sent: {1} \nDescription: {2}'.format(message.author, message.created_at, problem[1]))
                            await i.send('Reportee:{0} \nTime sent: {1} \nDescription: {2}'.format(message.author, message.created_at, problem[1]))
                            await message.delete()

            # if message.content.startswith('`play'): #WIP because ffmpeg sounds painful
            #     target = message.author
            #     if message.author.voice != None:
            #         targetvoicestatechannel = message.author.voice.channel
            #         await targetvoicestatechannel.connect()
            #         print("Is in a voice channel")
            #     else:
            #         print("not in a voice channel")
    

getToken = open("token.token", "r")
token = getToken.read()
client.run(token)
