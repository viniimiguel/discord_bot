import discord
from discord.ext import commands
import youtube_dl

class Discord_bot():
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True

        self.bot = commands.Bot(command_prefix='/', intents=self.intents)

        self.discord_token = ''

    def main(self):
        @self.bot.command()
        async def inverse(ctx, message):
            await ctx.send(message[::-1])
        self.bot.run(self.discord_token)

        

if __name__ == '__main__':
    discord_bot = Discord_bot()
    discord_bot.main()