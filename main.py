#importing libraries
import pandas as pd
import ssl

#GATHERING DATA AND APPENDING 

tabNo = [6, 8, 6, 7, 6, 6, 7, 7, 8, 10, 7, 6, 7, 9, 7, 7, 6, 9, 7, 5, 7, 8]
riderNo = [93, 1, 5, 10, 12, 20, 21, 23, 33, 35, 36, 42, 49, 54, 63, 72, 73, 79, 88, 43, 25, 37]
riderName = ["Marc Marquez", "Jorge Martin", "Johann Zarco", "Luca Marini", "Maverick Vinales", "Fabio Quartararo", "Franco Morbidelli", "Enea Bastianini", "Brad Binder", "Somkiat Chantra", "Joan Mir", "Alex Rins", "Fabio Di Giannantonio", "Fermin Aldeguer", "Francesco Bagnaia", "Marco Bezzecchi", "Alex Marquez", "Ai Ogura", "Miguel Oliveira", "Jack Miller", "Raul Fernandez", "Pedro Acosta"]
riderCountry = ["Spain", "Spain", "France", "Italy", "Spain", "France", "Italy", "Italy", "South Africa", "Thailand", "Spain", "Spain", "Italy", "Spain", "Italy", "Italy", "Spain", "Japan", "Portugal", "Australia", "Spain", "Spain"]

tbRiders = pd.DataFrame()

# to find table number in the wikipedia page
# wiki = pd.read_html('https://en.wikipedia.org/wiki/Jorge_Martin')
# for i in range(0,15):
#     print("##################################",i)
#     print(wiki[i])


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




tbRiders.to_excel("C:/Mayura/Projects/MotoGP/RiderDetails.xlsx", index=False)