# Python United Congress API Client

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Support These Projects](#support-these-projects)

## Overview

This is a python API client library that is used to collect data from the
United States Congress and a few other departments inside the US Government.
This library will make filtering the requests easier, and give you a nice easy
to use tool to grab vital civic data to be used in a wide range of analysis.

## Setup

Right now, the library is not hosted on **PyPi** so you will need to do a local
install on your system if you plan to use it in other scrips you use.

First, clone this repo to your local system. After you clone the repo, make sure
to run the `setup.py` file, so you can install any dependencies you may need. To
run the `setup.py` file, run the following command in your terminal.

```console
pip install -e .
```

This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.

## Usage

Here is a simple example of using the `congress` library to pull the bulk data
sources and grabbing a speicifc year of bulk data for the Privacy Act Issuances.

```python
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
```

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding). I'm
always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require me
to pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).
