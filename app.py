import os
import threading
from flask import Flask
from pyrogram import Client, filters

# ✅ Environment se API config le lo
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# ✅ Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Telegram Bot is Running!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# ✅ Pyrogram Client
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
def start_handler(client, message):
    message.reply_text("Bot is working, bhai!")

# ✅ Run both Flask and Bot
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run()
