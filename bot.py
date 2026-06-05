import os
from telethon import TelegramClient, events

# መለያ ቁጥሮችዎን ከሲስተሙ ውስጥ ያነባል
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

client = TelegramClient('session_name', api_id, api_hash)

# የሚላከው ፅሁፍ እና ሊንክ (እዚህ ጋር መቀየር ይችላሉ)
REPLY_MESSAGE = """
ሰላም! መልዕክትዎ ደርሶኛል። በአሁኑ ሰዓት መስመር ላይ ስላልሆንኩ ስመለስ አወራዎታለሁ።

እስከዚያው ይህንን ሊንክ ይጫኑ፦ https://example.com
"""

@client.on(events.NewMessage(incoming=True, private=True))
async def handler(event):
    # መልዕክት የላከው ሰው እርስዎ ራስዎ ካልሆኑ ብቻ ምላሽ ይሰጣል
    if not event.is_private or event.sender_id == (await client.get_me()).id:
        return
    await event.reply(REPLY_MESSAGE)

print("አውቶማቲክ መልስ ሰጪው ስራ ጀምሯል...")
client.start()
client.run_until_disconnected()
