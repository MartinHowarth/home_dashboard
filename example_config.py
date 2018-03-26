config = {
    'birthday': {
        'birthdays': [
            {
                'name': 'Jane Bloggs',
                'date': '1984-05-07',
            },
            {
                'name': 'Joe Bloggs',
                'date': '1982-04-21',
            },
        ],
        'max_listings': 4,
    },
    'bus': {
        'bus_stop_code': '91532',
        'max_listings': 4,
        'walk_minutes_to_stop': 5,
        'run_minutes_to_stop': 2,
    },
    'train': {
        # Register for an api key here: http://realtime.nationalrail.co.uk/OpenLDBWSRegistration/
        'nre_api_key': 'YOUR-KEY',
        'train_station_code': 'MAN',
        'max_listings': 4,
    },
    'weather': {
        'open_weather_map_api_key': '47e4af10b0f2e0e180830016297b2162',
        'location': 'Enfield,uk',
    },
}


if __name__ == "__main__":
    import json
    print(json.dumps(config))
