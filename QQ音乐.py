










            f.write(songContent)
            print("下载完毕")
        # print(jsonData)
        # print(purl)
        jsonData = res.json()
        p_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data = {"req": {"param": {"guid": "8182077584"}},"req_0": {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey","param": {"guid": "8182077584", "songmid": ["%s"], "uin": "7945"}},"comm": {"uin": 7945}}' % songmid
        path = songname + '.mp3'
        purl = jsonData["req_0"]["data"]["midurlinfo"][0]["purl"]
        res = requests.get(url=p_url, headers=headers)
        song_info_li.append((songmid, songname))
        song_url = 'http://isure.stream.qmusic.qq.com/' + purl
        songContent = requests.get(url=song_url, headers=headers).content
        songmid = song_info["songmid"]
        songmid = song_info[0]
        songname = song_info["songname"]
        songname = song_info[1]
        with open(path, 'wb') as f:
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win32; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/76.0.3809.100 Safari/537.36"}
    # print(html)
    # 想要获取songmid-->1.正则匹配 2.截取->转为字典
    # 注意 此处通过postman返回并不是json的
    # 注意list下为列表格式
    # 获取songmidb
    for song_info in song_info_list:
    for song_info in song_li:
    html = html[9:-1]
    html = res.text
    print(type(html))
    res = requests.get(url=url, headers=headers)
    return song_info_li
    searchword = input("请输入想要搜索的歌曲:")
    song_info_li = []
    song_li = songdata["data"]["song"]["list"]
    songdata = json.loads(html)
    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=1&w=%s" % searchword
# -*- coding: utf-8 -*-
# @Author  : Amy
# @File    : QQ音乐.py
# @Time    : 2020/7/9 13:58
def getPurl(song_info_list):
def getSongMid():
getPurl(song_info_list)
headers = {
import json
import requests
song_info_list = getSongMid()