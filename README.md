# convert-hdf5-to-text
Convert the data in a hdf5-formatted file into a series of text files, which are easier to manipulate.

HDF5 files are ]hierarchially structured data files](https://en.wikipedia.org/wiki/Hierarchical_Data_Format). They're analogous to lists in R where every element or "group" in the HDF5 file can have a different structure. While HDF5 files are nice for storing data, it's usually easier to manipulate data when it's stored in delimited text files instead (e.g. csv and tsv files). This script will take each group in an HDF5 file and convert it to a delimited text file format.

## USAGE

The syntax for the script is as follows:

`python3 hdf5_to_csv.py <HDF5 FILE TO CONVERT> <DESIRED SEPERATOR FOR OUTPUT FILES>`

For example:

`python3 hdf5_to_csv.py example.hdf5 tab`

will produce one tab-delimited text file for every data group in the `example.hdf5` file.

To get comma delimited text files, type this instead:

`python3 hdf5_to_csv.py example.hdf5 ,`

Each output file is given the same name as the data group it represents. 
