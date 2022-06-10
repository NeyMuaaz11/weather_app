import requests
def get_weather(query):

    # Generate parameters as a dict
    params = {'key':'f68f78080ffc4dc7863174330202207',
            'q':query}

    # Make an API call using the specified parameters
    r = requests.get("http://api.weatherapi.com/v1/current.json", params = params)

    # Save the returned data as JSON object in the form of a python dict
    data = r.json()
    return data