import os

class Config(object):
    BOT_TOKEN = os.environ.get("8447554320:AAEN2-vR3uog54OBYbT72GSKJ3jBgbVeg9E")
    API_ID = int(os.environ.get("27991871"))
    API_HASH = os.environ.get("8dda0c086a4bb6cd0f5a3b74b55fdee3")
    AUTH_USER = os.environ.get('AUTH_USERS', '7734031129').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
