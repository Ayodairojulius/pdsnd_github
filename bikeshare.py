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
    bold = '\33[1m'
    print(bold + 'ENTER YOUR NAME:')
    name =input().title()
    
    print(bold + 'Hello! {} Let\'s explore some US bikeshare data!'.format(name))
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("\n Kindly choose your city of interest:")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("\nMake a choice by entering the name of the city of interest (e.g. Chicago or New York City or Washington).")
        # user input converted to lower to standardize the
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\noh!, wrong input, please check again and reenter")

       
    print("\nYou picked {}, now let us continue....".format(city.title()))  
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3,
                  'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month of interest, between January to June, to get corresponding data insight:")
        print("enter 'all' if you wish to view for all the available months")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input. try again following the accepted input format.")
            
    
    print("\nChoosen month of interest: {}.".format(month.title()))


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
         print("\nEnter a day of the week to obtain corresponding data insight.:")
         print("This should be in the form monday or MONDAY, tuesday or TUESDAY, ...).")
         print("Note: (Enter 'all' or 'All' to get insight for all days in a week.)")
         day = input().lower()

         if day not in DAY_LIST:
                print("\nInvalid input. Please try again following the accepted input formats.")

            
    print("\nChoosen Day of interest: {}.".format(day.title()))    
    print("\nYou have chosen to view data for city: {}, month/s: {} and day/s: {}.".format(city.upper(), month.upper(), day.upper()))
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
    print("\nWait, let's load your data.......")
    df = pd.read_csv(CITY_DATA[city])
    
    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
#     df['day_of_week'] = df['Start Time'].dt.day_name
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"\nMost Common Day: {common_day}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"\nMost Common Start Hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")


    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {common_end_station}")
    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]
    print(f"\nThe most frequent combination of trips are from {combo}.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)

    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)

    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The types of users by number are given below:\n\n{}".format(user_type))


    # TO DO: Display counts of gender
    print('\n Collating Gender stats......')
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nIn this file, there is no 'Gender' column.")


    # TO DO: Display earliest, most recent, and most common year of birth

    print('\n Collating Birth Year stats......')
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth:        {common_year}")
    except:
        print("\nThis file has no information about the year of birth of users.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data_frame(df):
    """this function displays 5 rows of data from the csv file for the city selected.

    Args:
        param1 (df): The data frame we are working with.

    Returns:
        None.
    """
    EXPECTED_RESPONSE = ['yes', 'no']
    data = ''
  
    count = 0
    while data not in EXPECTED_RESPONSE:
        print("\nDo you wish to view the raw data?")
        print("\nAcceptable responses:\nYes or yes\nNo or no")
        data = input().lower()
       
        if data == "yes":
            print(df.head())
        elif data not in EXPECTED_RESPONSE:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the acceptable responses.")
            
   
    while data == 'yes':
        print("Do you wish to view more raw data?")
        count += 5
        data = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if data == "yes":
             print(df[count:count+5])
        elif data != "yes":
             break

    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data_frame(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
