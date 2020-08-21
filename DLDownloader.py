import requests, os, csv, getpass

# List-related ariables
email = input('Please type in your email address: ')
password = getpass.getpass('Please type in your password: ')
list_type = input('Please select the list type (full, new, deled, fulldns, newdns, deleteddns): ') or 'full'
zone_code = input('Please type in a zone code: ') or 'all_zones'

# File generating variables
desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
filename = f'Domainlists_Zone_{zone_code}_{list_type.capitalize()}.csv'
path = f"{desktop}/{filename}"
url = f"https://domainlists.io/api/{list_type}/{zone_code}/{email}/{password}/"

# Writing .csv
response = requests.get(url)
with open(f'{path}', 'wb') as n:
    r = (response)
    n.write(r.content)
