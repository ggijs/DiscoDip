from discord import *
import logintoken as tokens

connection = discord.Discord(tokens.get_token())
connection.connect()