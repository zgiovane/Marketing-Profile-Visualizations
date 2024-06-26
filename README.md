Data that was utilized for this research can be found here: https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
Note that is wanting to run the code the user may need to install the libraries to the local machine utilizing the following command below: <br> `pip install -library-`

## INTRODUCTION
This report presents an analysis of demographic factors influencing income levels, leveraging data provided by the U.S. Census Bureau. In collaboration with XYZ Corporation, this project aims to support UVW College in developing targeted marketing strategies to enhance enrollment by identifying potential students through income-level indicators.

## GOALS & BUSINESS OBJECTIVES
The primary objective is to uncover the relationship between income levels and various demographic factors, including education, age, gender, race, and working hours. By understanding these relationships, UVW College can better tailor its marketing efforts to attract individuals most likely to enroll.

## ASSUMPTIONS
The Census Bureau data accurately reflects the broader population's demographic and income distribution. Income level is a significant factor influencing individuals' decisions regarding higher education enrollment. UVW has the

## USER STORIES & VISUALIZATIONS

### User Story 1: Impact of Education on Income
The visualization I chose was the Bar plot showing the number of individuals by education and salary. Some insights I determined is Higher education levels correlate with higher income brackets, suggesting targeted marketing towards individuals with specific educational backgrounds could be effective.

![](https://github.com/zgiovane/Marketing-Profile-Visualizations/blob/a82c996ca32330de508185e2eead6dbb80c9c071/plot-visuals/Screenshot%202024-02-27%20215422.png)
 
### User Story 2: Age and Income Distribution
The next visualization I chose is the Box plot segmented by income and age, filtered for individuals with specific education levels. Some insights I learned were younger individuals, especially those under 30, show a wider distribution in income levels across different education levels, indicating a potential target demographic for marketing campaigns.

![](https://github.com/zgiovane/Marketing-Profile-Visualizations/blob/39f62b704b7cb36c3f28eced897eb68b189921a0/plot-visuals/Screenshot%202024-02-27%20215749.png)

### User Story 3: Marital Status and Occupation's Effect on Income
The visualization I chose for this user story was the stacked bar chart showing the percentage of individuals exceeding $50K income by occupation and marital status. Some insights I reasoned were certain occupations and marital statuses are more likely to earn above $50K, highlighting potential demographics for recruitment.

![](https://github.com/zgiovane/Marketing-Profile-Visualizations/blob/9d7284524636cb42b815e0bd57a061e5385338e9/plot-visuals/Screenshot%202024-02-27%20215934.png)
 
### User Story 4: Gender and Race Income Distribution
The next visualization I chose was the count plots for income distribution by gender and race. Some insights I learned through this were significant disparities in income distribution suggest targeted marketing could address underrepresented or disadvantaged groups.

![](https://github.com/zgiovane/Marketing-Profile-Visualizations/blob/e0833e1581b31819f8cf3e0f200e69d450a20657/plot-visuals/Screenshot%202024-02-27%20220053.png)

![](https://github.com/zgiovane/Marketing-Profile-Visualizations/blob/e3a2fe65f72d03596bdf42b3d8b8fc1320e29807/plot-visuals/Screenshot%202024-02-27%20220119.png)

### User Story 5: Hours Per Week and Capital Gain
The final visualization I created for this was Strip plot showing hours worked per week by capital gain category, segmented by income level. Insights from this user story revealed individuals working longer hours or with higher capital gains are more likely to fall into the higher income bracket, indicating a demographic with potential interest in furthering their education for career advancement.

![](https://github.com/zgiovane/Marketing-Profile-Visualizations/blob/410f41bb7b2be02110b8683cfdbaacd59c321c58/plot-visuals/Screenshot%202024-02-27%20220408.png)
 
## METHODOLOGY
The project involved extensive data cleaning, including handling missing values and transforming data types for analysis. Notably, "Capital Gain" and "Hours Per Week" were converted to numeric types and binned for categorical analysis. These transformations enabled a comprehensive examination of the data through various visualizations.

## KEY FINDINGS
- Education level is a strong predictor of income, with higher education correlating to higher income levels.
- Age distributions suggest younger individuals with certain education levels might be more receptive to marketing efforts.
- Marital status and occupation significantly influence income, offering targeted marketing opportunities.
- Gender and race disparities in income distribution present opportunities for targeted outreach to promote diversity and inclusion.
- Working hours and capital gains are indicators of income level, suggesting individuals seeking career advancement are a key demographic.

## FUTURE WORK
Further analysis could explore the impact of additional variables such as industry, employer size, or geographical location on income. Advanced modeling techniques, including predictive analytics, could refine marketing strategies.

## CONCLUSION
The analysis reveals significant insights into the demographic factors influencing income levels, providing UVW College with data-driven strategies to enhance marketing efforts. By focusing on identified key demographics, UVW College can more effectively target potential students, thereby increasing enrollment and promoting educational advancement.
