# Introduction
**A Telegram Bot to force users to join a specific channel before sending messages in a group.**
- Find it on Telegram as [Force Subscribe](https://t.me/ForceSubscribeEN_bot)

## Todo
- [ ] Add multiple channels support
- [X] Configure different groups with different channels
- [X] Clean messages after completion
- [ ] LOGGER support.

## Deploy

### Installation
- Clone this repo
```
git clone https://github.com/tldr-cell/force-subscribe-telegram-bot
```
- Change directory
```
cd force-subscribe-telegram-bot
```
- Install requirements
```
pip3 install -r requirements.txt
```

### Configuration
Add [APP_ID](https://my.telegram.org/apps), [API_HASH](https://my.telegram.org/apps), [BOT_TOKEN](https://t.me/botfather) in [Config.py](Config.py) or in Environment Variables.

### Deploying
- Run bot.py
```
python3 bot.py
```

## Thanks to
- [Viper Adnan](https://github.com/viperadnan-git) for original repo
- [PyroGram](https://PyroGram.org)
- [Hasibul Kabir](https://GitHub.com/hasibulkabir) and [Spechide](https://GitHub.com/spechide) for helping.