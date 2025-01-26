from urllib.request import urlopen

# URLからレスポンスを取得
url = "https://eiger-inc.co.jp/"
response = urlopen(url)

# 1. response自体を確認
print(type(response))  # <class 'http.client.HTTPResponse'>

# 2. レスポンス本文を取得（バイト列）
contents = response.read()
print(type(contents))  # <class 'bytes'>

# 3. バイト列をデコードして文字列に変換
text = contents.decode("utf-8")
print(type(text))  # <class 'str'>
