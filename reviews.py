# add your code here
import pandas as pd

wine_df = pd.read_csv('data/winemag-data-130k-v2.csv')

#pivot the data by country and use two different aggregation functions to get count and mean onthe points column
country_average_points = wine_df.pivot_table(values = ['points'], index='country', aggfunc=['count', 'mean'])
#drop the 1st level of the pivot dataframe
country_average_points = country_average_points.droplevel(1, axis=1)
#sort the dataframe by the count of points in descending order
country_average_points.sort_values(by = 'count', ascending=False, inplace=True)
#round the mean points to 1 decimal places
country_average_points['mean'] = country_average_points['mean'].round(1)
country_average_points.rename(columns={'mean':'points'}, inplace=True)

country_average_points.to_csv('data/reviews-per-country.csv')
