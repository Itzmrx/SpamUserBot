import os

class API:
    API_ID = int(os.getenv("API_ID", "24689434"))
    API_HASH = os.getenv("API_HASH", "2b2a89e9e48a08bedfd1fd3c5ff3c050")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7100012154:AAEhCQEVENcUmpZGoGvhNBQJgznZ7ZOy2lE")
    STRING_SESSION = os.getenv("STRING_SESSION", "AQAvLgW4oIqlWmJg6OYi8QUirhMrB1qmWWv-ip1ywspgbwyZQNmzxRwB_b_dJO3l4UD6lbO-cz1ySccG5mtQNYpumbqtvR-Np1MNNHkI07dqZCcW5H-qNBVLhhx8EtctnHQAWX1oAhq1Z2D8WOWyrk2AgyHSqlUIy-odpGVzJ3uVAwBjNeGcjPXcS6TPaRZ5pIkfPdkaYcWY_kJC5SpZ25XENjZBtDT4DWsTyUM25Qf-c0w5f906F4AWxD6PA8qFfAJPKGxMBLYN1g_87qRa9bb82sEMahzrK3asYCG6iw2jt0y2H4po2ABt0gNYWy_QQMwKiepNjlYMGZY-9_5w6-4JAAAAAYxrUdgA")
    STRING_SESSION_2 = os.getenv("STRING_SESSION_2", "")
    STRING_SESSION_3 = os.getenv("STRING_SESSION_3", "")
    STRING_SESSION_4 = os.getenv("STRING_SESSION_4", "")
    STRING_SESSION_5 = os.getenv("STRING_SESSION_5", "")
    STRING_SESSION_6 = os.getenv("STRING_SESSION_6", "")
    STRING_SESSION_7 = os.getenv("STRING_SESSION_7", "")
    STRING_SESSION_8 = os.getenv("STRING_SESSION_8", "")
    STRING_SESSION_9 = os.getenv("STRING_SESSION_9", "")
    STRING_SESSION_10 = os.getenv("STRING_SESSION_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb+srv://itzking:<password>@cluster0.4k07byk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "5874405107"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "")
    HELP_PIC = os. getenv("HELP_PIC", "")
    START_PIC = os. getenv("START_PIC", "")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", ".")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # CHANGE 'True' TO 'False' IF YOU WANNA DISABLE PORN
