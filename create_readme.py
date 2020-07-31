#  出力ファイル形式:Markdown
#  要 pip install requests, pip install beautifulsoup4
#  なんか要らない気がしたのでupdateは未実装。必要そうなら作る

import os
import re
import json
import requests
import bs4

os.chdir(os.path.dirname(os.path.abspath(__file__)))

dictjson = "urldict.json"

dirname = ".提出一覧"

dirname2 = "E:\ぷろぐらむ\競プロ"

if os.path.isfile(dictjson):
    with open(dictjson, mode="r") as f:
        urldict = json.load(f)
else:
    urldict = {}

def createatcoder(url, m, home, page):
    taskurl = home + "/contests/" + m[3] + "/tasks"
    get_taskurl_info = requests.get(taskurl)
    bs4Obj = bs4.BeautifulSoup(get_taskurl_info.text, 'html.parser')
    contesttitle = bs4Obj.find(class_="contest-title").text
    conid = re.match(".*?([\d]+)", contesttitle)

    if re.match(".*?AtCoder Beginner", contesttitle):
        urldict[m[3]] = "ABC" + conid[1]
        contesttitle = "ABC" + conid[1]
    elif re.match(".*?AtCoder Regular", contesttitle):
        urldict[m[3]] = "ARC" + conid[1]
        contesttitle = "ARC" + conid[1]
    elif re.match(".*?AtCoder Grand", contesttitle):
        urldict[m[3]] = "AGC" + conid[1]
        contesttitle = "AGC" + conid[1]
    else:
        urldict[m[3]] = contesttitle

    tbody = bs4Obj.tbody

    tr = tbody.find_all("tr")

    tasks = {}
    urls = {}

    for i in range(len(tr)):
        txt = tr[i].text
        s = txt.splitlines()
        tasks[s[1]] = s[2]

        link = tr[i].find("a")
        url = link.get("href")
        urls[s[1]] = url

    res = ""

    #  title
    res += "# {0} {1}  \n\n".format(page, contesttitle)

    #  top page
    res += "## [TOP]({0})  \n\n".format(home + "/contests/" + m[3])

    for obj in tasks:
        res += "[{0} {1}]({2})   \n".format(obj, tasks[obj], home+urls[obj])
        res += "[]({0})  \n\n".format(home + "/contests/" + m[3] + "/submissions/")

    updir = "./{0}/{1}/{2}".format(dirname, page, contesttitle)
    if not os.path.isdir(updir):
        os.makedirs(updir)

    updir2 = "{0}/atcoder/{1}".format(dirname2, contesttitle)

    if not os.path.isdir(updir2):
        os.makedirs(updir2)

    create = False

    upfile = updir + "/readme.md"
    if not os.path.isfile(upfile):
        create = True
        with open(upfile, mode="w") as f:
            f.write(res)

    if create:
        print("create:" + contesttitle)
    else:
        print("already created:" + contesttitle)

def updateatcoder():
    pass

def main():


    if get_url_info.status_code != 404 and get_url_info.status_code != 403:
        m = re.match(r"https?://([\w]+.[\w]+)/([\w-]+)/([\w-]+)/?([\w-]*)", url)
        home = re.match(r"https?://([\w]+.[\w]+)", url).group()
        if m[1] == "atcoder.jp":
            if m[2] == "contests":
                if not m[3] in urldict:
                    #  create readme.md
                    createatcoder(url, m, home, "AtCoder")

                if m[4] != "":
                    if m[4].isdecimal():
                        #  update readme.md
                        updateatcoder()


        elif m[1] == "yukicoder.me":
            pass



        urldictjson = json.dumps(urldict)

        with open(dictjson, mode="w") as f:
            f.write(urldictjson)

    else:
        print("404 Error")


if __name__ == "__main__":
    print("URL:")
    url = input()

    get_url_info = requests.get(url)

    main()