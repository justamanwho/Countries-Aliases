import pycountry
import json

aliases = dict()
print(list(pycountry.countries))

with open('the-world.txt', 'r', encoding='utf-8') as the_world:

    independent_countries = [country.strip() for country in the_world.readlines()]

    for country in independent_countries:
        try:
            country_data = pycountry.countries.search_fuzzy(country)[0]

            alpha_2, alpha_3 = country_data.alpha_2, country_data.alpha_3
            aliases[country] = [alpha_2, alpha_3]

            name = country_data.name if country != country_data.name else None
            if name:
                aliases[country].append(name)

            try:
                common_name = country_data.common_name if country_data.common_name != country else None
                if common_name:
                    aliases[country].append(common_name)
            except AttributeError:
                pass

            try:
                official_name = country_data.official_name if country_data.official_name != country else None
                if official_name:
                    aliases[country].append(official_name)
            except AttributeError:
                pass

        except LookupError as e:
            print('no', country)


country_data = pycountry.countries.get(name='Cabo Verde')
alpha_2, alpha_3 = country_data.alpha_2, country_data.alpha_3
name, official_name = country_data.name, country_data.official_name
aliases['Cape Verde'] = [alpha_2, alpha_3, name, official_name]

country_data = pycountry.countries.get(name='Congo, the Democratic Republic of the')
alpha_2, alpha_3 = country_data.alpha_2, country_data.alpha_3
name = country_data.name
aliases['Democratic Republic of the Congo'] = [alpha_2, alpha_3, name]

country_data = pycountry.countries.get(alpha_3='CIV')
alpha_2, alpha_3 = country_data.alpha_2, country_data.alpha_3
name, official_name = country_data.name, country_data.official_name
aliases['Ivory Coast'] = [alpha_2, alpha_3, name, official_name]

country_data = pycountry.countries.get(name='Ireland')
alpha_2, alpha_3 = country_data.alpha_2, country_data.alpha_3
name = country_data.name
aliases['Republic of Ireland'] = [alpha_2, alpha_3, name]


with open('aliases.json', 'w', encoding='utf-8') as json_file:
    json.dump(aliases, json_file, ensure_ascii=False, indent=1)

print(aliases)


