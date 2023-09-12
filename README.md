# Postgraduate - Big Data Analytics - FIA 
## Prediction of ROAS in search query (Google Merchandise Store) 
### Student's Name: Nadja Pereira dos Santos

Table of Contents
1. Search Engine
2. Post-Sales Prediction
3. Work Objective
4. Description of Variables
5. Exploratory Analysis
6. KNN Model

## 1. Search Engine
In the modern economy, using search engines is a part of digital life. In this context, machine learning plays a crucial role in enabling the public to solve specific problems, ranging from personal questions to searching for products and services. Typically, when it comes to consumer goods, the audience starts with a generic term and gradually refines the search until they find the ideal product hosted on a website or e-commerce platform. There are four popularly known machine learning algorithms used for classifying searches, such as "Rankbrain," "Bert," "Smith," and "MUM." Specifically, "BERT" is a neural network that understands words without context and how people are asking questions. "Smith" is an "enhanced BERT" based on word hierarchy. "MUM" is considered a thousand times more powerful than "BERT" due to being faster and more intuitive.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/bc115d65-597f-4d68-90e0-124c1e21d24f)

### Queries
According to the book "The Art of SEO," 78% of internet searches use four words or less. The author himself points out that the best returns can be found in the third or fourth position. One of the key metrics to measure the effect of a click after a search is the Click Through Rate (CTR). In a study published in 2019 by TrajectData, the CTR generated on desktops for both branded and non-branded searches becomes similar starting from the third position on Google. The CTR of branded searches in the second position is noteworthy, as described in the link below.

## 2. Post-Sales Prediction
In this work, the focus is on the 'navigational query' of the Google Merchandise Store website. Google provides purchase information from the brand's product site, including items like cups, backpacks, notebooks, and various other products, for free. This information is available through the Google Analytics platform for learning purposes. Since media investment is also provided, the goal is to make post-sales predictions to gain insights into sales already made. The calculation of ROAS (Return on Ad Spend) can indicate the percentage of how much a campaign has yielded in relation to its keyword. ROAS stands for "Return of Ad Spend," representing the value of each dollar spent for each return received by the company. In one search, the keyword "Google Clothing" had 1,591 clicks, cost $6,038.57, generated $3,164 in revenue, and resulted in a -48% ROAS. Going beyond ROAS using machine learning techniques is an interesting alternative for future ad campaigns, with the identification of user behavior patterns and better allocation of media budget.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/5b8ad5c0-dc0f-4ab5-95cd-bde70f64304d)


## 3. Work Objective
<p> </p>
The main objective of this work is to make predictions beyond ROAS using data extracted from Google Analytics - Universal Analytics. The well-known formula is (Revenue - Cost) / Cost, and the purpose is to predict, based on past results, which machine learning technique contributes to investment performance. Unlike ROI (Return on Investment), ROAS is the most significant indicator of the success of advertising campaigns. Consequently, marketing and media companies can make adjustments to their campaigns based on the available budget.


## 4. Description of Variables
Keywords - words that users use on Google
Clicks - Users clicked on an ad element.
Cost - Amount charged for the ad investment.
CPC (Cost Per Click) - Amount charged after the user clicks on the ad.
Users - Logged-in (or not) individuals who interact with pages or apps.
Sessions - Time the user spends on an app or website; by default, it is set for up to 30 minutes, but this time can be changed according to business needs.
E-commerce Return Rate - Average conversions that were completed.
Pages/Session - The number of pages the user navigated during a session.
Transactions - Purchase orders on the websites.
Revenue - Value received from completed transactions.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/8c2ec0fc-f366-4cf9-82df-6bea322dc607)


## 5. Exploratory Analysis (Total Dataset)
The raw dataset consists of 858 rows, composed of columns related to a campaign, such as the number of clicks, cost of the search query, bounce rate, among other data. However, there were two problems: the dataset had exactly identical duplicate terms that were merged, reducing it to 765 rows. When a new selection was made, excluding rows with zero revenue, it was further reduced to 47 rows. The option was to conduct separate analyses regarding the dataset.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/0ed359c9-3f67-4591-acd9-de8198ec3ca5)


### 5.1. Exploratory Analysis (Total Dataset)
Below are the details of the total dataset, and even the 'cleaned' dataset with processed data shows similar values. For example, there is a histogram with very similar values and outliers present in the dataset. 95% of the revenue is 0, which means that a significant investment is made in ads, but almost no revenue is generated.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/21d9e8be-ca04-4b33-9871-89878b8d2748)


## (Positive ROAS)
After separating the dataset into positive and negative ROAS, new insights are presented. In the case of positive revenue, for example, there is a significantly higher value related to the search for "Google Merchandise Store" with a cost of $2,182 and revenue of $135,917, resulting in a ROAS of 6129%. The second unusual value is $61 in cost and $1,324 in revenue, with a 2070% ROAS.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/11b611be-32ff-44aa-bbaf-f4edee663b90)


## (Negative ROAS)
Considering 35 rows with different revenue values, there is an average of -0.74%. The lowest value is -9% with a $300 investment and $274 in returns.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/2b51e2a7-45bb-4d50-944d-3874e37074ad)


### (Linear Regression)
Comparing the R^2 of the dataset, we have on the left side revenue data that is 'greater' than the others and revenue data that is 'lower,' both with negative values. The prevalence of negative revenue directly affects the index.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/6b83fb39-c246-46b5-b356-20fe0b551452)


### K-means
There are two prominent groups, yellow (A) and purple (B). The yellow group is much more dispersed and has revenue up to 1500, while the purple group is concentrated around 5000 in revenue and 2000 in cost. The main recommendations are to use more keywords that generate higher revenue, found in the 'positive' list, and not to invest more than $2000 to avoid negative impacts on results.

![image](https://github.com/nadjapereira/ml-thesis/assets/11997614/dbbdc6cb-52c2-4a43-959e-0a023dc582d4)




