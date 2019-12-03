import git
import os

def CreateDir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Couldn\'t create directory: %s' %  directory)

def Clone(repo):
    if os.path.exists("repos/"+repo.split("/")[1]):
        print("%s already exists" % repo)
        print("--------------------")
        return False
    try:
        git.Git("repos").clone("https://github.com/"+repo)
        print('cloned %s' % repo)
        err=False
    except:
        print("could not clone the repo: %s" % repo)
        err=True
    finally:
        print("--------------------")
        return err