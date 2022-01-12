import time

import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday','tuesday','wednesday','tuesday','friday','saturday','sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = ""
    month = "all"
    day = "all"
    # user prompt for selecting the city
    while True: 
        city = input("Please enter the city you want to analyze (eg. chicago): ")
        city = city.lower()
        try:
            if(CITY_DATA[city]):
                break;
        except:
            print("The city you wrote is not in our dictionary, please input a correct city name");
    month = input("Please enter the month you want to analyze (eg. 'january') or 'all' for no filter:")
    month = month.lower()
    if not month in months:
        month = "all"
        print("The entered month is wrong. It will continue with all")

    day = input("Please enter the day of the week you want to analyze (eg. 'monday') or 'all' for no filter:")
    day = day.lower()
    if not day in days:
       day = "all"
       print("The entered month is wrong. It will continue with all")

    print('-'*40)
    return city, month, day


def read_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("Most popular month: ",popular_month)
    
    df['dayofweek'] = df['Start Time'].dt.weekday_name
    popular_dayofweek = df['dayofweek'].mode()[0]
    print("Most popular day of week: ",popular_dayofweek)

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most popular hour: ",popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    popular_start_station = df['Start Station'].mode()[0]
    print("Most popular start station: ",popular_start_station)


    popular_end_station = df['End Station'].mode()[0]
    print("Most popular end station: ",popular_end_station)


    df['combine'] = df["Start Station"]+" - "+df["End Station"]
    popular_combination_stations = df['combine'].mode()[0]
    print("Most popular combination of stations: ",popular_combination_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: ",total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print("Average travel time: ",mean_travel_time)


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type_counts = df['User Type'].value_counts()
    print("User type counts: \n",user_type_counts)

    if "Gender" in df.columns:
         # write code for Gender statistics
        gender_counts = df['Gender'].value_counts()
        print("\nGender counts: \n",gender_counts)

    if "Birth Year" in df.columns:
        earliest = df['Birth Year'].min()
        print("\nEarliest year of birth: ",earliest)

        most_recent = df['Birth Year'].max()
        print("Most recent year of birth: ",most_recent)

        most_common = df['Birth Year'].mode()[0]
        print("Most common year of birth: ",most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = read_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        rowindex = 0

        while True:
            raw = input('\nWould you like to get 5 more raw data? Enter yes or no.\n')
            if raw.lower() != 'yes':
                break
              
            print(df.iloc[rowindex:rowindex+5,:])
            rowindex=rowindex+5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
