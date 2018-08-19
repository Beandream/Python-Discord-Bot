    if message.content.startswith('!hello'):
        msg = ''' X | O | X
---+---+---
 O | X | O
---+---+---
 O | x | O'''.format(message)
        await client.send_message(message.channel, msg)