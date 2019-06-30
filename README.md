# python_challenge

How to run:
Put any files you want the program to be able to save/load to in the Files folder.  Run main.py using Python 3.7

Provided Files:

TESTFILE_IPS.txt - Used by unit tests

TESTFILE_LOAD.txt - Used by unit tests

list_of_ips.txt - Text file containing 5000 IPs.  Load IPs into the program with the "Get IPs" button.

list_of_ips_RESULTS.txt - Text file containing responses for IPs in list_of_ips.txt.  Load into the program using "Load 
Responses" to skip the IP Lookup process.

small_list_of_ips.txt - Text file containing 100 IPs.  I recommend using this file if you want to try out IP Lookup.


Navigating the UI:

Get IPs- Located at the top of the UI.  Clicking this button will check the Files folder for a file with the same name in the box left to the button and populate the IP List with any IPs found in the file.

IP Lookup- Located at the left of the UI.  Clicking this button will look up Geo IP data for all IPs in the list.  Progress can be checked from the terminal window.  Results are populated in the Responses list.

Save/Load Responses- 3 buttons located at the bottom of the UI.  "Load Responses" will load a file from the Files folder into the Responses list.  "Save Filtered Responses" will save a list of filtered responses to a file if a filter is applied.  "Save Responses" will save all responses to to a file, including filtered responses.  The file used by these buttons is specified using the textbox above them.

Filter Responses- Located in the bottom-right of the UI.  Clicking this will filter out responses from the Responses list using a Query provided in the textbox to the left of the button.  These responses can be saved using the "Save Filtered Responses" button.  See below for Query Language details.

Clear Filter- Located in the bottom-right of the UI.  Clicking this will remove a filter and display the original list of responses in the Responses window.

Query Language:

Grammar - <key><operator><value>:<key><operator><value>
  
':' is used to seperate statements.

Operators:

'='- Equals, can be used with strings and numbers

'!='- Not equals, can be used with strings and numbers

'<'- Less than, can be used with numbers

'>'- Greater than, can be used with numbers

'<='- Less than or equal, can be used with numbers

'>=' Greater than or equal, can be used with numbers


Query Language Examples:

"ip=1.1.1.1"- Filters responses with an ip of "1.1.1.1"

"country_code!=JP:latitude<0"- Filters responses with a latitude less than 0 if JP is not their country_code

"country_code=US:zip_code=:longitude>=0" - Filters responses with a country_code of "US", a blank zip code, and a longitude greater than or equal to 0.


Running Unit/Integration Tests:

You can get pytest using "pip install pytest".  You can run unit tests using "pytest unit_tests.py" and you can run integration tests using "pytest integration_tests.py".
