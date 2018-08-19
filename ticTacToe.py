def runGame(message):
    if message.content.startswith('!hello'):
        msg = ''' X | O | X\n---+---+---\nO | X | O\n---+---+---\nO | x | O'''.format(message)
        await client.send_message(message.channel, msg)