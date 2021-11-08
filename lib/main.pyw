# First, we need to import the discord and random library
import discord
import random

# We'll need the user id and a client id for the bot
user_id = 'the_id'
client_id = 'the_second_id'

# Initializing discord client
client = discord.Client()

# Words that trigger the bot
words = [ # Examples in french
        "je re",
        "je reviens", "je vais revenir"
        ]

# Another scenario
music_words = [
                ";;p", ";;play"
                ]

# Answers of the bot
answers = [ # Again, examples in french
            "Il nous dit : \"A bientôt\"", 
            "Il nous dit : \"J\'reviens dans quelques jours\"", 
            "Il nous dit : \"J\'rigole je reviens pas\"", 
            "Il nous dit : \"A la prochaine\"",
            "Il nous dit : \"Je suis venu, j\'ai vu, c\'était nul donc je reviendrai pas aujourd\'hui\"",
            "Il nous dit : \"Mdr vous avez vraiment cru que j'allais revenir ?\"",
            "Il nous dit : \"er eJ\"",
            "Il nous dit : \"Je suis de gauche mais je ne l\'assume pas donc je préfère partir\"",
            "Il nous dit : \"Le vocal était mieux avant donc salut\""
            ]

# Answers for the second scenario
music_answers = [
            "Sacré zikos celui-là"
            ]

# Bot behavior :
@client.event
# When there's a message in the channel :
async def on_message(message):
    # if the author id matches the user_id of the user we want to translate :
    if message.author.id == user_id:
        # We go through the words list
        for i in range(len(words)):
            # If a word matches with a word in the message content :
            if words[i] in message.content.lower():
                # The bot answers with a random answer of the answers list
                await message.channel.send(random.choice(answers))
                # Then we break the for loop.
                break 
        # The same thing for the second scenario
        for i in range(len(music_words)):
            if music_words[i] in message.content:
                await message.channel.send(random.choice(music_answers))
                break

# Run the script
if __name__ == '__main__':
    client.run(client_id)
