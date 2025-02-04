

### Date created
30/04/2022

### Project Title
EXPLORE US BIKESHARE DATE

### Description
In this project,I made use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote the code to import the data and answer interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

In this project,I used data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I also compared the system usage between three large cities: Chicago, New York City, and Washington, DC.


### Software Requirements
You should have 
* Python 3,NumPy, and pandas installed using Anaconda
* A text editor, like [Sublime](https://www.sublimetext.com/) or [Atom](https://atom.io/).
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).


### Files used
* chicago.csv
* new_york_city.csv
* wishington.csv

### DATA SETS
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

### Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

**1 Popular times of travel (i.e., occurs most often in the start time)**

* most common month
* most common day of week
* most common hour of day

**2 Popular stations and trip**

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

**3 Trip duration**

* total travel time
* average travel time

**4 User info**

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Credits
* https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.htmlhttps://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
* https://pandas.pydata.org/pandas-docs/stable/reference/series.html#indexing-iteration
* https://pandas.pydata.org/pandas-docs/stable/reference/series.html#reindexing-selection-label-manipulation
