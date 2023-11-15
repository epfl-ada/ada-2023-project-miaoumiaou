import pandas as pd
import tarfile
import gzip
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.parse
import requests
from bs4 import BeautifulSoup 
import os
from Functions import *

def download_extract_data():
    directory_path = "./data"

    # Vérifiez si le répertoire existe déjà
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print("Repository data created")
    else:
        print("Repository data already exist")


    urls=["https://snap.stanford.edu/data/wikispeedia/wikispeedia_paths-and-graph.tar.gz",
        "https://snap.stanford.edu/data/wikispeedia/wikispeedia_articles_plaintext.tar.gz"]
        #,"https://snap.stanford.edu/data/wikispeedia/wikispeedia_articles_html.tar.gz"]
        #Le dernier lien contient tous les codes htm de tous les articles wikispeedia (très lourd et jsp si on va utiliser ?)

    for url in urls:    
        response=requests.get(url)
        if response.status_code==200: #Verify that the response is True
            save_path="./data/"+url[43:]
            with open(save_path,"wb")as f:
                f.write(response.content)
                print(save_path+" downloaded")

    PATH=["./data/wikispeedia_paths-and-graph.tar.gz",
        "./data/wikispeedia_articles_plaintext.tar.gz"]

    DEST=["./data/wikispeedia_paths-and-graph",
        "./data/wikispeedia_articles_plaintext"]

    for i,path in enumerate(PATH):
        with tarfile.open(path,"r:gz") as fichier:
            fichiers_names=fichier.getnames()
            for name in fichiers_names:
                fichier.extract(name, DEST[i])
            
    for path in PATH:
        os.remove(path)


def load_plain_article():
    text_file_dir="./data/wikispeedia_articles_plaintext/plaintext_articles/"
    file_data=[]

    for filename in os.listdir(text_file_dir):
        with open(os.path.join(text_file_dir, filename), "r") as file:
            content = file.read()
        
            # Split the content into lines to remove the header
        lines = content.split('\n')

        #Removing the header (line 0)
        if lines:
            lines.pop(0)

        # Making it an array and removing all \n
        content = '\n'.join(lines)
        content = content.replace("\n", " ")

        filename_fin=filename[:-4]
        new_file_content= {"text_content": content, "title": urllib.parse.unquote(filename_fin , encoding = 'utf-8')}
        
        file_data.append(new_file_content)

    test_data = pd.DataFrame(file_data)
    return test_data