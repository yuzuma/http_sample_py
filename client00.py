# LINE LIVE のページから、適切なchunklist.m3u8を出力をする

import requests
import re

# weather news
# URL = 'https://live.line.me/channels/659/broadcast/3055754'

# ann0
# URL = 'https://live.line.me/channels/231/broadcast/295248'

# test
URL = 'https://live.line.me/channels/851984/broadcast/3125601' 

content = requests.get(URL).content.decode('UTF-8')

p = re.compile('http://lss.line-cdn.net/p/live.+?chunklist.m3u8')
matchResult = p.findall(content)


# 高画質のURLに変換して、出力をする
print(re.sub('/360/', '/720/', matchResult[-1]))

