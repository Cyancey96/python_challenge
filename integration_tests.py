from functions import *


def test_geo_lookup_ips():
    ip_list = ['1.1.1.1', '2.2.2.2']
    expected_geo_list = [{"ip": "1.1.1.1", "country_code": "AU", "country_name": "Australia", "region_code": "", "region_name": "", "city": "", "zip_code": "", "time_zone": "Australia/Sydney", "latitude": -33.494, "longitude": 143.2104, "metro_code": 0},
                         {"ip": "2.2.2.2", "country_code": "FR", "country_name": "France", "region_code": "", "region_name": "", "city": "", "zip_code": "", "time_zone": "Europe/Paris", "latitude": 48.8582, "longitude": 2.3387, "metro_code": 0}]
    actual_geo_list = geo_lookup_ips(ip_list)
    assert expected_geo_list == actual_geo_list
