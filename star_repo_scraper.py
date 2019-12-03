#!/usr/bin/python
import sys
from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, link):
        self.link=link
        self.repos=[]

    def GetRepos(self, link):
        result=requests.get(link)
        soup = BeautifulSoup(result.text, 'html.parser')
        next_button=list(soup.find('div', {"data-test-selector": "pagination"}).descendants)[2]
        is_last_page=False if next_button.name=="a" else True

        repo_divs=soup.find_all('div', {"class":"col-12 d-block width-full py-4 border-bottom"})

        for repo_div in repo_divs:
            self.repos.append(str(repo_div.div.h3.a.get("href")))
        return is_last_page, next_button

    def ScrapeRepos(self):
        is_last_page, next_button=self.GetRepos(self.link)

        while not is_last_page:
            next_page=next_button.get("href")
            is_last_page, next_button=self.GetRepos(next_page)

        return self.repos

