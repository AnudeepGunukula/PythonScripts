# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
      li=[]
      ck=[]
      li.append(city1.population)
      li.append(city2.population)
      li.append(city3.population) 
      for i in li:
          if i>min_population:
                ck.append(i)
      ck.sort()
      if len(ck)==0:
            return ''
      ans=ck[0]
      if ans==city1.population:
            return city1.name+', '+city1.country
      elif ans==city2.population:
           return city2.name+', '+city2.country
      elif ans==city3.population:
        return city3.name+', '+city3.country
print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""