# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# define a function updated_damages
def float_damages(damage):
  updated_damages =[]
  for x in damage:
    if "M" in x:
      updated_damages.append(float(x.strip("M"))*1000000)
    elif "B" in x:
      updated_damages.append(float(x.strip("B"))*1000000000)
    else:
      updated_damages.append("Damages not recorded")
  return updated_damages

# Building a dictionary with all Hurricane data
def Huricane_dictionary(name,month,year,max_sustained_wind,area_affected,damage,death):
  Hurricane_List_data = {}
  for i in range(0,33):
    H_sub = {}
    H_sub['Name']= name[i]
    H_sub['Month']= month[i]
    H_sub['Year']= year[i]
    H_sub['Max Sustained Wind']=  max_sustained_wind[i]
    H_sub['Areas Affected']= area_affected[i]
    H_sub['Damage']= damage[i]
    H_sub['Death']= death[i]
    Hurricane_List_data[name[i]] = H_sub
  return Hurricane_List_data
H_by_name = Huricane_dictionary (names,months,years,max_sustained_winds,areas_affected,damages,deaths)
#print(Huricane_dictionary(names,months,years,max_sustained_winds,areas_affected,damages,deaths))
#Hurricane_dict = Huricane_dictionary(names,months,years,max_sustained_winds,areas_affected,damages,deaths)

# Hurricanes per Year function

def data_by_year(data_by_name):
  H_by_year = {}
  for key in data_by_name:
      if data_by_name[key]['Year'] not in H_by_year.keys():
        H_by_year[data_by_name[key]['Year']] = [data_by_name[key]]
      elif data_by_name[key]['Year'] in H_by_year.keys():
        H_by_year[data_by_name[key]['Year']].append(data_by_name[key])
  return H_by_year

# Function to count times per city
def count_times_per_city(cities):
  temp_lst = []
  for i in range(0,len(cities)-1):
    for x in range(0,len(cities[i])-1):
      temp_lst.append(cities[i][x])
  cities_hit_times = {}
  for i in temp_lst:
    cities_hit_times[i] = temp_lst.count(i)
  return cities_hit_times

lst = count_times_per_city(areas_affected)

# Most city hit by Hurricane Function
def max_hit_city(cities):
  greatest_hits = 0
  for record in cities:
    if cities[record] > greatest_hits:
        city_name = record
        greatest_hits = cities[record]
  print ("The greatest hit city is",city_name,"with hits = ", greatest_hits)

# function to get Highest deaths Hurricane
def Highest_H_deaths (H_names,H_deaths):
  Huricane_death_lst = {key:value for key, value in zip(H_names,H_deaths)}
  max_deaths = 0
  for i in Huricane_death_lst:
    if Huricane_death_lst[i] > max_deaths:
        H_death = i
        max_deaths = Huricane_death_lst[i]
  return ("Hurricane", H_death, "Has Highest deaths =", max_deaths)
#print(Highest_H_deaths(names,deaths))

# Rate Hurricanes base on Mortality Scale
def hurricanes_by_mortality(hurricanes):
  mortality = {0: [],1: [], 2: [], 3: [], 4: []}
  for key in hurricanes.keys():
    if hurricanes[key]['Death'] >= 0 and hurricanes[key]['Death'] < 100:
      mortality[0].append(key)
    elif hurricanes[key]['Death'] >= 100 and hurricanes[key]['Death'] < 500:
      mortality[1].append(key)
    elif hurricanes[key]['Death'] >= 500 and hurricanes[key]['Death'] < 1000:
        mortality[2].append(key)
    elif hurricanes[key]['Death'] >= 1000 and hurricanes[key]['Death'] < 10000:
        mortality[3].append(key)
    else:
        mortality[4].append(key)
  return mortality
#print(hurricanes_by_mortality(Hurricane_dict))

# Function to rate Hurricane Damages
updated_damages = float_damages(damages)
Hurricane_dict = Huricane_dictionary(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)
def greatest_damage(hurricanes):
  damage_max = 0
  for key in hurricanes.keys():
    if hurricanes[key]['Damage'] == 'Damages not recorded':
      continue
    elif hurricanes[key]['Damage'] > damage_max:
      greatest_hurricane = key
      damage_max = hurricanes[key]['Damage']
  return ("Greatest Hurricance damage done by", greatest_hurricane," with ", damage_max, "dollars")

#print(greatest_damage(Hurricane_dict))

def rate_by_damage(hurricanes):
  hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: []}
  for key in hurricanes.keys():
    if hurricanes[key]['Damage'] == "Damages not recorded":
      continue
    elif hurricanes[key]['Damage'] >= 0 and hurricanes[key]['Damage'] < 100000000:
      hurricanes_by_damage[0].append(key)
    elif hurricanes[key]['Damage'] >= 100000000 and hurricanes[key]['Damage'] < 1000000000:
      hurricanes_by_damage[1].append(key)
    elif hurricanes[key]['Damage'] >= 1000000000 and hurricanes[key]['Damage'] < 10000000000:
      hurricanes_by_damage[2].append(key)
    elif hurricanes[key]['Damage'] >= 10000000000 and hurricanes[key]['Damage'] < 50000000000:
      hurricanes_by_damage[3].append(key)
    else:
      hurricanes_by_damage[4].append(key)
  return hurricanes_by_damage

#print(rate_by_damage(Hurricane_dict))

















     





