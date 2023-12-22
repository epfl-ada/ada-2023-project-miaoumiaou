#### ada-2023-project-miaoumiaou

# Blue click, Red click : Decoding the matrix behind the political bias of Wikispeedia


#### ABSTRACT 
 
Today, Wikipedia is part of everybody's life. It is the first source that most people will check when they want to get information. This website is maintained by volunteers through open collaboration, and what makes its strength, can also bring problems. Wikipedia aims to have a neutral point of view and stay strictly factual but can we garantee this when anyone can become a contributor ? (Das & Lavoie, 2016) observed that a large number of Wikipedia editors change their behaviour and focus on editing controversial topics when promoted to administrators, they might be biased (consciously or not) and influence these articles. 
Our study aims to examine the political bias within Wikipedia and its potential impact on Wikispeedia players, a game where participants try to navigate to a specific article solely using hyperlinks within the current article. This game  aims to characterize semantic distances between concepts (West et al., 2009). This will allow us to see if this semantic distance is influenced by bias.


#### RESEARCH QUESTIONS 
The research questions we will examine fall into two distinct categories.  
First, we'll take a look at how the articles are written, then we'll look at articles about political figures and their personal political positions.

- Is there a political bias in the way wikipedia articles are written ?
    - Are articles written more on a right or left biased way ?
    - Is there a difference between articles categories ?
    - Does a bias in the writting is correlated to a biased personnality (focus on the politicial people) ?

- If there is a bias, does it affect the way people play wikispeedia ?  
    - Does it take them more time if they go through biased articles ?
    - Does it impact the success rate ? (more or less finished paths)
    - Are there more backclicks depending on the biases of the preceeding articles ?
    - Does it affect the rating in the game ?
    - Does a biased article leads to another biased article based on the link between the articles ?

- What about the players ?
    - Do players tend to choose particulate start or finish pages ?
    - Do players tend to go more on right or left articles ?
    




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
We have used web scraping technic in order to extract the text content of 3000 random articles exclusive to RationalWiki (serves as a left leaning version of Wikipedia) and Infogalactic (serves as a right-leaning version of Wikipedia) to train our NLP model. These files are stored to csv and used as dataframe containing the plain text and title of each articles. 
For more details about how we extracted the data, the code is available in the notebook called scraped_data/data_from_the_web.ipynb
    - Training model <br>
Then a first cleaning of the text are applied in the NLP code/Clean.ipynb and after that, we use the NLP_final.ipynb to define the model. We split our data in a test and train set ( 10%/90% ) then we tokenize and vectorize using BERT and afterwards fit a SVM model to classify the Wikispeedia articles. The results are conclusive are the accuracy on the test set is 92.55%. 




About the part of the project about political people, we needed to classify the political alignement of the person itself and that is much harder to do with a natural language processing script, as it will be influenced by the way the text is written rather than the life and opinion of the presented person. After trying to classify them using different techniques (using kmeans or the same SVM model as before), we realized the only way to get meaningful results was to classify them by hand. As the data consists of only about 60 people, it made sense to do it manually. 


-  Analyses <br>
Global analyses on the entire dataset <br>
Analyses on the differences between the finished paths and the unfinished paths <br>
Analyses on the starting and ending pages <br>
Global analyses on the political people <br>
Correlation analyses on political people between the bias of their article and their political affiliation <br>
Politication affiliation distribution of the political people <br>
Political bias repartion <br>
Political analyses by article type and categories <br>
Comparative analyses between the finished paths and the unfinished paths on the average numerical bias <br>
Impact of Bias on Wikispeedia Gameplay <br>
Linear Regression: To correlate article bias with navigation path. <br>
Correlation Analysis: Regression, Chi and T test to study relationships between article bias and gameplay metrics like backclicks. <br>
Comparative Statistical Tests: T-tests for comparing different political groupings. <br>
Chi-Square Test: To examine associations in categorical data like path choices. <br>
Political bias repartition for backclisks in finished and unfinished paths<br>
Analyses of bias evolution through the paths <br>
General Methodological Approaches <br>
Logistic regression to determine wether the results are statistically significant <br>

 



#### Organization within the team 

Wassim Maj : Redaction of Readme, Graphs, Analyses, Redaction of Data Story<br>
Viacheslav Bolotnikov : Data collection from websites, Analyses<br>
Jeremy Dahan : Data collection from websites, Redaction of Data Story<br>
Matthieu Jacques : Classification of political people, Graphs<br>
Adrien Joliat : NLP model, Analyses, Graphs, Website Design<br>



Sources 

[1] Das, S., Lavoie, A., & Magdon-Ismail, M. (2016). Manipulation among the arbiters of collective intelligence: How Wikipedia administrators mold public opinion. ACM Transactions on the Web (TWEB), 10(4), 1-25.

[2] Hube, C. (2017, April). Bias in wikipedia. In Proceedings of the 26th International Conference on World Wide Web Companion (pp. 717-721).


[3] West, R., Pineau, J., & Precup, D. (2009, June). Wikispeedia: An online game for inferring semantic distances between concepts. In Twenty-First International Joint Conference on Artificial Intelligence.

