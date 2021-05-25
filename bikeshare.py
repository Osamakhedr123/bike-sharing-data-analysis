import time
import pandas as pd
import numpy as np

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




    months= ['january', 'february', 'march', 'april', 'may', 'june']

    days = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ] 

    print('Hello! Let\'s explore some US bikeshare data!')

    # getting user input for city
    while True:
        try:
            city = input('would you like to see data for Chicago, New York City or Washington? \n> ').lower()
            if city in CITY_DATA.keys():
                break
        except:
            print('You entered an invalid input. Please enter chicago, new york or washington.\n')
        
    # getting user input for filter
    while True:
        try:
            filters =input('would you like to filter the data by month,day,both, or none? \n ').lower()
            if filters in ['month','day','both','none']:
                break
        except:
            print('You entered an invalid filter. please try again.')  

    if filters=='month':
        month=input('which month? {} \n> '.format(months)).lower()
        day='all'
    elif filters=='day':
        day=input('which day? {} \n> '.format(days)).title()
        month='all' 
    elif filters=='both':
        month=input('which month? {} \n> '.format(months)).lower()
        day=input('which day? {} \n> '.format(days)).title()      
    else:
        month,day='all','all'
   



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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]    
    
    
    return df
    
    
    

def time_stats(df,day,month):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displaying the most common month

    if month=='all':
        most_common_month = df['month'].mode()[0]
        print("The most common month is :", most_common_month)

    # displaying the most common day of week
    if day=='all':
        most_common_day_of_week = df['day_of_week'].mode()[0]
        print("The most common day of week is :", most_common_day_of_week)


    # displaying the most common start hour

    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displaying most commonly used start station

    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_common_start_station)
   


    # displaying most commonly used end station

    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", most_common_end_station)

   


    # displaying most frequent combination of start station and end station trip

           
    df['most_common_start_end_station'] = df['Start Station']+" to "+df['End Station']
    print("The most commonly used start station and end station : {}".format(df['most_common_start_end_station'].mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displaying total travel time


    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # displaying mean travel time
    
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displaying counts of user types

    user_counts = df['User Type'].value_counts()
    print("Counts of user types:\n",user_counts)



    # Displaying counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:\n",gender_counts)
  


    # Displaying earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest=df['Birth Year'].min()
        print("earliest birth year:",earliest)
        most_recent=df['Birth Year'].max()
        print("most recent birth year:",most_recent) 
        most_common_year = df['Birth Year'].mode()[0]
        print("The most common birth year:", most_common_year)
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,day,month)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    iter=5
    check='yes'
    while check=='yes':
        check=input('do you want to explore some raw input? enter yes for more or anything else to exit \n').lower()
        if check!='yes':
            break
        else:
            print(df.head())
        while True:
            check=input("do you want to display more raw input? enter yes for more or anything else to exit \n").lower()
            if check!='yes':
                break
            else:
                iter+=5
                print(df.iloc[iter:].head())
                iter+=5
                  
    print('thank you for using this program')





if __name__ == "__main__":
	main()
