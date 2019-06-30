from functions import *
import tkinter as tk

# GUI helper vars
ip_list = []
geo_list = []
filtered_geo_list = []


def GUI_parse_file():
    global filename_entry, ip_list, ip_list_lb
    ip_list = parse_file(filename_entry.get())
    '''Update GUI'''
    ip_list_lb.delete(0, ip_list_lb.size())
    for i, ip in enumerate(ip_list, 0):
        ip_list_lb.insert(i, ip)


def GUI_geo_lookup_ips():
    global ip_list, geo_list, geo_ip_results
    geo_list = geo_lookup_ips(ip_list)
    '''Update GUI'''
    for i, geo_data in enumerate(geo_list, 0):
        geo_ip_results.insert(i, geo_data)


def GUI_save_geodata():
    global geo_list, geo_filename_entry
    save_geodata(geo_filename_entry.get(), geo_list)


def GUI_save_filtered_geodata():
    global filtered_geo_list, geo_filename_entry
    save_geodata(geo_filename_entry.get(), filtered_geo_list)


def GUI_load_geodata():
    global geo_list, geo_ip_results, geo_filename_entry
    geo_list = load_geodata(geo_filename_entry.get())
    '''Update GUI'''
    geo_ip_results.delete(0, geo_ip_results.size())
    for i, geo_data in enumerate(geo_list, 0):
        geo_ip_results.insert(i, geo_data)


def GUI_filter_response():
    global geo_list, filtered_geo_list, geo_ip_results, filter_entry
    filtered_geo_list = filter_response(geo_list, filter_entry.get())
    '''Update GUI'''
    geo_ip_results.delete(0, geo_ip_results.size())
    for i, geo_data in enumerate(filtered_geo_list, 0):
        geo_ip_results.insert(i, geo_data)


def GUI_clear_filter():
    global geo_list, filtered_geo_list, geo_ip_results
    filtered_geo_list = []
    '''Update GUI'''
    geo_ip_results.delete(0, geo_ip_results.size())
    for i, geo_data in enumerate(geo_list, 0):
        geo_ip_results.insert(i, geo_data)


top = tk.Tk()
root = tk.Frame(top)
root.pack(side=tk.TOP)
file_label = tk.Label(root, text="File Name:")
file_label.pack(side=tk.LEFT)
filename_entry = tk.Entry(root, bd=5)
filename_entry.pack(side=tk.LEFT)
get_ip_button = tk.Button(root, text="Get IPs", command=GUI_parse_file)
get_ip_button.pack(side=tk.LEFT)
ip_frame = tk.Frame(top)
ip_frame.pack(side=tk.LEFT)
res_frame = tk.Frame(top)
res_frame.pack(side=tk.LEFT)
filter_frame = tk.Frame(top)
filter_frame.pack(side=tk.BOTTOM)
filter_label = tk.Label(filter_frame, text="Query:")
filter_label.pack(side=tk.LEFT)
filter_entry = tk.Entry(filter_frame, bd=5)
filter_entry.pack(side=tk.LEFT)
filter_button = tk.Button(filter_frame, text="Clear Filter", command=GUI_clear_filter)
filter_button.pack(side=tk.BOTTOM)
filter_button = tk.Button(filter_frame, text="Filter Responses", command=GUI_filter_response)
filter_button.pack(side=tk.BOTTOM)
load_button = tk.Button(res_frame, text="Load Responses", command=GUI_load_geodata)
load_button.pack(side=tk.BOTTOM)
save_button = tk.Button(res_frame, text="Save Responses", command=GUI_save_geodata)
save_button.pack(side=tk.BOTTOM)
save_filtered_button = tk.Button(res_frame, text="Save Filtered Responses", command=GUI_save_filtered_geodata)
save_filtered_button.pack(side=tk.BOTTOM)
geo_filename_entry = tk.Entry(res_frame, bd=5)
geo_filename_entry.pack(side=tk.BOTTOM)
file_label = tk.Label(res_frame, text="File Name:")
file_label.pack(side=tk.BOTTOM)
geo_ip_results = tk.Listbox(res_frame, height=20, width=100)
geo_ip_results.pack(side=tk.BOTTOM)
ips_label = tk.Label(ip_frame, text="IP List")
ips_label.pack(side=tk.TOP)
ips_label = tk.Label(res_frame, text="Responses")
ips_label.pack(side=tk.TOP)
ip_list_lb = tk.Listbox(ip_frame, height=20)
ip_list_lb.pack(side=tk.TOP)
geo_lookup_button = tk.Button(ip_frame, text="IP Lookup", command=GUI_geo_lookup_ips)
geo_lookup_button.pack(side=tk.BOTTOM)
top.mainloop()