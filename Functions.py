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
import plotly
import plotly.express as px
import plotly.graph_objects as go
from math import pi
from plotly.subplots import make_subplots
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import ttest_1samp
from scipy.stats import chi2_contingency
import plotly.figure_factory as ff
from collections import Counter

def download_extract_data():
    directory_path = "./data"

    # Vérifiez si le répertoire existe déjà
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print("Repository data created")
    else:
        print("Repository data already exist")

    if os.path.exists("./data/wikispeedia_articles_plaintext"):
        return 1
        
         
    urls=["https://snap.stanford.edu/data/wikispeedia/wikispeedia_paths-and-graph.tar.gz",
        "https://snap.stanford.edu/data/wikispeedia/wikispeedia_articles_plaintext.tar.gz"]

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
    return 0

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


# Function to convert bias labels to numbers, calculate averages, and then convert back to categorical bias
def calculate_path_biases(path, all_articles_df):
    # Define a mapping from categorical bias to numerical values
    bias_mapping = {
    'left': -1,
    'center': 0,
    'right': 1
    }

    articles = path.split(';')  # Adjust delimiter if needed
    biases = all_articles_df[all_articles_df['article'].isin(articles)]['Bias']
    
    # Map the categorical biases to numerical values
    numerical_biases = biases.map(bias_mapping)
    
    # Calculate the average numerical bias
    average_numerical_bias = numerical_biases.mean()
    # Get the bias of the start article, assuming the first article in the list
    start_numerical_bias = numerical_biases.iloc[0] if len(numerical_biases) > 0 else None
    #Get the bias of the end article, assuming the last article in the list
    end_numerical_bias = numerical_biases.iloc[-1] if len(numerical_biases) > 0 else None

    # Convert the average numerical bias back to a categorical bias
    average_bias_label = numerical_to_categorical_bias(average_numerical_bias)
    
    # Convert the start numerical bias back to a categorical bias if necessary
    start_bias_label = numerical_to_categorical_bias(start_numerical_bias) if start_numerical_bias is not None else None
    #Convert the end numerical bias back to a categorical bias if necessary
    end_bias_label = numerical_to_categorical_bias(end_numerical_bias) if end_numerical_bias is not None else None

    return average_numerical_bias, average_bias_label, start_bias_label, end_bias_label

# Helper function to convert numerical bias back to categorical
def numerical_to_categorical_bias(numerical_bias):
    if numerical_bias < -1/3:
        return 'left'
    elif -1/3 <= numerical_bias <= 1/3:
        return 'center'
    else:
        return 'right'
    

    # Function to create histograms with colored bias zones
def create_colored_histogram(df, title):
    # Initialize figure
    fig = go.Figure()

    # Define colors for bias zones
    colors = {
        'left': 'lightcoral', 
        'center': 'lightgray',  
        'right': 'lightblue'  
    }

    # Add histogram for each bias zone with specific color
    for label, color in colors.items():
        # Filter the dataframe for the specific bias zone
        zone_df = df[(df['average_numerical_bias'] > -1/3 if label != 'left' else df['average_numerical_bias'] <= -1/3) &
                     (df['average_numerical_bias'] <= 1/3 if label != 'right' else df['average_numerical_bias'] > 1/3)]
        # Add trace for the zone
        fig.add_trace(go.Histogram(x=zone_df['average_numerical_bias'], name=label.capitalize(),
                                   marker_color=color, nbinsx=30, opacity=0.6))

    # Add vertical lines to demarcate the bias zones
    fig.add_vline(x=-1/3, line_width=2, line_dash="dash", line_color="grey")
    fig.add_vline(x=1/3, line_width=2, line_dash="dash", line_color="grey")

    # Update layout
    fig.update_layout(title=title, xaxis_title='Average Numerical Bias', yaxis_title='Count',
                      barmode='stack')

    # Add annotations for start and end counts in each zone
    for label, color in colors.items():
        start_count = df[df['start_bias_label'] == label].shape[0]
        end_count = df[df['end_bias_label'] == label].shape[0]
        # Place annotation in the middle top of the graph in their respective zone
        zone_center = {'left': 0.2, 'center': 0.5, 'right': 0.8}[label]
        fig.add_annotation(x=zone_center, y=1.02, text=f"Start: {start_count}<br>End: {end_count}",
                        showarrow=False, xref="paper", yref="paper", bgcolor=color, font=dict(color='black'),
                        align="center")
    return fig


# Define a function to assign color based on bias value
def get_color(value):
    colors = {
        'left': 'lightcoral', 
        'center': 'lightgray',  
        'right': 'lightblue'  
    }
    if value < -1/3:
        return colors['left']
    elif value > 1/3:
        return colors['right']
    else:
        return colors['center']
