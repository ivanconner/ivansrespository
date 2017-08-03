import matplotlib.pyplot as plt
import os.path
import dateutil.parser
import datetime
import numpy as np
   
# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))  

# initialize the aggregators
lenders=[]

# Open the file
filename = os.path.join(directory, '2014_Foreclosures.csv')
datafile = open(filename,'r')

# Search for all the occurrences of each bank on the file.
for line in datafile:     
    regis, proptype,lender = line.split(',')
  
    if 'Bank of America' in lender:
            lenders+=[1]       
    if 'Wells Fargo Bank N.A.'in lender:
            lenders+=[2] 
    if 'JP Morgan Chase NA' in lender:
            lenders+=[3]       
    if 'Capital One'in lender:
            lenders+=[4] 
    if 'Ocwen Loan Servicing  LLC' in lender:
            lenders+=[5]       
    if 'Nationstar Mortgage LLC'in lender:
            lenders+=[6]  
            
# Close the file
datafile.close()
    
# Set of text values used to label the x axis.
text_values = ["BofA", "WF", "Chase", "CapOne", "Ocwen", "NatStar"]

# Create 6 bins to put each bank's data in (7 is the end of the range of 
# bins and thus not included in the total count of actual bins). Displace the 
# bins half a graduation to the left.
bins = np.arange(7) + 0.5

# Label the x axis with ticks and their associated values. Displace them one half
# a graduation to the right.
plt.xticks(bins + 0.5, text_values)

# Create the histograms using data from the lenders list and using bins with the
# attributes that follow. 
plt.hist(lenders, bins, histtype='bar', rwidth=.5)

# Label the x axis
plt.xlabel('Banks')

# Label the y axis
plt.ylabel('Number of Foreclosures')

# Include a tittle.
plt.title('2014 Foreclosures of Leading Banks')
plt.show()