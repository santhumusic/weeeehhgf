from pyrogram impor Client, filters

bot = Client(
    ":spambot:",
    API_ID,
    API_HASH,
    session_string=STRING_SESSION,
    in_memory=True, 
    plugins=dict(root="spam")
) 
