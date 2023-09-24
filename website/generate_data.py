from flask import Flask, render_template
import json


def bubble_sort_top_20(input_dict):
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
        # Stop execution and return only the top 20 items
        if i == 19:
            return dict(items[:20])

    # Return the top 20 items
    return dict(items[:20])


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
        
    # sort the dictionary by value of mins in descending order. Only need to get the top 20 so use bubble sort
    out_dict = bubble_sort_top_20(out_dict)
    
    # make a list of unique colors for each bar (website) in the graph
    # Top 20 websites
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'grey', 'black',
          'lightblue', 'lime', 'cyan', 'magenta', 'teal', 'gold', 'navy', 'indigo', 'silver', 'olive']

    """
    datasets = [{
        "label": "Time spent on websites (mins)",
        "backgroundColor": 'rgba(75, 192, 192, 0.2)',
        "borderColor": 'rgba(75, 192, 192, 1)',
        "borderWidth": 1,
        "data": list(out_dict.values())
    }]

    return {"labels": list(out_dict.keys()), "datasets": datasets}
    """

    return {"labels": list(out_dict.keys()), "datasets": [{"label": "Time spent on websites (mins)", "data": list(out_dict.values()), "backgroundColor": colors}]}

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