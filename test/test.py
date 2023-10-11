from EScrape import EScrape

if __name__ == '__main__':
    url = "https://pogoapi.net//api/v1/shiny_pokemon.json"
    scraper = EScrape(url)

    try:
        # Fetch JSON
        json_data = scraper.fetch_json()

        # Save JSON data to a file
        scraper.save_json_to_file("PoGo_Shiny.json", json_data)

        # Continue with other operations if needed
    except ValueError as e:
        print(e)
