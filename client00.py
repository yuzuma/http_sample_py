# LINE LIVE のページから、適切なchunklist.m3u8を出力をする

import requests
import re

from time import sleep
from datetime import datetime

# weather news
#URL = 'https://live.line.me/channels/659/broadcast/3055754'

# ann0
# URL = 'https://live.line.me/channels/231/broadcast/295248'

# test
URL = 'https://live.line.me/channels/231/upcoming/3290743'

now_time = datetime.now()

while True:
    current_time = datetime.now()
    # 5分経ったら、処理を抜ける
    if (current_time - now_time).total_seconds() > 60 * 5:
        break

    content = requests.get(URL).content.decode('UTF-8')

    p = re.compile('http://lss.line-cdn.net/p/live.+?chunklist.m3u8')

    matchResult = p.findall(content)
    if len(matchResult) > 0:
        # 高画質のURLに変換して、出力をする
        print(re.sub('/360/', '/720/', matchResult[-1]))
        break
    else :
        sleep(30)


