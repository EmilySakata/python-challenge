#inport library
import os
import csv
import pandas as pd

#Reach each of the csv vaule as a dataframe.
employee_data1 = pd.read_csv("employee_data1.csv")
employee_data2 = pd.read_csv("employee_data2.csv")

#add first name and last name into the data table.
employee_data1[['First_Name', 'Last_Name']] = employee_data1.Name.str.split(' ', expand=True)
employee_data2[['First_Name', 'Last_Name']] = employee_data1.Name.str.split(' ', expand=True)

# use dictionary to convert states 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#use the dictionary of full state name and shrt statename, replace the state name by the short state name.
employee_data1["State"].replace(us_state_abbrev, inplace=True)
employee_data2["State"].replace(us_state_abbrev, inplace=True)

# change the date format to  month / days/ year
employee_data1['DOB'] = pd.to_datetime(employee_data1.DOB)
employee_data1['DOB'] = employee_data1['DOB'].dt.strftime('%m/%d/%Y')

employee_data2['DOB'] = pd.to_datetime(employee_data2.DOB)
employee_data2['DOB'] = employee_data2['DOB'].dt.strftime('%m/%d/%Y')

# replace the first 6 digit of the SSN with star
employee_data1["SSN"] = "***-**-" + employee_data1['SSN'].str[7:]
employee_data2["SSN"] = "***-**-" + employee_data2['SSN'].str[7:]

# output dataframe to cvs file
employee_data1.to_csv('new_employee_data1.csv', index=False, header=True)
employee_data2.to_csv('new_employee_data2.csv', index=False, header=True)



