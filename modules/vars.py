import os

API_ID    = os.environ.get("API_ID", "22215080")
API_HASH  = os.environ.get("API_HASH", "6ab80ad5d78fee18fdd9b909edfbafd5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8146589575:AAHJF63wom5wwtaugVWqAxMeeaiqrYZsy1s") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
