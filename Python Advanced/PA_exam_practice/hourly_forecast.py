def forecast(*args):
    result = ""

    my_forecast = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': []
    }

    for location, weather in args:
        my_forecast[weather].append(location)

    for weather, locations in my_forecast.items():
        if locations:
            for location in sorted(locations):
                result += f"{location} - {weather}\n"

    return result
