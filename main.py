# main.py
import json
import time

# Dummy data instead of API
DUMMY_COUNTRIES = ["us", "fr", "be"]

DUMMY_LEADERS = {
    "us": [
        {
            "name": "George Washington",
            "start_date": "1789",
            "end_date": "1797",
            "wikipedia_url": "https://en.wikipedia.org/wiki/George_Washington",
        },
        {
            "name": "Abraham Lincoln",
            "start_date": "1861",
            "end_date": "1865",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Abraham_Lincoln",
        },
    ],
    "fr": [
        {
            "name": "Napoleon Bonaparte",
            "start_date": "1804",
            "end_date": "1815",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Napoleon",
        }
    ],
    "be": [
        {
            "name": "Leopold II of Belgium",
            "start_date": "1865",
            "end_date": "1909",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Leopold_II_of_Belgium",
        }
    ],
}

def get_countries():
    """Return dummy list of countries"""
    return DUMMY_COUNTRIES

def get_leaders(country):
    """Return dummy leaders for a country"""
    return DUMMY_LEADERS.get(country, [])

def get_first_paragraph(wikipedia_url):
    """Return a fake paragraph (simulate scraping)"""
    return f"This is a simulated first paragraph for {wikipedia_url}"

def main():
    countries = get_countries()
    all_data = {}

    for country in countries:
        print(f"Fetching leaders for {country}...")
        leaders = get_leaders(country)
        country_data = []

        for leader in leaders:
            print(f"  Fetching info for {leader['name']}...")
            wiki_para = get_first_paragraph(leader['wikipedia_url'])
            leader_info = {
                "name": leader['name'],
                "start_date": leader['start_date'],
                "end_date": leader['end_date'],
                "wikipedia_first_paragraph": wiki_para,
            }
            country_data.append(leader_info)
            time.sleep(0.5)  # just for effect

        all_data[country] = country_data

    # Save to JSON
    with open("leaders_data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    print("Done! 'leaders_data.json' has been created with dummy data.")

if __name__ == "__main__":
    main()
