import geoip2.database
import os

GEO_DB = "GeoLite2-City.mmdb"  
BLOCKED_COUNTRIES = ["CN", "RU", "KP"]

def is_geo_blocked(ip):
    if not os.path.exists(GEO_DB):
        return False
    try:
        reader = geoip2.database.Reader(GEO_DB)
        response = reader.city(ip)
        country = response.country.iso_code
        return country in BLOCKED_COUNTRIES
    except:
        return False
