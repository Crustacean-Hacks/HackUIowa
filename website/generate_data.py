from flask import Flask, render_template
import json

app = Flask(__name__)

def read_and_convert_json(filename):
    # Initialize the nested dictionary structure
    data_structure = {
        "websites": {}
    }

    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

            # Process website data
            websites = data.get("websites", {})
            for website, years in websites.items():
                data_structure["websites"][website] = {}
                for year, months in years.items():
                    data_structure["websites"][website][year] = {}
                    for month, days in months.items():
                        data_structure["websites"][website][year][month] = {}
                        for day, hours in days.items():
                            data_structure["websites"][website][year][month][day] = {}
                            for hour, value in hours.items():
                                data_structure["websites"][website][year][month][day][hour] = value

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data_structure


from datetime import datetime, timedelta


# Function to get data for a specific date
def get_data_for_date(date, data_structure):
    year, month, day = date.split('-')

    result = {}

    websites_data = data_structure.get("websites", {})
    for website, years in websites_data.items():
        year_data = years.get(year, {})
        month_data = year_data.get(month, {})
        day_data = month_data.get(day, {})

        if day_data:
            result[website] = {year: {month: {day: day_data}}}

    return result


# Function to get data for a week starting from a specific date
def get_data_for_week(start_date, data_structure):
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    week_data = {}

    for i in range(7):
        current_date = start_date_obj + timedelta(days=i)
        current_date_str = current_date.strftime('%Y-%m-%d')
        day_data = get_data_for_date(current_date_str, data_structure)

        for website, years in day_data.items():
            if website not in week_data:
                week_data[website] = {}
            for year, months in years.items():
                if year not in week_data[website]:
                    week_data[website][year] = {}
                for month, days in months.items():
                    if month not in week_data[website][year]:
                        week_data[website][year][month] = {}
                    week_data[website][year][month].update(days)

    return week_data


# Function to get data for a month
def get_data_for_month(date, data_structure):
    year, month, _ = date.split('-')

    month_data = {}

    websites_data = data_structure.get("websites", {})
    for website, years in websites_data.items():
        year_data = years.get(year, {})
        month_data_for_site = year_data.get(month, {})

        if month_data_for_site:
            month_data[website] = {year: {month: month_data_for_site}}

    return month_data


# Function to get data for a year
def get_data_for_year(date, data_structure):
    year, _, _ = date.split('-')

    year_data = {}

    websites_data = data_structure.get("websites", {})
    for website, years in websites_data.items():
        year_data_for_site = years.get(year, {})

        if year_data_for_site:
            year_data[website] = {year: year_data_for_site}

    return year_data

# Example usage:
filename = "hackathons/HackUIowa/website/test.json"
result = read_and_convert_json(filename)
print(result)

# Example usage
filename = "hackathons/HackUIowa/website/test.json"
data_structure = read_and_convert_json(filename)
date = "2023-09-23"
result_for_date = get_data_for_date(date, data_structure)
print(result_for_date)

# Example usage
filename = "hackathons/HackUIowa/website/test.json"
data_structure = read_and_convert_json(filename)
start_date = "2023-09-23"
result_for_week = get_data_for_week(start_date, data_structure)
print(result_for_week)

# Example usage
filename = "hackathons/HackUIowa/website/test.json"
data_structure = read_and_convert_json(filename)
date = "2022-09-23"
result_for_month = get_data_for_month(date, data_structure)
print(result_for_month)

# Example usage
filename = "hackathons/HackUIowa/website/test.json"
data_structure = read_and_convert_json(filename)
date = "2021-09-23"
result_for_year = get_data_for_year(date, data_structure)
print(result_for_year)