
# Instagram Reach Analysis

This README provides an overview of the Customer Lifetime Value (CLV) Analysis Project, a Python-based data analysis project that aims to extract insights from a dataset and visualize key metrics related to customer lifetime value.

## How to use this repository
This repository has three files:

1. Excel file - This is the dataset that was used to analyse metrics and create visualizations.

2. Python file - This is the .py file that contains the codes to do the analysis on the dataset.

3. Read.me - This is the current file that contains instructions to navigate and use this project and results from the analysis of the data including visualizations.

## Installation instructions

Download the Excel file to your local machine using the link provided in the data sources section on this page.
Download a Python IDE to explore the analysis process and visualizations. I used Jupyter Notebooks for my project.
Feel free to adapt the code to your own datasets or use it as a reference for similar projects.

## Data sources

You can download the dataset from here: [https://statso.io/customer-lifetime-value-analytics-case-study/ ](https://statso.io/instagram-reach-analysis-case-study/)

## References

[https://thecleverprogrammer.com/2023/05/01/customer-lifetime-value-analysis-using-python/ ](https://amankharwal.medium.com/data-analysis-projects-with-python-a262a6f9e68c)

## Results and evaluation

![impressions](https://github.com/sumaiyamahmud/instagram_reach_analysis/assets/113713705/b365eb3c-fb99-4c5c-91ef-c233af1444d0)

This graph shows the distributions of impressions. The histogram is divided into 10. Each bin on the x-axis represents a range of impressions, and the height of the bar in each bin indicates the count of posts that fall within that range. Impressions within the range 0-5000 has the highest count. 74 posts have an impression in the range 0-5000 and1 post has an impression between 35k to 40k.

![corr](https://github.com/sumaiyamahmud/instagram_reach_analysis/assets/113713705/f9894c17-2637-464a-a754-ec8df192a339)

This correlation matrix shows a negative correlation between comments and and the rest of the features and the highest correlation is between profile visits and follows indicating more visits lead to higher number of follows.

![eng](https://github.com/sumaiyamahmud/instagram_reach_analysis/assets/113713705/3e02b7f3-a054-459c-9500-00781b183b88)

This plot indicates that the number of shares increases for posts with more likes as shown by the higher concentration of dark blue data pointsto the left of the plot and a yellow data point to the very right of the plot and lighter shades in between. It also shows that the data points are larger in size as the number of likes increase, indicating posts with higher likes get more profile visits.

![hy](https://github.com/sumaiyamahmud/instagram_reach_analysis/assets/113713705/07377ca3-4d7e-4908-a668-1b7ba90f9f99)

This graph above shows that there are 119 posts in the dataset where the number of comments is approximately 19, indicating that majority of the posts get very few comments. The posts hardly get any shares as shown by a lack of green colour in the graph. The height of the blue bars show that few posts are getting a high number of likes. Overall, the 

#Interpretation: This information provides insights into the distribution of likes across your dataset. You can observe how many posts receive a certain number of likes, and the histogram helps you identify patterns or trends in terms of user engagement.

![fr](https://github.com/sumaiyamahmud/instagram_reach_analysis/assets/113713705/9f225994-f9aa-47fc-a28e-3eed05dd1c1d)

This plot shows that as the profile visits increase, so does the follows.
