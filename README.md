# Used car price prediction
- The repository is to explore the data of used car from https://www.truecar.com/. The process includes raw data collection, data processing, exploratory data analysis, machine learning models building.

## Raw data collection
`./data_collection`

- The data sources is scraped from TrueCar offical website. 

## Data processing
`./data_processing`

- ~175k raw data. Dropped ~15k duplicates. Handled missing values and outliers ~19k. The processed data has ~134k records.

## EDA and feature selection.
`./data_analysis`

- Check scatter plots between some numeric features and average list price.
- Check correlation matrix of numeric features.
- Encoding nominal categorical features.

Some findings:
1. There is a strong positive relationship between year and average list price. The average of price increases as the year of used car increases.
2. There is a negative relationship(not strong) between mpg combined and average list price. The lower the mpg combined the higher the average list price.
3. There is a strong negative relationship mileage range and average list price. The lower the mileage range the higher the average list price.
4. There are high correlations between mpg city, mpg combined, and mpg highway.
5. vehicle list price has relatively high correlation with vehicle year

## Machine learning
`./modeling`

- Dimension of features ~135k x 35
- Random forest regressor tuned with GridsearchCV.
    - R2 test: 0.84; R2 train: 0.87
    - RMSE test: 1697.04; RMSE train: 1504.47
    
- Top features, ranked by importance
    - mileage
    - style_id
    - chrome_trim_id
    - year
    - mpg_combined
    - drive_train_FWD
    - model_id
    - make_id
    - body_style_pickup-truck
    - body_style_suv