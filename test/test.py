from EScrape import EScrape

if __name__ == '__main__':
    url = "https://pogoapi.net//api/v1/shiny_pokemon.json"
    scraper = EScrape(url)

    try:
        # Fetch JSON
        json_data = scraper.fetch_json()
        print(json_data)

    except ValueError as e:
        print(e)
