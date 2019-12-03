#!/usr/bin/python
import sys
from bs4 import BeautifulSoup
import requests

if len(sys.argv)<2:
    print("pass a github user link as an argument")
    exit()
pr_link="https://thepiratebay.org/torrent/7349696/The_Matrix_Revolutions_(1999)_1080p_BrRip_x264_-_1.85GB_-_YIFY"
link=sys.argv[1]+"?tab=repositories"

res=requests.get(link)

soup = BeautifulSoup(res.text, 'html.parser')

repo_ul=soup.find(id="user-repositories-list").find_all('li')

for repo_li in repo_ul:
    print(repo_li.find('a').get('href'))