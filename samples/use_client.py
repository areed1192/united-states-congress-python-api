import json

from pprint import pprint
from congress.client import Congress

with open(file='samples/fields/fields_org.jsonc', mode='r') as fields_file:
    fields_table = json.load(fp=fields_file)

# Initialize the Congress Client.
congress_client = Congress()

# Grab the database resources.
data_sources = congress_client.data_sources()
pprint(data_sources)

# Grab the Folder Resource for the Privacy Act Issuance Resource for 2017.
pia_2017 = congress_client.privacy_act_issuances(
    folder='2017'
)
pprint(pia_2017)

# Grab the Folder Resource for the Code of Federal Regulations Resource for 2020.
cfr_2020 = congress_client.code_of_federal_regulations(
    folder='2020'
)
pprint(cfr_2020)

# Grab the Folder Resource for the Federal Register Resource for 2020.
fr_2020 = congress_client.federal_register(
    folder='2020'
)
pprint(fr_2020)

# Grab the Folder Resource for the Bill Status Resource for 116.
bill_status_116 = congress_client.bill_status(
    folder='116'
)
pprint(bill_status_116)

# Grab the Folder Resource for the Commerce Business Daily Resource for 2001.
cbd_2001 = congress_client.commerce_business_daily(
    folder='2001'
)
pprint(cbd_2001)

# Grab the Folder Resource for the Public Papers of the Presidents of the United States Resource for 2014.
ppp_2014 = congress_client.public_papers_president(
    folder='2014'
)
pprint(ppp_2014)

# Grab the Folder Resource for the Supreme Court Decisions Resource for 1937.
scd_1937 = congress_client.supreme_court_decisions(
    folder='1937'
)
pprint(scd_1937)

# Grab the Folder Resource for the Congressional Bills Resource for 116.
bills_116 = congress_client.congressional_bills(
    folder='116'
)
pprint(bills_116)

# Grab the Folder Resource for the United States Government Manual Resource for 2019.
govman_2019 = congress_client.us_government_manuals(
    folder='2019'
)
pprint(govman_2019)

# Grab the Folder Resource for the Bill Summary Resource for 116.
billsum_116 = congress_client.bill_summaries(
    folder='116'
)
pprint(billsum_116)

# Grab the Folder Resource for the Electronic Code of Federal Regulations Resource for Title 50.
ecfr_title_50 = congress_client.electronic_code_of_federal_regulation(
    folder='title-50'
)
pprint(ecfr_title_50)

# Grab the Folder Resource for the House Rules and Manual Resource for 116.
hman_116 = congress_client.house_rules_and_manual(
    folder='116'
)
pprint(hman_116)

# Grab the Folder Resource for the Public and Private Laws (xml uslm beta) Resource for 116.
plaw_116 = congress_client.private_and_public_laws(
    folder='116'
)
pprint(plaw_116)

# Grab the Folder Resource for the Statutes at Large (xml uslm beta) Resource for 117.
statute_117 = congress_client.statutes_at_large(
    folder='117'
)
pprint(statute_117)
