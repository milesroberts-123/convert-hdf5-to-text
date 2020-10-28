import h5py
import numpy as np
import pandas as pd
import sys

#Parse input arguments
name = sys.argv[1]
seperator = sys.argv[2]

if seperator == "tab":
	seperator = "\t"

#Read in dataset
dataset = h5py.File(name, 'r')
groups = list(dataset.keys())

print("These are the groups in %s" % name)
print(groups)

print("Saving the data in individual groups as text files...")
for group in groups:
	print("Reading data in %s..." % group)
	df = pd.DataFrame(np.array(dataset[group])) #Convert group to numpy array, then pandas dataframe
	print("Writing data in %s..." % group)
	df.to_csv(group + ".txt", sep=seperator) #Write dataframe to text file

