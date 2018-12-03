#!usr/bin/env python3
from wxpy import *

if __name__ == "__main__":
    bot = Bot()
    friend = bot.friends().search('')[0]
    friend.send('哈哈哈哈')
    print(friend)
