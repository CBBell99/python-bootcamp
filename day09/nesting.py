# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a dictionary

travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ['Berlin', 'Hamburg', 'Stuttgart']
}

# nesting a dict in a dict

travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        'total_visits': 12
        },
    "Germany":{"cities_visited":['Berlin', 'Hamburg', 'Stuttgart'], "total_visits": 12}
}

travel_log3 = [
{
    'country':"France",
    "cities_visited": ["Paris", "Lille", "Dijon"], 
        'total_visits': 12
},
{
    'country':"Germany","cities_visited":['Berlin', 'Hamburg', 'Stuttgart'], "total_visits": 12
}
]
