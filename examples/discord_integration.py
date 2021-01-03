
# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2017-2019 TwitchIO

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from discord.ext import commands as discord_commands
from twitchio.ext import commands as commands


class DiscordCog(commands.Bot):

    def __init__(self, bot):
        # Discord bot instance
        self.discord_bot = bot
        self.bot = commands.Bot(irc_token='...', nick='...', prefix='!', initial_channels=['...'])

        # Start the Twitch Bot
        self.discord_bot.loop.create_task(self.bot.start())

        #Registering TwitchIO Command
        self.bot.command(name="test")(self.twitch_command)
        #Registering TwitchIO Event
        self.bot.listen("event_message")(self.event_message)

    # Discord.py event
    async def on_message(self, message):
        print(message.content)

    # TwitchIO event
    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Discord command
    @discord_commands.command(name='test')
    async def discord_command(self, ctx):
        await ctx.send('Hai there!')

    # TwitchIO command
    async def twitch_command(self, ctx):
        await ctx.send('Hai there!')


# Add the Discord cog as per usual
def setup(bot):
    bot.add_cog(DiscordCog(bot))
