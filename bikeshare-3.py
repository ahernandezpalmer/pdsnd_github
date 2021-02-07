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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city_list = ["chicago", "new york city", "washington"]
    print('Cities available for analysis: Chicago, New York City, Washington: ')
    city = input('Please enter the name of the City: ')
    city=city.lower()
    while True:
        try:
            if city not in city_list:
                city = input('City not valid, please enter city again: ').lower()
            else:
                print('You selected the city:', city.capitalize())
                break
        except ValueError:
            print('That is not a valid city')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list=['all','january','february','march','april','may','june']
    month = input('Please enter the month to filter by,  options are : january, february, march, april, may , june, all ')
    while True:
        try:
            if month not in month_list:
                month = input('Month not valid, please enter month again: ')
            else:
                print('You selected the month: ', month)
                break
        except ValueError:
            print('That is not a valid month')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input('Please enter the day of the week: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday ')
    while True:
        try:
            if day not in day_list:
                day = input('Day not valid, please enter day again: ')
            else:
                print('You selected the day: ',day)
                break
        except ValueError:
            print('That is not a valid day')
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month ,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

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

def display_raw_data(df):
    
    i = 0
    raw = input('Do you like to display raw data? yes/no') 
    # TO DO: convert the user input to lower case using lower() function
    raw=raw.lower()
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.head())  # start by viewing the first few rows of the dataset!
            print(df.columns) # viewing the first few colummns # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Do you like to see 5 more raws?").lower()# TO DO: convert the user input to lower case using lower() function
            
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # extract month ,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    
    popular_month = df['month'].mode()[0]
    print('The most popular month of the year is : ',popular_month)
 
    # TO DO: display the most common day of week
    
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is : ',popular_day)

    # TO DO: display the most common start hour
    
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    # adding function round() to eliminate unnecesary decimals
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #TO DO: display most commonly used start station
    popular_start_station= df['Start Station'].mode()[0]
    print('Most commonly used Start Station: ',popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station= df['Start Station'].mode()[0]
    print('Most commonly used End Station: ',popular_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station=df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most commonly used Start-End Station: ', popular_start_end_station)


    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum(axis=0)
    print('Total trip duration: ',round(total_travel_time))
    
    # TO DO: display mean travel time
    mean_trip_duration=df['Trip Duration'].mean()
    print('Mean trip duration: ', round(mean_trip_duration))
    
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count=df['User Type'].count()
    print('User Type count =  ',user_type_count)
    
    while True:
        try:
            if city.lower() != 'washington':
                # TO DO: Display counts of gender
                gender_count=df['Gender'].count()
                print('Gender count = ',gender_count)
                
                # TO DO: Display earliest, most recent, and most common year of birth
                earliest_birth_year=df['Birth Year'].min()
                mostrecent_birth_year=df['Birth Year'].max()
                mostcommon_birth_year=df['Birth Year'].mode()[0]
                print('Earliest birth of year: ',round(earliest_birth_year))
                print('Most recent birth of year: ',round(mostrecent_birth_year))
                print('Most common birth of year: ',round(mostcommon_birth_year))
                break
            else:
                print('For washington city no stats for Gender and Birth Year are available ')
                break
        except ValueError:
            print('That is not a valid city')
    
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if city.lower() != 'washington':
            
            display_raw_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)
            
        else:
            display_raw_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)
            
            
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'no':
            break
        elif restart == 'yes':
            continue
        else:
            restart = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
           
if __name__ == "__main__":
	main()

