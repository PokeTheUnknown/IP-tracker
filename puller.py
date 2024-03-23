import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Define the phone number
phone_number = 'YOUR PHONE NUMBER'

# Parse the phone number
the_number = phonenumbers.parse(phone_number)

# Get the location description
your_location = geocoder.description_for_number(the_number, "en")
print(your_location)

# Get the service provider name
service_provider = carrier.name_for_number(the_number, "en")
print(service_provider)

# Initialize OpenCageGeocode with your API key
key = 'e5230236e5fe4f0b8a4d36b14ef60291'
geocoder = OpenCageGeocode(key)

# Query for location details
query = your_location
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
long = results[0]['geometry']['lng']
print(lat, long)

# Create a map
my_map = folium.Map(location=[lat, long], zoom_start=0)

# Add a marker
folium.Marker([lat, long], popup=your_location).add_to(my_map)

# Save the map as HTML
my_map.save("myLoc.html")