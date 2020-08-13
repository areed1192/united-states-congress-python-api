from pprint import pprint
from congress.client import Congress

# Initialize the Congress Client.
congress_client = Congress()

# Grab the data sources.
data_sources = congress_client.data_sources()
pprint(data_sources)

# Grab the different resources from the Privacy Act Issuance.
pia_2017 = congress_client.privacy_act_issuances(file='2017')
pprint(pia_2017)


file_names = [
    'resources',
    '2013',
    '2015',
    '2011',
    '2009',
    '2017',
    '2007',
    '2019',
]

for file in file_names:

    # Grab the different resources from the Privacy Act Issuance.
    data_sources = congress_client.privacy_act_issuances(file=file)
    pprint(data_sources)

    # Save the Data.
    congress_client.save_to_json(
        content=data_sources,
        file_name='samples/responses/pia_{file_label}.jsonc'.format(
            file_label=file)
    )
