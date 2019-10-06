import discord,os

#TO do
# Give roles
# Respond to questions
# alert mods
# bug reporting

client = discord.Client()

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
        chanel = message.channel
        await chanel.send('Sick meme bruh')

    if message.content.startswith('`creator'):
        chanel = message.channel
        await chanel.send('I am created by Hawkeye. You can find more about me here: https://github.com/H4wki/SyntaxrBot/tree/master')

    if message.content.startswith('`help'):
        target = message.author
        await target.send("Hi there, I here you are looking for some instructions on my instructions. You can find a list of commands here: ")

getToken = open("token.token", "r")
token = getToken.read()
client.run(token)
