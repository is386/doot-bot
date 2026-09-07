# Doot

This is a Discord bot written in Python that joins a voice channel and loops the doot music forever. That is
the whole bot. Commands start with `?`.

## Features

### Doot

`?play` joins the voice channel named `Doot Land` and starts playing `song.mp3` through ffmpeg. When the
song ends it starts it over again, so it never stops on its own.

### Leaving

`?leave` disconnects the bot from the voice channel. This command is admin only, because otherwise it would
stop dooting.

Note: The voice channel name is hardcoded at the top of `doot.py`, so change `CHANNEL` if your channel is
called something else. The bot silently does nothing if it cannot find the channel.

## Setup

The bot token goes in the `bot.start("")` call at the bottom of `doot.py`. Put the swap in the file before
you run it, and do not commit it.

The bot needs to be able to see voice channels and connect to them, so it uses all intents.

## Dependencies

- `python 3.8+`
- `ffmpeg` at `/usr/bin/ffmpeg`

### Python Dependencies

- `discord.py`
- `PyNaCl`

`PyNaCl` is what discord.py uses for voice, so the bot will not connect without it.

## Run

`python3 doot.py`
