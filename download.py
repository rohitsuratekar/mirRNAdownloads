#Downloads DIANA-microT-CDS  hits from given list of miRNA ids. 

import numpy as np
import pandas as pd
import requests

threshold = '0.7'
#Input file name
#First column of input file should be miRNA names
nameList = 'sample_list.csv' 

rawMatrix= pd.read_csv(nameList, header=None)
nameArray = np.asarray(rawMatrix[0])  
for currentID in nameArray:
	isThere = 0
	pre_url = 'http://diana.imis.athena-innovation.gr/DianaTools/index.php?r=download/microT_CDS&genes=&mirnas='
	post_url = '&descr=&threshold='
	url = pre_url+currentID+post_url+threshold
	filename = "%s.csv"%(currentID)
	try:
		results = requests.get(url)
		if results.status_code == 200:
			with open(filename, 'wb') as raw:
				raw.write(results.content)
			isThere = 1
		else:
			print("No result found with : %s"%(currentID))

	except ValueError:
		pass

	if (isThere==1):
		f = open(filename,"r")
		lines = f.readlines()
		f.close()
		f = open(filename,"w")
		for line in lines:
			if line.startswith("ENST"):  #Takes only content which starts with "ENST"
				f.write(line)
		f.close()




