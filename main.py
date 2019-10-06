import discord,os,re

#TO do
# Give roles
# Respond to questions
# alert mods
# bug reporting

client = discord.Client()

sentreports=[]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # if message.content.startswith('$greet'):
    #     channel = message.channel
    #     await channel.send('Say hello!')

    #     def check(m):
    #         return m.content == 'hello' and m.channel == channel

    #     msg = await client.wait_for('message', check=check)
    #     await channel.send('Hello {.author}!'.format(msg))
    if message.content.startswith('$lulw'):
        channel = message.channel
        await channel.send('Sick meme bruh')

    if message.content.startswith('`creator'):
        channel = message.channel
        await channel.send('I am created by Hawkeye. You can find more about me here: https://github.com/H4wki/SyntaxrBot/tree/master')

    if message.content.startswith('`clear'):
        channel = message.channel
        await channel.purge()

    if message.content.startswith('`help'):
        target = message.author
        await target.send("Hi there, I hear you are looking for some instructions on my instructions. You can find a list of commands here: https://github.com/H4wki/SyntaxrBot/blob/master/currentCommands",delete_after=60)

    if message.content.startswith('`report'):
        if message.channel.name != "bug-report":
            for i in client.get_all_channels():
                if i.name == "bug-report":
                    problem = re.split(r'\w\s', message.content, 1)
                    await i.send('Reportee: {0}\nTime sent: {1} \nDescription: {2}'.format(message.author, message.created_at, problem[1]))
    

getToken = open("token.token", "r")
token = getToken.read()
client.run(token)
