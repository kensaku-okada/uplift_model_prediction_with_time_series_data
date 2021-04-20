# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import pathlib 
import urllib.request
import sys
import rdata

def download_a_file_from_url(url: str, destination_path):
    urllib.request.urlretrieve(url, destination_path)
    
    
def import_rda_file(import_path, dataframe_name: str):

    parsed = rdata.parser.parse_file(import_path)
    converted = rdata.conversion.convert(parsed)
    return converted[dataframe_name]    

public_file_url: str = "https://github.com/google/GeoexperimentsResearch/raw/master/data/geoassignment.rda"

absolute_dir = pathlib.Path().resolve()
data_name = "geoassignment"
file_name = data_name + ".rda"

destination_path = absolute_dir.parent.joinpath("data", "public_data", file_name)

download_a_file_from_url(public_file_url, destination_path)

public_df = import_rda_file(import_path=destination_path, dataframe_name=data_name)

# -

public_df.head


