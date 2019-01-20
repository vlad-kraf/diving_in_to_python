import requests
import pprint

def get_location_info():
    return requests.get("http://api.ipstack.com/check?access_key=dce4b5cc14aa07144f7284fc8dc3348e&format=1").json()

if __name__  == "__main__":
    pprint.pprint(get_location_info())