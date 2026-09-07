# doot-bot

This is a Discord bot written in Python that joins a voice channel and loops the doot music forever. That is
the whole bot. Commands start with `?`.

![](https://github.com/1nderr/doot-bot/blob/main/doot.png?raw=true)

## Features

### Doot

`?play` joins the voice channel named `Doot Land` and starts playing `song.mp3` through ffmpeg. When the
song ends it starts it over again, so it never stops on its own. If there is no channel with that name, the
bot says so and tells you to make one.

The `song.mp3` in this repo is based on
[this YouTube playlist](https://www.youtube.com/watch?v=WzFXaEYPE10&list=PLelh_z0pMOn-J5ZReYaR_UVOyoDJUT3HR).

### Leaving

`?leave` disconnects the bot from the voice channel. This command is admin only, because otherwise it would
stop dooting.

Note: The voice channel name is hardcoded at the top of `doot.py`, so change `CHANNEL` if your channel is
called something else.

## Setup

This bot requires a file named `secret.py` in the root folder with the following content:

```
token = "PASTE_YOUR_BOT_TOKEN_HERE"
```

The bot needs to be able to see voice channels and connect to them, so it uses all intents.

## Dependencies

- `python 3.12`
- `ffmpeg` at `/usr/bin/ffmpeg`

### Python Dependencies

- `discord.py`
- `PyNaCl`

To use the `requirements.txt` file, just run `pip3 install -r requirements.txt`.

Note: `PyNaCl` is what discord.py uses for voice, so the bot will not connect without it. The Dockerfile
installs `ffmpeg` itself, so you only need it on the machine if you are running the bot outside of Docker.

## Build

`docker build -t dootbot .`

## Run

`docker run --rm -d dootbot`
