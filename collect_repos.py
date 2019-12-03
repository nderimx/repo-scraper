from gitter import *
from star_repo_scraper import Scraper
import sys

if len(sys.argv)<2:
    print("pass a github user link as an argument")
    exit()
link="https://github.com/"+sys.argv[1]+"?tab=stars"
err_count=0

scraper=Scraper(link)
repos=scraper.ScrapeRepos()


print(repos)
print(len(repos))

CreateDir("repos")

for repo in repos:
    err=Clone(repo)
    if err:
        err_count+=1

