def city_country(city, country):
        """Returns a formatted, country and its city"""
        country = f"'{city.title()}, {country.title()}'"
        return country

my_city = city_country('kampala', 'uganda')
print(my_city)
my_city = city_country('kigal', 'rwanda')
print(my_city)
my_city = city_country('nairobi', 'kenya')
print(my_city)
