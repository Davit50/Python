import requests
from bs4 import BeautifulSoup as BS

#
r = requests.get("https://codeforces.com/ratings/country/Armenia")
html = BS(r.content, 'html.parser')

for el in html.select(".dark"):
    # title = el.select('a')
    print(el.text.strip())
    # print(el.text)

# s = requests.Session()
#
# # get CSRF
# auth_html = s.get("https://www.spoj.com/login")
# auth_bs = BS(auth_html.content, "html.parser")
# csrf = auth_bs.select("input[name=next_raw]")[0]['value']
# # login
# payload = {
#     # "YII_CSRF_TOKEN": csrf,
#     'returnUrl': '/',
#     "login_user": "Davit2006",
#     "password": "competitive010programmer",
#     "autologin": 1
#
# }
#
# answ = s.post("https://www.spoj.com/login/", data=payload)
# main = s.get("https://www.spoj.com/ranks/users/")
# answ_bs = BS(main.content, "html.parser")
#
# for el in answ_bs.select('.table-condensed > tr > td'):
#     print(el)


