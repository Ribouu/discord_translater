# discord_translater
![traducteur-removebg-preview (1)](https://user-images.githubusercontent.com/76816773/140748275-658fdc5b-c974-495e-9e82-6571fc73661a.png)


Simple bot that sends sentences when someone in particular writes a particular word.
Feel free to use the code.
I know it's simple, but you can use it as a base for something else.
The code is running online with Heroku. If you want to run it on your own computer, I advise changing the extension of the file to .pyw to run it in the background, without any window. You can change it into .py if you want to keep the possibility to stop it easily. Otherwise, you can stop it in the task manager (for Windows, I don't know for Linux and MacOs).

## Setup and Run

Requires **Python 3.7+**. You can download the latest version of Python [here](https://www.python.org/downloads/).

I recommend working in a **virtual environment**. 

Install the necessary package :

**Windows**

    py -3 -m pip install -r requirements.txt
    
**Linux**

    python3 -m pip install -r requirements.txt
    
In first, you need to create a new application on the [discord developer website](discord.com/developers/applications). Once you have created it, add bot to the app in bot section. You can turn off "public bot" if you don't want other people to add your bot to their servers. Give the administrator permission to the bot. Then, below the name of the bot, you can copy the token needed in the program to run the bot. 
To add the bot to whatever server you want, go to the OAuth2 section, click bot in the scopes panel. You just have to access the given link to choose the desired server.
For the name and the image, use whatever you want. I used this copyright-free image (under creative-commons license) : https://commons.wikimedia.org/wiki/File:Logo_traduction_vert.svg


You also need the id of the user whose messages you want to translate. In discord, go to advanced settings and check the developer mode. Now, you just have to right-click on the user and copy their id.

Finally, in main.pyw, change the user_id and client_id with the previous ids.
 
Start the bot :

-  To run it in the terminal :
  
        py lib/app.pyw &
  
  Do ctrl-C to stop it.
  
-  To run it in the background :
  
        pyw lib/app.pyw

You can also run it by double-clicking on app.pyw.

## Credits
Created by Ribou ([Twitter](https://www.ribou.fr/twitter), [Twitch](https://www.ribou.fr/twitch))

Documentation of [discord.py](https://discordpy.readthedocs.io/en/stable)

Videos on YouTube to understand how API work.