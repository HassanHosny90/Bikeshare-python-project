from calendar import c
import time
from urllib import response
import pandas as pd
import numpy as np
from sympy import primitive

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    

    while True:
        
        city = input("Please choose a city to analyze (Chicago / New York City / Washington):").lower()
        if city in CITY_DATA:
            break
        else:
            print("Please enter a correct city name")
   
        
    
    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:

        month = input("Please enter a specific month (January --> June) or type \'all\' to view all months:").lower()
        if month in months:
            break
        else:
            print("Please enter a correct month")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:

        day = input("Please enter a specific weekday or type \'all\' for all days:").lower()
        if day in days:
            break
        else:
            print("Please enter a correct answer")

            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city]) 
    # Converting [Start Time] column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract and convert month and day of week to new separate columns
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.day_name()   # I got this method from searching

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # Filter by month new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week new dataframe
        df = df[df['day of week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May' , 'June']
    
    print("The most common month is: {}".format(months[most_common_month - 1]))

    # display the most common day of week
    most_common_day = df['day of week'].mode()[0]
    print("The most common day is: {}".format(most_common_day))

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Hour'].mode()[0]
    print("The most common start hour is: {}".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    #most_start_count = most_start_station.value_counts()
    print("The most common start point is: {}".format(most_start_station))

    # display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("The most common end point is: {}".format(most_end_station))

    # display most frequent combination of start station and end station trip
    df['Most Trip'] = df['Start Station'] +' : '+ df[ 'End Station']
    most_trip = df['Most Trip'].mode()[0]
    print("The most common trip is: {}".format(most_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print("Total travel duration is: {}".format(total_duration))
    # display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print("The average travel duration is: {}".format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_count = df['User Type'].value_counts()
    print("The total count of user types is: \n{}".format(users_count))

    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("The total number of gender is: \n{}".format(gender_counts))
    except:
        print("There is no Gender Column in your selected data")

    # Display earliest, most recent, and most common year of birth
    try:
        earl_year = (df['Birth Year'].min()).astype(int)  # I got this method from searching 
        recent_year = (df['Birth Year'].max()).astype(int)
        common_year = (df['Birth Year'].mode()[0]).astype(int)
    except:
        print("There is no Birth Date column in your selected data")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#function to ask user if User wanted to display the data

def show_data(df):
    """Asking User if want to see the Data"""

    print('\nFor more...\n')
    start_time = time.time()


    Answer = ['yes','no']
    while True:
        user_response = input("Do you want to see the first 5 Data rows?(yes or no)").lower()
        if user_response == 'yes':
            start = 0
            end = 5
            print(df.iloc[start:end])
            break
        elif user_response == 'no':
            break
        else:
            print("Please enter a valid answer")

    if user_response == 'yes':
        while True:
            user_response_2 = input("Do you want to see the next 5 rows in Data? (yes or no)")
            if user_response_2 == 'yes':
                start += 5
                end += 5
                print(df.iloc[start:end])
            elif user_response_2 == 'no':
                break
            else:
                print("Please enter a valid answer")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
