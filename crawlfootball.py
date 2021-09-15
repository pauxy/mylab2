import os

folder = "../csc2005-lab02-2021/"
for f in os.listdir(folder):
    try:
        file = open(folder+f,"r")
        text =file.read()
        texts = text.split("\n")
        link = texts[2].split("https://")[1].replace(".git","").replace("https://github.com/","")
        print(f+" : "+link)
    except:
        print(f)
