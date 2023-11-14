# ada-2023-project-miaoumiaou

# Left click, Right click : A Safari Through Wikispeedia's Political Jungle

### README (1000 WORDS)


#### ABSTRACT (122  / max 150)
 
Today, Wikipedia is part of everybody's life. It is the first source that most people will check when they want to get information on something. This website is maintained by volunteers through open collaboration, and what makes its strength, can also bring problems. Wikipedia aims to have a neutral point of view and stay strictly factual but can we garantee this when anyone can become a contributor ? This study aims to examine the political bias within Wikipedia and its potential impact on Wikispeedia players, a game where participants try to navigate to a specific article solely using hyperlinks within the current article. (Wikispeedia will also allow us to investigate whether players tend to associate biased articles with positive or more negative attributes.)

https://dl.acm.org/doi/pdf/10.1145/3041021.3053375


#### RESEARCH QUESTIONS 
The research questions we will look into fall into 2 distinct categories. First, we'll take a look at the way articles are written, and then we want to study articles about political people and how their personal political alignments. 

- Is there a political bias in the way wikipedia articles are written ?
    - Do people tend to associate these biases in a positive or negative manner ?

- If there is a bias, does it affect the way people play wikispeedia ?  
    - Does it take them more time if they go through biased articles ?
    - Does it impact the success rate ? (more or less finished paths)
    - Are there more backclicks depending on the biases of the preceeding articles ?
    - ..?

Then, we will look at the subset of articles about Political People. On these articles, we want to look at the impact of their political views and run the same analysis as before.

- Do people tend to associate these political people in a positive or negative manner ?

- Do the political alignment of people affect the way people play wikispeedia ?
    - Does it take them more or less time, does it impact the success rate, affect the number of backclicks ?




#### DATASETS
Our main dataset is the Wikispeedia dataset. It contains the 4600 articles used in the Wikispeedia game, as well as data from users' games, including finished and unfinished paths taken, time taken for each path, categorization of articles and more.
In order to classify the articles in our main dataset, we need training data to fit our model. 
We'll use two alternatives websites to Wikipedia : RationalWiki for content with a left-leaning perspective and Infogalactic for right-leaning articles, acknowledging that both are recognized for their respective biases. This data will allow us to train our model in a supervised way.

(https://mediabiasfactcheck.com/conservapedia/)

https://mediabiasfactcheck.com/infogalactic/
https://mediabiasfactcheck.com/rationalwiki/



#### METHOD
- Classifying articles
The first part of the project will consist in classifying the articles we have considering their biases. Using our 
biased websites, we will train a Support Vector Machine model (SVM) to classify the articles on Wikispeedia.
    - Data collection and preprocessing
Using a data scraping script, we create a dataframe containing the plain text and title of 3000 random articles of both Infogalactic and Rationalwiki. We then clean the data, removing stopwords and tokenize the texts. 
    - Training model 
We then split our data in a split and train set and train our model. 




About the part of the project about political people, we needed to classify the political alignement of the person itself and that is much harder to do with a natural language processing script, as it will be influenced by the way the text is written rather than the life and opinion of the presented person. After trying to classify them using different techniques (using kmeans or the same SVM model as before), we realized the only way to get meaningful results was to classify them by hand. As the data consists of only about 60 people, it made sense to do it manually. 


- Analysis


??? 

Confounding factors ???



#### PROPOSED TIMELINE


17th of November : Project Milestone 2 Deadline
- Pre-processing of data, initial analyses
...
(17.11-01.12 : HW2)
... 
1st December :
8th of December : 
15th of December :
22nd of December : Final Project deliverable


#### Organization within the team 

Wassim Maj : Overview of Readme, 
Via : Data collection from websites, 
Jeremy  : Data collection from websites, 
Matthieu : Classification of political people, ..
Adrien Joliat : Implimenting ML model, 



Sources 

