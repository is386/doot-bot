import asyncio
import discord
from discord.ext import commands

AUDIO = "song.mp3"
CHANNEL = "Doot Land"

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
        try:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=CHANNEL)
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
        await bot.start("")

asyncio.run(main())
