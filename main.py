import os

LINE = "v2.9.1: fixed a bug where the brain woke the host at 3am to rehearse a conversation from 2011 that never happened."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)