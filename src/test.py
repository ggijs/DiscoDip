from discord import *
import tokenfile as tokens

connection = discord.Discord(tokens.get_token())
connection.connect()