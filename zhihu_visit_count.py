import requests
import re
import pandas as pd

file_path = r'zhihu_topics.xlsx'
df = pd.read_excel(file_path, sheet_name = 'Sheet1')

headers = {
    'Cookie':'__snaker__id=FPQWBOQnZTNMXmHh; SESSIONID=iWJYoLR04jLwh69rMjs7cJeNxMlWBSketv5ZPLGg3r4; JOID=UlwcAEmKsBuDNN6rCYmWAJTg-icZrZ4yoRX5hSCrlzWqFv-MJ7lnc-cy16wCZ5FcA9IfqqdvDLzGge7pSm3-tKc=; osd=VV8dAkuNsxqBNtmoCIuUB5fh-CUerp8woxL6hCKpkDarFP2LJLhlceAx1q4AYJJdAdAYqaZtDrvFgOzrTW7_tqU=; _xsrf=rGu7z1Sc6Lg70V6xQ8odbhi6clGGq8cO; _zap=a70a73bb-2a9c-4dbe-b973-2ba43ab2ea29; d_c0=ASDSc9wnihmPTkBZde5oMn44pw8OSjN3rFs=|1731548202; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1733203739,1733475096,1734415189; HMACCOUNT=3FCF7CE530FF0A2C; q_c1=a943948953a140c4926304e1423cf678|1734427293000|1734427293000; tst=r; __zse_ck=004_EwPxSc5cEn7vVJXa=ul8Ozx2uM/xR01WDvuqZ2hhnxK=Avl8ihSNxSj9cLRKOjlemUF49bT/R8ivrpgW8Kb4hBRjCL9dtPfgsuO6og=bDmU/DLK9fIUHnQwVljo7jWEC-eoA3BHQVdRYf26enu0n0eEWYEi5CeNTfjLTomm6kFsbJNUwMowgBURdR1o6tphCJjs9G3nXhsWEgFYsErA+DVb/ahpMPFssOefVdeODzfNTVtMV1Jmzz65Ce+HG/ShRz; gdxidpyhxdE=7VEcGKMcQ27aAosTW%5Cu4VP1%2BeqEUgdJXNncyrnt6Lxu4IS2Uh79tL1pAwHi%2By7zaQYGmc9r7Yj9c%5CKN%2FpxONwKp6%2FlaJiQgzd0mXL6PtJVcsGalVZtn%5ChVZ3SIQrXWuMskwHqBBw%5CfRYv6flW5BTxguVUwAaqEBeoap1uwL9p81lJRcX%3A1734595430891; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1734594617; BEC=5ee33e0856ed13c879689106c041a08d; captcha_session_v2=2|1:0|10:1734594617|18:captcha_session_v2|88:b0ZHVDlCd1o3RDlZYnBWY1djaW1pMjcxV3lWQjl6aG5mVWRIUk01L3ZLKzk4OWh3Y01XeDNpMTdnZHBZcmhhYQ==|0dd0dd62150152e4e84888ccd89b3766e595e16dae7560361442faffbf79527c',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

for url in df['url']:
    url = url
    res = requests.get(url, headers = headers)
    # print(res.text)
    visit_count = re.search(r'"visitCount":([^,]*),"commentCount"', res.text)
    # print(visit_count.group(1))
    if visit_count == None:
        print('转人工')
    else:
        print(visit_count.group(1))
    # print(visit_count)