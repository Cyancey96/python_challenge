import sys
import re
import json
import urllib.error as er
import urllib.request as req



'''Parses IPs from a filename into a list of IPs'''
def parse_file(filename):
    file = open(f"Files/{filename}")
    file_string = file.read()
    r = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    return r.findall(file_string)


'''Populates Geo IP data into geo_list using IPs in ip_list'''
def geo_lookup_ips(list_of_ips):
    geolist = []
    error_list = []
    base_url = "https://freegeoip.app"
    response_type = "json"
    counter = 0
    # First run
    for ip in list_of_ips:
        counter += 1
        try:
            res = json.loads(response(base_url, response_type, ip))
        except er.HTTPError:
            print(f'{counter}/{len(list_of_ips)}: Error retrieving info for ip: {ip}', file=sys.stderr)
            error_list.append(ip)
        else:
            geolist.append(res)
            print(f'{counter}/{len(list_of_ips)}: Success retrieving info for ip: {ip}')
    # Retry getting info for ips that failed
    while len(error_list) > 0:
        counter = 0
        original_error_list_len = len(error_list)
        for ip in error_list:
            counter += 1
            try:
                res = json.loads(response(base_url, response_type, ip))
            except er.HTTPError:
                print(f'{counter}/{original_error_list_len}: Error retrieving info for ip: {ip}', file=sys.stderr)
            else:
                error_list.remove(ip)
                geolist.append(res)
                print(f'{counter}/{original_error_list_len}: Success retrieving info for ip: {ip}')
    return geolist


'''Returns response for an api call'''
def response(base_url, response_type, ip_address):
    with req.urlopen(f'{base_url}/{response_type}/{ip_address}') as res:
        return res.read()

'''Saves geodata to a file with the name in geo_filename_entry'''
def save_geodata(filename, geo_data):
    file = open(f"Files/{filename}", 'w')
    json.dump(geo_data, file)


'''Loads geodata from a file with the name in geo_filename_entry'''
def load_geodata(filename):
    file = open(f"Files/{filename}", 'r')
    return json.load(file)


'''Filters geo_list and stores results in filtered_geo_list and updates filtered results to GUI'''
def filter_response(geo_data, query_string):
    return list(filter(lambda x: filter_query(x, query_string), geo_data))


'''Contains logic for filtering geo_data using a query stored in filter_entry'''
def filter_query(geo_data, query_string):
    filter_bool = True
    queries = re.split(":", query_string)
    for query in queries:
        keyvals = re.split("(!=|<=|>=|<|>|=)", query)
        try:
            if keyvals[0] not in geo_data:
                filter_bool = False
            elif keyvals[1] == "<" and float(geo_data[keyvals[0]]) >= float(keyvals[2]):
                filter_bool = False
            elif keyvals[1] == ">" and float(geo_data[keyvals[0]]) <= float(keyvals[2]):
                filter_bool = False
            elif keyvals[1] == "<=" and float(geo_data[keyvals[0]]) > float(keyvals[2]):
                filter_bool = False
            elif keyvals[1] == ">=" and float(geo_data[keyvals[0]]) < float(keyvals[2]):
                filter_bool = False
            elif keyvals[1] == "!=" and float(geo_data[keyvals[0]]) == float(keyvals[2]):
                filter_bool = False
            elif keyvals[1] == "=" and float(geo_data[keyvals[0]]) != float(keyvals[2]):
                filter_bool = False
        except ValueError:
            try:
                if keyvals[1] == "!=" and geo_data[keyvals[0]] == keyvals[2]:
                    filter_bool = False
                elif keyvals[1] == "=" and geo_data[keyvals[0]] != keyvals[2]:
                    filter_bool = False
            except ValueError:
                print(f"ValueError: {geo_data[keyvals[0]]}", file=sys.stderr)
                filter_bool = False
    return filter_bool
