from flask import Flask, render_template
import json
import site_analysis as sa
import app as Application

twenty_colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'grey', 'black',
            'lightblue', 'lime', 'cyan', 'magenta', 'teal', 'gold', 'navy', 'indigo', 'silver', 'olive']
six_colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

def bubble_sort_top_x(input_dict, x):
    # Convert dictionary items to a list of tuples
    items = list(input_dict.items())

    # Bubble sort in descending order
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        # If no swaps were made in this pass, the list is already sorted
        if not swapped:
            break
        # Stop execution and return only the top x items
        if i == (x-1):
            return dict(items[:x])

    # Return the top x items
    return dict(items[:x]), dict(items[x:])

def day_data_bar(data, year, month, day):
    out_dict = {}
    for site in data["websites"]:
        if(data["websites"][site][year][month][day] != None):
            time = 0 # time spent in seconds
            for hour in data["websites"][site][year][month][day]:
                time += data["websites"][site][year][month][day][hour]
                        
            mins = time // 60
            out_dict[site] = mins
    
    # sort the dictionary by value of mins in descending order. Only need to get the top 20 so use bubble sort
    out_dict, _ = bubble_sort_top_x(out_dict, 20)
    
    colors = twenty_colors
    
    return {"labels": list(out_dict.keys()), "datasets": [{"label": "Time spent on websites (mins)", "data": list(out_dict.values()), "backgroundColor": colors}]}
    
# Returns data for a bar graph of the time spent on different websites in a given month
def month_data_bar(data, year, month):
    out_dict = {}
    for site in data["websites"]:
        if(data["websites"][site][year][month] != None):
            time = 0 # time spent in seconds
            for day in data["websites"][site][year][month]:
                for hour in data["websites"][site][year][month][day]:
                    time += data["websites"][site][year][month][day][hour]
                        
            mins = time // 60 # convert from seconds to minutes
            out_dict[site] = mins
            
    # sort the dictionary by value of mins in descending order. Only need to get the top 20 so use bubble sort
    out_dict, _ = bubble_sort_top_x(out_dict, 20)
    
    # make a list of unique colors for each bar (website) in the graph
    # Top 20 websites
    colors = twenty_colors

    return {"labels": list(out_dict.keys()), "datasets": [{"label": "Time spent on websites (mins)", "data": list(out_dict.values()), "backgroundColor": colors}]}


# Returns json to send to javascript for the time spent on different websites all-time
def total_data_bar(data):
    data = d2
    out_dict = {}
    for site in data["websites"]:
        time = 0 # time spent in seconds
        for year in data["websites"][site]:
            for month in data["websites"][site][year]:
                for day in data["websites"][site][year][month]:
                    for hour in data["websites"][site][year][month][day]:
                        time += data["websites"][site][year][month][day][hour]
        
        mins = time // 60 # convert from seconds to minutes
        out_dict[site] = mins
        
    # sort the dictionary by value of mins in descending order. Only need to get the top 5 so use bubble sort
    out_dict, _ = bubble_sort_top_x(out_dict, 20)
    
    # make a list of unique colors for each bar (website) in the graph
    # Top 20 websites
    colors = twenty_colors

    return {"labels": list(out_dict.keys()), "datasets": [{"label": "Time spent on websites (mins)", "data": list(out_dict.values()), "backgroundColor": colors}]}

# USE CHATGPT TO MAKE A CALL TO THE API TO GET THE CATEGORY OF THE WEBSITE
def get_category(site):
    return Application.get_category(site)

# Adds up the times of categories not in the top 5
def get_rest_data(data):
    min_times = 0
    for cat, val in data:
        min_times += val
    return min_times

