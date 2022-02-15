import json
import os

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

#Def of lock
def get_user_list(config, key):
    with open('{}/plugins/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]
      
#Locks module
DEL_CMDS = True
DEV_USERS = get_user_list('elevated_users.json', 'devs')
DRAGONS = get_user_list('elevated_users.json', 'sudos')
SUPPORT_CHAT = 'Thanimaisupport'
DEMONS = get_user_list('elevated_users.json', 'supports')
TIGERS = get_user_list('elevated_users.json', 'tigers')
WOLVES = get_user_list('elevated_users.json', 'whitelists')

TOKEN = "BOT_TOKEN"
