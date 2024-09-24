import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # Count the number of occurrences for each race
    race_count = df['race'].value_counts()

    # Calculate the average age of men, rounded to one decimal place
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Calculate the percentage of people with a bachelor's degree, rounded to one decimal place
    percentage_bachelors = round(100 * df['education'].value_counts(normalize=True)['Bachelors'], 1)

    # Filter data for people with higher education (Bachelor's, Master's, Doctorate)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    # Filter data for people without higher education
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Calculate the percentage of people with higher education earning >50K, rounded to one decimal place
    higher_education_rich = round(100 * (higher_education['salary'] == '>50K').mean(), 1)
    # Calculate the percentage of people without higher education earning >50K, rounded to one decimal place
    lower_education_rich = round(100 * (lower_education['salary'] == '>50K').mean(), 1)

    # Find the minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Filter data for people who work the minimum number of hours per week
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    # Calculate the percentage of people who work the minimum hours and earn >50K, rounded to one decimal place
    rich_percentage = round(100 * (num_min_workers['salary'] == '>50K').mean(), 1)

    # Calculate the percentage of people earning >50K by country and sort in descending order
    country_stats = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean()).sort_values(ascending=False)
    # Find the country with the highest percentage of people earning >50K
    highest_earning_country = country_stats.index[0]
    # Calculate the highest percentage of people earning >50K in a country, rounded to one decimal place
    highest_earning_country_percentage = round(100 * country_stats.iloc[0], 1)

    # Find the most common occupation among people from India earning >50K
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().index[0]

    # If print_data is True, print the results
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Return the results in a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }