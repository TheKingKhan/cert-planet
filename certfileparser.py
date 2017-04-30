file = open("certinfo.txt", "r")
countryLimit = 246
orgLimit = 20
countries = []
numCountries = 0
file.readline()
for line in file:
	split = line.split("=")
	if split[0]=='issuer':
		pass	
	else:
		if split[0][4:15]=='countryName':
			country = split[1][:-1]
			orgname = next(file)
			split2 = orgname.split("=")
			org = split2[1][:-1]
			if country in countries:
				for i in range(len(countries)):
					if countries[i]==country:
						countries[i+1].append(org)
					else:
						pass
			
			else:
				numCountries+=1
				countries.append(country)
				countries.append([])
				countries[numCountries*2-1].append(org)

output = open("cert.txt", "r+")
for i in range(len(countries)):
	if type(countries[i]) is str:
		output.write(countries[i][1:] + ":")
		for org in countries[i+1]:
			output.write(org + ":")
		output.write("\n")

	else:
		pass	


print countries	
