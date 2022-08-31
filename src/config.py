TOKEN = "secret-api-key"  # Secret API token provided by discord api
STEAM_PATH = "C:\Program Files (x86)\Steam"  # Absolute path to steam folder
CHANNEL_NAME = "channel-name"  # Channel name the bot will send the message in
GAME_APP_ID = 730  # Game steam-app id
GAME_PROCESS_NAME = "csgo"  # Game's windows process name
LIFE_CHECK_INTERVAL = 3  # How often to check if game has been terminated
MAX_LIFE_CHECK_TRIES = 10  # Max tries for checking if the game launched

# Settings for embeded messages
EMBEDS = {
    "on": {
        "titles": ["CS:GO Launched", "Game launched"],
        "descriptions": ["GL & HF"],
        "images": ["https://cdn.frankerfacez.com/emoticon/113912/4"],
    },
    "off": {
        "titles": ["CS:GO turned off", "Exited game"],
        "descriptions": ["GGs"],
        "images": ["https://cdn.frankerfacez.com/emoticon/299177/4"],
    },
}

