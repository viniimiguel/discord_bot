import discord
from discord.ext import commands
import time
import random
import jogoForca

class Discord_bot():
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True

        self.bot = commands.Bot(command_prefix="$", intents=self.intents)

        self.discord_token = ""
    


    def main(self):
        @self.bot.event
        async def on_ready():
            print(self.bot.guilds)
            print("O bot foi iniciado")
            print("#" * 20)

        @self.bot.command(name="forca")
        async def get_forca(ctx):
            forca = jogoForca.Forca()

            forca.add_words()
            forca.game_define()

            await ctx.send(f"o jogo da forca foi iniciado voce tem 6 chances!")

            
            

        self.bot.run(self.discord_token)

if __name__ == '__main__':
    discord_bot = Discord_bot()
    discord_bot.main()

    





