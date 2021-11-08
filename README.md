# discord_translater
Simple bot that sends sentences when someone in particular writes a particulary word.
Feel free to use the code.
## Setup and Run

Requires **Python 3.7+**. You can download the latest version of Python [here](https://www.python.org/downloads/).

I recommend working in a **virtual environment**. 

Install the necessary package :

**Windows**

    py -3 -m pip install -r setup\requirements.txt
    
**Linux**

    python3 -m pip install -r setup/requirements.txt
    
In first, you need to create a new application on the [discord developer website](discord.com/developers/applications). Once you have created it, add bot to the app in bot section. You can turn off "public bot" if you don't want other people to add your bot to their servers. Give the administrator permission to the bot. Then, below the name of the bot, you can copy the token needed in the program to run the bot.
 
Start the bot :

-  To run it in the terminal :
  
    py lib/main.pyw &
  
  Do ctrl-C to stop it.
  
-  To run it in the background :
  
    pyw lib/main.pyw

## Credits
Created by Ribou ([Twitter](ribou.fr/twitter), [Twitch](ribou.fr/twitch))

Documentation of [discord.py](https://discordpy.readthedocs.io/en/stable)

Videos on YouTube to understand how API work.
