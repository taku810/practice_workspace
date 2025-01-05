#cspell:ignore youso
import requests
from bs4 import BeautifulSoup

# #明石高専のホームページのすべての画像を取得するコードを作成。

# url = "https://www.akashi.ac.jp/index.html"


# #HTMLを取得
# response = requests.get(url)
# if response.status_code == 200:
#     print("取得成功")
# else:
#     print(f"エラー:{response.status_code}")

# #HTMLのコードを表示（めちゃめちゃ長くなるので省略したほうが良い）
# html_content = response.text


# #HTMLをBSで解析(解析したものをsoupとして保存)
# soup = BeautifulSoup(html_content,"html.parser")

# #タイトルを取得
# page_title = soup.title.text
# print("page title:",page_title)


# #要素を抽出
# # first_paragraph = soup.find("a").img
# # print("first paragraph:",first_paragraph)

# image_youso = []
# all_links = soup.find_all("img")
# for i in all_links:
#     print(i.get("src"))

# #要素をダウンロード







#ここからは実際のニュースサイトでスクレイピングをしてみる
url = "https://news.ycombinator.com/"
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content,"html.parser")

page_title = soup.title.text
print("page title:",page_title)

all_titles = soup.find_all("td",class_="title")
for i in all_titles:
    print(i.get_text())




# #以下はAIが書いた実際のニュースサイトの記事の取得
# #(タイトル要素の抽出のHTMLタグの設定のところを手動で少し変更した)

# url = "https://news.ycombinator.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # タイトル要素の抽出
# titles = soup.find_all("td", class_="title")

# # タイトルの表示
# for i, title in enumerate(titles, start=1):
#     print(f"{i}: {title.text}")