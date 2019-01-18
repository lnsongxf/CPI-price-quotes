#STAGE 1 CREATE MASTER DATABASE


#to begin we need to import all the csv files 
#will have all the promblatic observations, we need to save this dataset as a python file 
#need to run the code below in jupter notebook 

#import pandas as pd
#year = []
#month = []
#for j in (2017, 2018):
 #   for i in range(1,13) : 
        #dataFile1 = pd.read_csv("dataset/price_quote_%d_%02d.csv" %(j, i))
        #month.append(dataFile1) #this will append after every cycle
        
      #  print("dataset/price_quote_%d_%02d.csv" %(j, i)) #this checks that the logic for the above is correct. 
      

#master = pd.concat(year) #here we are appending the all the data which is being held in multiple different dataframes. 
# we obviously want to have this in a single appended dataframe 

#CHECK THAT NUMBERS MATCH STATA OUTPUT 
#master.count()

#master.to_pickle("dataset/2018_1_MASTER_UKpricequotes.pkl")

#master[["QUOTE_DATE", "ITEM_ID", "ITEM_DESC" , "PRICE", "REGION", "SHOP_TYPE" ]] # this will only keep the variables you want. 
# we don't want that at this stage, since we want to save the full thing. 
