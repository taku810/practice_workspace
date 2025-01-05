# #cspell:ignore responce Romjul
import requests
import time

url = "https://automatetheboringstuff.com/files/rj.txt"
res = requests.get(url)
# res.raise_for_status()

# starttime = time.time()
# play = open("Rj.txt","wb")
# for chunk in res.iter_content(100000):
#     play.write(chunk)
# endtime = time.time()
# print("実行時間:", endtime-starttime)

try:
    res.raise_for_status() == 200
    print("接続成功")
    time.sleep(1)#一秒待機

    starttime = time.time()
    with open("romjul.txt","wb") as play:
        for i in res.iter_content(100):
            play.write(i)

    endtime = time.time()
    print("実行時間:",endtime - starttime)

except Exception as error:
    print("接続失敗:errormessage:",error)