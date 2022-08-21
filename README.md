# **COex Backend Test Day**
Objectives:
- [X] Create an application in Django using any packages/libraries
- [X] version all source code using GIT
- [X] design a database model to store the imported data in the next step
- [X] Let the categories (Category column) be implemented as a linked model
- [X] create a management command to import data from the supplied file
- [X] create output/listing of internal IDs and names of all locations using
    - [X] a) REST endpoint (preferred - ideally DRF and JSON format)
    - [X] b) Django Views
- [X] add filtering to the page/endpoint by category and whether the location is available with a dog
- [X] create a page/endpoint to display complete data for one location
- [X] create a way to add comments to each location
- [X] create a page with the statistics of the places that are stored in the DB
    - [X] Number of places
    - [X] an overview of the categories and the number of sites in each category
    - [X] the site with the most comments
    - [X] farthest place from the centre of the country
    - [X] number/estimate of English places
- [X] on the page/endpoint listing all places, add the current temperature for each place in degrees Celsius (use API from https://open-meteo.com/ for example)
    - [X] the page should have a mechanism/cache that will query the data only 1 per hour (preventing repeated requests that return the same value)

**Assignment Notes:**
- admin login via `coex:coex`
- admin commands are: `temperature_update`, `temperature_update_async` and `reimport_csv`
- you will need your own secret key, just run `python utils/new_secret_key.py`
- cache refresh is set to 2 hours
- For the purposes of this example only, the admin command `temperature_update` uses the `openmeteo_py` library, while `temperature_update_async` uses the `httpx` library