# day pie chart
def day_data_pie(data, year, month, day):
    out_dict = {}
    for site in data["websites"]:
        if(data["websites"][site][year][month][day] != None):
            time = 0 # time spent in seconds
            for hour in data["websites"][site][year][month][day]:
                time += data["websites"][site][year][month][day][hour]
            
            category = get_category(site)
            mins = time // 60 # convert from seconds to minutes
            if(category in out_dict):
                out_dict[category] += mins
            else:
                out_dict[category] = mins
    
    # sort the dictionary by value of mins in descending order. Only need to get the top 5 so use bubble sort
    out_dict, rest_dict = bubble_sort_top_x(out_dict, 5)
    rest_time = get_rest_data(rest_dict)    
    out_dict["Other Categories"] = rest_time
    
    datasets = [{
        "label": 'Website Time by Category',
        "backgroundColor": ['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 205, 86, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
        "borderColor": ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(255, 205, 86, 1)', 'rgba(54, 162, 235, 1)', 'rgba(153, 102, 255, 1)'],
        "borderWidth": 1,
        "data": list(out_dict.values()),
    }]

    return {"labels": list(out_dict.keys()), "datasets": datasets}

# month pie chart
def month_data_pie(data, year, month):
    out_dict = {}
    for site in data["websites"]:
        if(data["websites"][site][year][month] != None):
            time = 0 # time spent in seconds
            for day in data["websites"][site][year][month]:
                for hour in data["websites"][site][year][month][day]:
                    time += data["websites"][site][year][month][day][hour]
            
            category = get_category(site)
            mins = time // 60 # convert from seconds to minutes
            if(category in out_dict):
                out_dict[category] += mins
            else:
                out_dict[category] = mins
    
    # sort the dictionary by value of mins in descending order. Only need to get the top 5 so use bubble sort
    out_dict, rest_dict = bubble_sort_top_x(out_dict, 5)
    rest_time = get_rest_data(rest_dict)
    out_dict["Other Categories"] = rest_time
    
    datasets = [{
        "label": 'Website Time by Category',
        "backgroundColor": ['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 205, 86, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
        "borderColor": ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(255, 205, 86, 1)', 'rgba(54, 162, 235, 1)', 'rgba(153, 102, 255, 1)'],
        "borderWidth": 1,
        "data": list(out_dict.values()),
    }]

    return {"labels": list(out_dict.keys()), "datasets": datasets}
    

# all-time pie chart
def total_data_pie(data):
    data = d2
    out_dict = {}
    for site in data["websites"]:
        time = 0 # time spent in seconds
        for year in data["websites"][site]:
            for month in data["websites"][site][year]:
                for day in data["websites"][site][year][month]:
                    for hour in data["websites"][site][year][month][day]:
                        time += data["websites"][site][year][month][day][hour]
        
        category = get_category(site)
        mins = time // 60 # convert from seconds to minutes
        if(category in out_dict):
            out_dict[category] += mins
        else:
            out_dict[category] = mins
        
    # sort the dictionary by value of mins in descending order. Only need to get the top 5 so use bubble sort
    out_dict, rest_dict = bubble_sort_top_x(out_dict, 5)
    rest_time = get_rest_data(rest_dict)
    out_dict["Other Categories"] = rest_time
    
    # make a list of unique colors for each bar (website) in the graph
    # 6 colors
    colors = six_colors
    
    datasets = [{
        "label": 'Website Time by Category',
        "backgroundColor": ['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 205, 86, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
        "borderColor": ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(255, 205, 86, 1)', 'rgba(54, 162, 235, 1)', 'rgba(153, 102, 255, 1)'],
        "borderWidth": 1,
        "data": list(out_dict.values()),
    }]

    return {"labels": list(out_dict.keys()), "datasets": datasets}

d = {
  "storageid": "7832484732981421",
  "websites": {
    "google.com": {
      "2023": {
        "09": {
          "23": {
            "12": 18382,
            "13": 32423
          },
          "24": {
            "11": 23425433,
            "05": 234252313,
            "04": 2342323
          }
        }
      }
    }
  }
}

d2 = {
    "storageid": "7832484732981421",
    "websites": {
        "google.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "example.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "example.org": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "yahoo.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "bing.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "stackoverflow.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "wikipedia.org": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "github.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "reddit.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "apple.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "microsoft.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "amazon.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "twitter.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "linkedin.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "instagram.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "netflix.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "youtube.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "bing.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "stackoverflow.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "wikipedia.org": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "github.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "reddit.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "apple.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "microsoft.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "amazon.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "twitter.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "linkedin.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "instagram.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "netflix.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "youtube.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "example1.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        },
        "example2.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 38382,
                        "13": 52423
                    },
                    "24": {
                        "11": 43425433,
                        "05": 434252313,
                        "04": 4342323
                    }
                }
            }
        },
        "example3.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 18382,
                        "13": 32423
                    },
                    "24": {
                        "11": 23425433,
                        "05": 234252313,
                        "04": 2342323
                    }
                }
            }
        },
        "example4.com": {
            "2023": {
                "09": {
                    "23": {
                        "12": 28382,
                        "13": 42423
                    },
                    "24": {
                        "11": 33425433,
                        "05": 334252313,
                        "04": 3342323
                    }
                }
            }
        }
        # Add more websites and data here...
    }
}

# Now, you can extract the top 20 websites based on their total values.

    
#print(total_data_bar(d2))