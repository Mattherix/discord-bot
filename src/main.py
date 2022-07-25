from nextcord import Client

import logging

from src.utils import Utils

bot = Client()
TESTING_GUILD_ID = 1000483684262084679


def logger(filename: str):
    logger = logging.getLogger('nextcord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename=filename, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

if __name__ == '__main__':
    logger('../discord.log')

    bot.add_cog(Utils(bot))
    bot.run('MTAwMDQ4ODU1MTM1MzQzMDEwNw.GX6EjI.I0iZX-6icz50mxdjGc-H_33E0WD0_2QTbA_PPI')
