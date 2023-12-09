import discord
from discord.ext import commands
import time
import random

class Discord_bot():
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True

        self.bot = commands.Bot(command_prefix="$", intents=self.intents)

        self.discord_token = "MTE3MjcwNzcyNjQ5Nzk0NzY3OA.G8BuLc.5CMFySkvNHDVEo_iHMMjw5BZJ1UG_ObASs_5sY"
    


    def main(self):
        @self.bot.event
        async def on_ready():
            print(self.bot.guilds)
            print("O bot foi iniciado")
            print("#" * 20)

        @self.bot.command(name="forca")
        async def get_forca(ctx):
            print("hello world")
            

        self.bot.run(self.discord_token)

if __name__ == '__main__':
    discord_bot = Discord_bot()
    discord_bot.main()

    





