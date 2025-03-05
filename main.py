#importing libraries
import pandas as pd
import ssl

# to find table number in the wikipedia page
# wiki = pd.read_html('https://en.wikipedia.org/wiki/Jorge_Martin')
# for i in range(0,15):
#     print("################################## Table: ",i)
#     print(wiki[i])

#GATHERING DATA AND APPENDING 
tabNo = [6, 8, 6, 7, 6, 6, 7, 7, 8, 10, 7, 6, 7, 9, 7, 7, 6, 9, 7, 5, 7, 8]
riderNo = [93, 1, 5, 10, 12, 20, 21, 23, 33, 35, 36, 42, 49, 54, 63, 72, 73, 79, 88, 43, 25, 37]
riderName = ["Marc Marquez", "Jorge Martin", "Johann Zarco", "Luca Marini", "Maverick Vinales", "Fabio Quartararo", "Franco Morbidelli", "Enea Bastianini", "Brad Binder", "Somkiat Chantra", "Joan Mir", "Alex Rins", "Fabio Di Giannantonio", "Fermin Aldeguer", "Francesco Bagnaia", "Marco Bezzecchi", "Alex Marquez", "Ai Ogura", "Miguel Oliveira", "Jack Miller", "Raul Fernandez", "Pedro Acosta"]
riderCountry = ["Spain", "Spain", "France", "Italy", "Spain", "France", "Italy", "Italy", "South Africa", "Thailand", "Spain", "Spain", "Italy", "Spain", "Italy", "Italy", "Spain", "Japan", "Portugal", "Australia", "Spain", "Spain"]

tbRiders = pd.DataFrame()

for i in range(0,len(tabNo)):
    try:
        wiki = pd.read_html("https://en.wikipedia.org/wiki/"+riderName[i].replace(' ', '_'))
    except:
        try:
            wiki = pd.read_html("https://en.wikipedia.org/wiki/"+riderName[i].replace(' ', '_')+"_(motorcyclist)")
        except:
            print("")

    appTab = wiki[tabNo[i]] #Assign the required table to temp variable
    appTab.insert(0, "Number", riderNo[i]) #Add additional rider info
    appTab.insert(1, "Rider Name", riderName[i]) #Add additional rider info
    appTab.insert(2, "Home Country", riderCountry[i]) #Add additional rider info
    appTab = appTab.iloc[:-1] #Remove last row of totals from each table

    tbRiders = pd.concat([tbRiders, appTab], ignore_index=True)#append the table to actual df


#CLEANING DATA

#Renaming the columns
tbRiders = tbRiders.rename(columns = {'Number': 'bike_number', 'Rider Name': 'rider_name', 'Home Country': 'home_country', 'Season': 'season', 'Class': 'class', 'Motorcycle': 'motercycle', 'Team': 'team', 'Race': 'races_participated', 'Win': 'wins', 'Podium': 'podium', 'Pole': 'pole', 'FLap': 'fastest_lap', 'Pts': 'points', 'Plcd': 'placed', 'WCh': 'world_championships'})

#Cleaning column values
# tbRiders['points'] = tbRiders['points'].replace({'0*': '0'})
tbRiders['points'] = tbRiders['points'].astype(str).str.extract('(\\d+)').astype(float).astype('Int64')
tbRiders['placed'] = tbRiders['placed'].astype(str).str.extract('(\\d+)').astype(float).astype('Int64')
# .astype(str) makes all values to string before processing
# .str.extract('(\d+)') extracts only numeric digits
# .astype(float).astype('Int64') converts the extracted number into an integer while handling NaNs
tbRiders['placed'] = tbRiders['placed'].fillna(0)
tbRiders['world_championships'] = tbRiders['world_championships'].where(tbRiders['world_championships'] == '1', '0')

#Assigning datatypes
tbRiders['season'] = tbRiders['season'].astype(int)
tbRiders['points'] = tbRiders['points'].astype(int)
tbRiders['world_championships'] = tbRiders['world_championships'].astype(int)

#Reordering the column names
cols = list(tbRiders.columns)
cols.insert(2, cols.pop(4))  
cols.insert(3, cols.pop(4))
tbRiders = tbRiders[cols]

#Sorting the columns
tbRiders = tbRiders.sort_values(by=['bike_number', 'season'])


tbRiders.to_csv("C:/Mayura/Projects/MotoGP-DataAnalysis/RiderDetails.csv", index=False)