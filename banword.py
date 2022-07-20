import os
import discord

DIR_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))
BAN_LIST = os.path.join(DIR_PATH,"Config","ban_list.txt")

def _getBannedWords():
    newlines = []
    # Check each line of file
    
    with open(BAN_LIST, "r") as file:
        for line in file:
            clean_line = line.rstrip().lower()
            newlines.append(clean_line)
    
    return newlines

BannedWords = _getBannedWords()

def _words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

async def CheckForWords(message, bot):
    if _words_in_string(BannedWords, message.content.lower()):
        emoji = discord.utils.get(bot.emojis, name="greenwithit")
        await message.add_reaction(emoji)