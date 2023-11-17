#### ada-2023-project-miaoumiaou

# Blue click, Red click: Decoding the matrix behind the political bias of Wikispeedia


#### ABSTRACT 
 
Today, Wikipedia is part of everybody's life. It is the first source that most people will check when they want to get information. This website is maintained by volunteers through open collaboration, and what makes its strength, can also bring problems. Wikipedia aims to have a neutral point of view and stay strictly factual but can we garantee this when anyone can become a contributor ? (Das & Lavoie, 2016) observed that a large number of Wikipedia editors change their behaviour and focus on editing controversial topics when promoted to administrators, they might be biased (consciously or not) and influence these articles. 
Our study aims to examine the political bias within Wikipedia and its potential impact on Wikispeedia players, a game where participants try to navigate to a specific article solely using hyperlinks within the current article. This game  aims to characterize semantic distances between concepts (West et al., 2009). This will allow us to see if this semantic distance is influenced by bias.




#### RESEARCH QUESTIONS 
The research questions we will look into fall into 2 distinct categories. First, we'll take a look at the way articles are written, and then we want to study articles about political people and how their personal political alignments. 

- Is there a political bias in the way wikipedia articles are written ?
    - Do people tend to associate these biases in a positive or negative manner ?

- If there is a bias, does it affect the way people play wikispeedia ?  
    - Does it take them more time if they go through biased articles ?
    - Does it impact the success rate ? (more or less finished paths)
    - Are there more backclicks depending on the biases of the preceeding articles ?
    

Then, we will look at the subset of articles about Political People. On these articles, we want to look at the impact of their political views and run the same analysis as before.

- Do people tend to associate these political people in a positive or negative manner ?

- Do the political alignment of people affect the way people play Wikispeedia ?
    - Does it take them more or less time, does it impact the success rate, affect the number of backclicks ?
    




#### DATASETS
Our main dataset is the Wikispeedia dataset. It contains the 4604 articles used in the Wikispeedia game, as well as data from users' games, including finished and unfinished paths taken, time taken for each path, categorization of articles and more.
In order to classify the articles in our main dataset, we need training data to fit our model. 
We'll use two alternatives websites to Wikipedia : RationalWiki for content with a left-leaning perspective and Infogalactic for right-leaning articles, acknowledging that both are recognized for their respective biases. This data will allow us to train our model in a supervised way.


https://mediabiasfactcheck.com/infogalactic/ <br>
https://mediabiasfactcheck.com/rationalwiki/



#### METHOD
- Classifying articles <br>
The first part of the project consists in classifying the articles we have considering their biases. One of the factor of the bias in Wikipedia is the language style (Hube, 2017), and this is the one we will focus one for our classification. Using our biased websites, we will train a Support Vector Machine model (SVM) to classify the articles on Wikispeedia.
    - Data collection and preprocessing <br>
We have used web scraping technic in order to extract the text content of 3000 random articles exclusive to RationalWiki (serves as a left leaning version of Wikipedia) and Infogalactic (serves as a right-leaning version of Wikipedia) to train our NLP model. 
Additionnaly we have found 608 articles that are common to RationalWiki, Infogalactic and Wikispeedia dataset. This will offer another type of analysis to find the bias in wikispeedia articles text. These files are stored to csv and used as dataframe containing the plain text and title of each articles. 
For more details about how we extracted the data, the code is available in the notebook called scraped_data/data_from_the_web.ipynb
We then clean the data, by removing stopwords and tokenizing the texts. 
    - Training model <br>
We then split our data in a split and train set and train our model. 




About the part of the project about political people, we needed to classify the political alignement of the person itself and that is much harder to do with a natural language processing script, as it will be influenced by the way the text is written rather than the life and opinion of the presented person. After trying to classify them using different techniques (using kmeans or the same SVM model as before), we realized the only way to get meaningful results was to classify them by hand. As the data consists of only about 60 people, it made sense to do it manually. 


-  Analyses <br>
Impact of Bias on Wikispeedia Gameplay <br>
Linear Regression: To correlate article bias with navigation time.
Logistic Regression: For analyzing success rates as binary outcomes.
Correlation Analysis: Pearson or Spearman methods to study relationships between article bias and gameplay metrics like backclicks. <br>
Analysis of Articles on Political Figures <br>
Comparative Statistical Tests: T-tests for comparing different political groupings.
Chi-Square Test: To examine associations in categorical data like path choices. <br>
General Methodological Approaches <br>
Multivariate Analysis: Multiple regression or ANOVA for analyzing multiple variables.
Time-Series Analysis: For identifying trends in data over time
Propensity score matching to found Confounding factors
 


#### PROPOSED TIMELINE


17th of November : Project Milestone 2 Deadline <br>
    - Pre-processing of data, initial analyses <br>
1st December : First analyses <br>
8th of December : Analysis and Visualisation <br>
15th of December : Start of redaction of data story and website design <br>
22nd of December : Final Project deliverable  <br>


#### Organization within the team 

Wassim Maj : Redaction of Readme, Graphs, Redaction of Data Story<br>
Viacheslav Bolotnikov : Data collection from websites, Analyses<br>
Jeremy Dahan : Data collection from websites, Redaction of Data Story<br>
Matthieu Jacques : Classification of political people, Graphs<br>
Adrien Joliat : Implimenting ML model, Website Design<br>



Sources 

[1] Das, S., Lavoie, A., & Magdon-Ismail, M. (2016). Manipulation among the arbiters of collective intelligence: How Wikipedia administrators mold public opinion. ACM Transactions on the Web (TWEB), 10(4), 1-25.


Hube, C. (2017, April). Bias in wikipedia. In Proceedings of the 26th International Conference on World Wide Web Companion (pp. 717-721).
[2]

West, R., Pineau, J., & Precup, D. (2009, June). Wikispeedia: An online game for inferring semantic distances between concepts. In Twenty-First International Joint Conference on Artificial Intelligence.
[3]
