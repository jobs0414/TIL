import webbrowser


keywords = ["아이유","수지","신소율"]
url = "https://search.naver.com/search.naver?query="


for name in keywords:
    webbrowser.open(url + name)
