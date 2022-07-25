import logging
import os

from dotenv import load_dotenv
from nextcord import Client

from src.utils import Utils

bot = Client()
TESTING_GUILD_ID = 1000483684262084679


def logger(filename: str):
    logger = logging.getLogger('nextcord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename=filename, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


def main() -> None:
    logger('discord.log')

    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

    bot.add_cog(Utils(bot))
    bot.run(DISCORD_TOKEN)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


if __name__ == '__main__':
    main()
