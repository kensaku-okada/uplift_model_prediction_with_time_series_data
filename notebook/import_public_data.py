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

import sys
import pathlib 
import urllib.request
import sys
import rdata
import feather
import pyreadr


# +
def download_a_file_from_url(url: str, destination_path):
    urllib.request.urlretrieve(url, destination_path)

def import_rda_file_by_rdata(import_path, dataframe_name: str):
    parsed = rdata.parser.parse_file(import_path)
    converted = rdata.conversion.convert(parsed)
    return converted[dataframe_name]    

def import_external_file_as_dataframe(public_file_url, data_name, extension, import_method="feather"):

    absolute_dir = pathlib.Path().resolve()
    file_name = data_name + extension
    destination_path = absolute_dir.parent.joinpath("data", "public_data", file_name)
    download_a_file_from_url(public_file_url, destination_path)
    
    if (import_method == "rdata"):
        return import_rda_file_by_rdata(import_path=destination_path, dataframe_name=data_name)

#     this case returns error "ArrowInvalid: Not a Feather V1 or Arrow IPC file" when the file format is not feather
    elif (import_method == "feather"):
        return feather.read_dataframe(destination_path)[data_name]

    elif (import_method == "pyreadr"):
        return pyreadr.read_r(str(destination_path))[data_name]

    else:
        print("not registered import method. returns None")
        sys.exit(0)



# +
public_file_url: str = "https://github.com/google/GeoexperimentsResearch/raw/master/data/geoassignment.rda"
# import_method = "rdata" # failed
# import_method = "feather" # failed
import_method = "pyreadr" # succeeded!

geoassignment_df = import_external_file_as_dataframe(
    public_file_url, 
    data_name="geoassignment", 
    extension=".rda", 
    import_method=import_method)
print(geoassignment_df)
# -


geoassignment_df.head

public_file_url: str = "https://github.com/google/GeoexperimentsResearch/raw/master/data/salesandcost.rda"
salesandcost_df = import_external_file_as_dataframe(
    public_file_url, 
    data_name="salesandcost", 
    extension=".rda", 
    import_method=import_method)



salesandcost_df.head


