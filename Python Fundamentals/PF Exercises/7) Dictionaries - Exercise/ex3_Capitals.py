countries = input().split(", ")
cities = input().split(", ")
countries_and_cities = dict(zip(countries, cities))
# countries_and_cities = {country: city for (country, city) in zip(countries, cities)}
for country, city in countries_and_cities.items():
    print(f"{country} -> {city}")
