#cspell: ignore downloadxkcd elams xkcd
#downloadxkcd
import requests,bs4,os

url = "https://xkcd.com"
os.makedirs("xkcd",exist_ok = True)

# while not url.endswith("#"):
for i in range(5):
  #ページのダウンロード
  print(f"ページをダウンロード中{url}...")
  res = requests.get(url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text,"lxml")

  #コミック画像を検索
  elams = soup.select("#comic img")
  if elams == []:
    print("対象が見つかりませんでした。")
  else:
    comic_url = "https:" + elams[0].get("src")

    #画像をダウンロード
    print(f"画像をダウンロード中...:対象URL:{comic_url}")
    res = requests.get(comic_url)
    res.raise_for_status()

    #画像をハードウェアに保存
    file = open(os.path.join("xkcd",os.path.basename(comic_url)),"wb")
    for i in res.iter_content(100000):
      file.write(i)
file.close()
print("ダウンロードが完了しました")