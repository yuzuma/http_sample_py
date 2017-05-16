# LINE LIVE のページから、適切なchunklist.m3u8を出力をする

import requests
import re

URL = 'https://live.line.me/channels/659/broadcast/3055754'

content = requests.get(URL).content.decode('UTF-8')

p = re.compile('http://lss.line-cdn.net/p/live.+?chunklist.m3u8')
matchResult = p.findall(content)


# 高画質のURLに変換して、出力をする
print(re.sub('/360/', '/720/', matchResult[-1]))

