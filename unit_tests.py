import os
from functions import *


def test_parse_file():
    expected_ip_list = ['244.36.171.60', '241.189.201.17', '153.199.153.228']
    actual_ip_list = parse_file("TESTFILE_IPS.txt")
    assert actual_ip_list == expected_ip_list


def test_save_geodata():
    filename = "TESTFILE_SAVE.txt"
    geo_data = [{"ip": "244.36.171.60", "country_code": "", "country_name": "", "region_code": "", "region_name": "", "city": "", "zip_code": "", "time_zone": "", "latitude": 0, "longitude": 0, "metro_code": 0},
                {"ip": "81.44.150.240", "country_code": "ES", "country_name": "Spain", "region_code": "AN", "region_name": "Andalusia", "city": "Villaverde del Rio", "zip_code": "41318", "time_zone": "Europe/Madrid", "latitude": 37.5892, "longitude": -5.8744, "metro_code": 0},
                {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}]
    save_geodata(filename, geo_data)
    file = open(f"Files/{filename}", 'r')
    assert json.load(file) == geo_data
    '''Clean Up'''
    file.close()
    os.remove(f"Files/{filename}")


def test_load_geodata():
    filename = "TESTFILE_LOAD.txt"
    expected_geo_data = [{"ip": "244.36.171.60", "country_code": "", "country_name": "", "region_code": "", "region_name": "", "city": "", "zip_code": "", "time_zone": "", "latitude": 0, "longitude": 0, "metro_code": 0},
                {"ip": "81.44.150.240", "country_code": "ES", "country_name": "Spain", "region_code": "AN", "region_name": "Andalusia", "city": "Villaverde del Rio", "zip_code": "41318", "time_zone": "Europe/Madrid", "latitude": 37.5892, "longitude": -5.8744, "metro_code": 0},
                {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}]
    actual_geo_data = load_geodata(filename)
    assert actual_geo_data == expected_geo_data


def test_filter_query_equal_string():
    query = "country_name=Switzerland"
    geo_data = {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}
    assert filter_query(geo_data, query)


def test_filter_query_not_equal_string():
    query = "country_name!=SWEETzerland"
    geo_data = {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}
    assert filter_query(geo_data, query)


def test_filter_query_equal_float():
    query = "longitude=8.5546"
    geo_data = {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}
    assert filter_query(geo_data, query)


def test_filter_query_not_equal_float():
    query = "longitude!=10.0"
    geo_data = {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}
    assert filter_query(geo_data, query)


def test_filter_query_less_than():
    query = "longitude<10"
    geo_data = {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}
    assert filter_query(geo_data, query)


def test_filter_query_greater_than():
    query = "latitude>10"
    geo_data = {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}
    assert filter_query(geo_data, query)


def test_filter_query_greater_than_or_equal():
    query1 = "latitude>=10"
    query2 = "latitude>=47.3664"
    geo_data = {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH",
                "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich",
                "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}
    assert filter_query(geo_data, query1)
    assert filter_query(geo_data, query2)


def test_filter_query_less_than_or_equal():
    query1 = "latitude<=100"
    query2 = "latitude<=47.3664"
    geo_data = {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH",
                "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich",
                "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}
    assert filter_query(geo_data, query1)
    assert filter_query(geo_data, query2)


def test_simple_filter_response():
    query = "country_name!=Spain"
    geo_data = [{"ip": "244.36.171.60", "country_code": "", "country_name": "", "region_code": "", "region_name": "", "city": "", "zip_code": "", "time_zone": "", "latitude": 0, "longitude": 0, "metro_code": 0},
                {"ip": "81.44.150.240", "country_code": "ES", "country_name": "Spain", "region_code": "AN", "region_name": "Andalusia", "city": "Villaverde del Rio", "zip_code": "41318", "time_zone": "Europe/Madrid", "latitude": 37.5892, "longitude": -5.8744, "metro_code": 0},
                {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}]
    expected_geo_data = [{"ip": "244.36.171.60", "country_code": "", "country_name": "", "region_code": "", "region_name": "", "city": "", "zip_code": "", "time_zone": "", "latitude": 0, "longitude": 0, "metro_code": 0},
                         {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}]
    actual_geo_data = filter_response(geo_data, query)
    print(actual_geo_data)
    assert expected_geo_data == actual_geo_data


def test_complex_filter_response():
    query = "ip!=244.36.171.60:latitude<50:latitude<=47.3664:longitude>-6:longitude>=-5.8744:zip_code>8002"
    geo_data = [{"ip": "244.36.171.60", "country_code": "", "country_name": "", "region_code": "", "region_name": "", "city": "", "zip_code": "", "time_zone": "", "latitude": 0, "longitude": 0, "metro_code": 0},
                {"ip": "81.44.150.240", "country_code": "ES", "country_name": "Spain", "region_code": "AN", "region_name": "Andalusia", "city": "Villaverde del Rio", "zip_code": "41318", "time_zone": "Europe/Madrid", "latitude": 37.5892, "longitude": -5.8744, "metro_code": 0},
                {"ip": "40.82.106.5", "country_code": "CH", "country_name": "Switzerland", "region_code": "ZH", "region_name": "Zurich", "city": "Zurich", "zip_code": "8002", "time_zone": "Europe/Zurich", "latitude": 47.3664, "longitude": 8.5546, "metro_code": 0}]
    expected_geo_data = [{"ip": "81.44.150.240", "country_code": "ES", "country_name": "Spain", "region_code": "AN", "region_name": "Andalusia", "city": "Villaverde del Rio", "zip_code": "41318", "time_zone": "Europe/Madrid", "latitude": 37.5892, "longitude": -5.8744, "metro_code": 0}]
    actual_geo_data = filter_response(geo_data, query)
    print(actual_geo_data)
    assert expected_geo_data == actual_geo_data
