from geopy.geocoders import Photon

def get_lat_lon(country_name):
    geolocator = Photon(user_agent="geoapiExercises")
    location = geolocator.geocode(country_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None
