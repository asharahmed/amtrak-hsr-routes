
import pandas as pd

# define the top five high-speed rail priority projects
priority_projects = [{'start_city': 'San Francisco', 'end_city': 'Los Angeles', 'investment': 60},
                     {'start_city': 'Dallas', 'end_city': 'Houston', 'investment': 20},
                     {'start_city': 'New York City', 'end_city': 'Washington DC', 'investment': 50},
                     {'start_city': 'Seattle', 'end_city': 'Portland', 'investment': 40},
                     {'start_city': 'Tampa', 'end_city': 'Orlando', 'investment': 2.5}]

# define the second-tier projects
second_tier_projects = [{'start_city': 'Chicago', 'end_city': 'Milwaukee', 'investment': 8},
                        {'start_city': 'Atlanta', 'end_city': 'Charlotte', 'investment': 18},
                        {'start_city': 'Louisville', 'end_city': 'Nashville', 'investment': 15},
                        {'start_city': 'Denver', 'end_city': 'Albuquerque', 'investment': 40},
                        {'start_city': 'Chicago', 'end_city': 'St. Louis', 'investment': 18},
                        {'start_city': 'Tulsa', 'end_city': 'Oklahoma City', 'investment': 8},
                        {'start_city': 'Chicago', 'end_city': 'Detroit', 'investment': 30},
                        {'start_city': 'Nashville', 'end_city': 'Memphis', 'investment': 15},
                        {'start_city': 'Kansas City', 'end_city': 'St. Louis', 'investment': 19},
                        {'start_city': 'Chicago', 'end_city': 'Indianapolis', 'investment': 17}]

# combine the two lists into a single list
projects = priority_projects + second_tier_projects

# create a Pandas DataFrame from the project data
df = pd.DataFrame(projects)

# add a column for the project name based on the start and end cities
df['project'] = df['start_city'] + ' to ' + df['end_city']

# rearrange the columns to put the project name first
df = df[['project', 'start_city', 'end_city', 'investment']]

# save the DataFrame to a CSV file
df.to_csv('amtrak_hsr_routes.csv', index=False)

# display the DataFrame
print(df)
