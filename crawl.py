import os

folder = "../csc2005-lab02-2021/"
for file in os.listdir(folder):
    try:
        file = open(folder+file,"r")
        text =file.read()
        texts = text.split("\n")
        print(texts)

    except:
        print(file)
