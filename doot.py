import asyncio
import discord
from discord.ext import commands

from secret import token

AUDIO = "song.mp3"
CHANNEL = "Doot Land"
NO_CHANNEL = "There is no **{}** voice channel. Make one and try again."

bot = commands.Bot(
    command_prefix="?",
    help_command=None,
    activity=discord.Game("DOOTING"),
    intents=discord.Intents.all())


class Doot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = None

    @commands.command()
    async def play(self, ctx):
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=CHANNEL)
        if not voiceChannel:
            await ctx.send(NO_CHANNEL.format(CHANNEL))
            return

        try:
            self.vc = await voiceChannel.connect()
            self.vc.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=AUDIO), after=lambda e: self.repeat())
        except:
            return

    def repeat(self):
        self.vc.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=AUDIO), after=lambda e: self.repeat())

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def leave(self, ctx):
        await self.vc.disconnect()


async def main():
    async with bot:
        await bot.add_cog(Doot(bot))
        await bot.start(token)

asyncio.run(main())
