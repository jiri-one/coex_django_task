from openmeteo_py import Options, OWmanager


def return_temperature(latitude, longitude):
    options = Options(latitude,longitude,current_weather=True)
    mgr = OWmanager(options)
    meteo = mgr.get_data()
    return meteo['current_weather']['temperature']

print(return_temperature(33.9842, -6.8675)) # Latitude, Longitude for Rabat,Morocco
