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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            city=input("Enter The city name you want to acquire statistics for,\nYou can either choose Chicago, New York City or Wahington: ").lower()
            if city in CITY_DATA.keys():
                break
        except:
            print("You entered an invalid input, Please try again\nEnter Chicago,Washington or New York City")
    while True:
        try:
            choice=input("Do you want to filter by month, day, both or none? ").lower()
            if choice in ['month','day','both','none']:
                break
        except:
            print("That's a wrong choice!\nTry again\nChoose between month, day, both or none")
    if choice=='day' or choice=='both':
        while True:
            try:
                day=input("Enter the day name: ").title()
                days = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
                if day in days:
                    break
            except:
                    print("You entered an invalid input\nPlease choose a week day name and enter it:\n{}\n".format(days))
    if choice=='month' or choice=='both':
        while True:
             try:
                 months = ['January', 'February','March', 'April', 'May', 'June']
                 month=input("Enter the month name:\n{}\n ".format(months)).title()
                 if month in months:
                    break
             except:
                print("You entered an invalid month name, Please choose from:\n{}\n".format(months))
    if choice=='none':
        month,day='all','all'
    elif choice=='day':
        month=all
    elif choice=='month':
        day='all'
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['Start_hour'] = df['Start Time'].dt.hour
    if month!='all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
        df=df[df['month']==month]
    if day!='all':
        df = df[df["day_of_week"] == day]
    return df


def time_stats(df,day,month):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month=='all':
        print("The most common month: ",df['month'].mode()[0])

    # display the most common day of week
    if day=='all':
        print("The most common day: ",df['day_of_week'].mode()[0])

    # display the most common start hour
    print("The most common start hour: ",df['Start_hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most popular Start station: ",df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most popular End station: ",df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['start_and_end']=df['Start Station']+"   to   "+ df['End Station']
    print("The most frequent combination of start and end stations:",df['start_and_end'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['travel_time']=df['End Time']-df['Start Time']
    print("Total travel time:\n",df['travel_time'].sum())

    # display mean travel time
    print("The mean of travel time:",df['travel_time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The count of user types:\n", df['User Type'].value_counts())
    
    # Display counts of gender
    if "Gender" in df.columns:
        print("The counts of gender:\n", df['Gender'].value_counts())

     
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("The earliset year of birth: {}\nThe most recent year of birth: {}\nThe most common year of birth: {}".format(
            df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0]))

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
    check='yes'
    while check=='yes':
        check=input("Do you want to view raw data of {}?\nType yes for more or any other key to exit: ".format(city)).lower()
        if check!='yes':
            break
        n = 5
        print(df.head(n))
        while True:
            check=input("do you want to see more?\nEnter yes to continue or any other key to exit: ").lower()
            if check!='yes':
                break
            n+=5
            print(df.head(n))
    print("Thank you for using my program")
if __name__ == "__main__":
	main()

