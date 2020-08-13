import json
import bisect

from typing import List
from congress.client import Congress


# Load the old Fields File from Power Query.
with open(file='samples/fields/fields.jsonc', mode='r') as data_file:
    fields_table = json.load(fp=data_file)

# Initialize the New Dictionary.
fields_dict = {}

# Loop through each row.
for row in fields_table:

    topic = row['Endpoint']
    endpoint = row['File_Name']

    # See if the current endpoint is in our Fields Dict.
    if topic not in fields_dict:

        # If it's not add the new endpoint, and set the other fields.
        fields_dict[topic] = {}
        fields_dict[topic]['endpoints']: List = []
        fields_dict[topic]['paths']: List = []
        fields_dict[topic]['arguments']: List = []

    # Add the endpoints.
    fields_dict[topic]['endpoints'].append(row)

    # Create a File Dict.
    file_dict = {
        'file_name': 'samples/responses/{topic}/{endpoint}.jsonc'.format(topic=topic, endpoint=endpoint),
        'arguments': endpoint
    }

    # Add the Files Path.
    fields_dict[topic]['paths'].append(file_dict)
    bisect.insort(fields_dict[topic]['arguments'], endpoint)

# Dump the data to the Fields Organized File.
with open(file='samples/fields/fields_org.jsonc', mode='w+') as data_file:
    json.dump(obj=fields_dict, fp=data_file, indent=2)

# Initialize the Congress Client.
congress_client = Congress()

# Loop through each Path Resource.
for path_resource in fields_table['STATUTE']['paths']:

    # Grab the Folder Name and File Name
    folder = path_resource['arguments']
    file_name = path_resource['file_name']

    # Grab the data.
    data_sources = congress_client.statutes_at_large(folder=folder)

    # Save the Data.
    congress_client.save_to_json(
        content=data_sources,
        file_name=file_name
    )