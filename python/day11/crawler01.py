# crawler.py
from bs4 import BeautifulSoup

html_doc = """
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>joneconsulting/python</title>
  </head>
  <body class="logged-in env-production">
  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>
    <header class="Header  f5" role="banner">
    <p class="d-flex flex-justify-between px-3 container-lg">
  </div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.find_all('a'))
# print(soup.get_text())
