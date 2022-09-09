
from email.mime import image
from selectors import EpollSelector
from weakref import WeakValueDictionary
import requests, json, webbrowser
url = "https://holidays-jp.github.io/api/v1/date.json"
res = requests.get(url)
data = json.loads(res.content)
url2 = "https://yesno.wtf/api"
res2 = requests.get(url2)
data2 = res2.json()
#webbrowser.open(data2["image"])
c = {s: z for z, s in data.items()}
#for v , i in enumerate(data):
 #   print(v, i)
while True:
    pref = input('祝日を入力:')
    if pref in c:
        d = c[pref]
        print(d)
    else:
        break
    if (res := input('他の祝日を見ますか y/n') =='n'):
        break
    
