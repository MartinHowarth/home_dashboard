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
    'clock': {},
    'train': {
        # Register for an api key here: http://realtime.nationalrail.co.uk/OpenLDBWSRegistration/
        'nre_api_key': 'YOUR-KEY',
        'train_station_code': 'MAN',
        'max_listings': 4,
    },
    'weather': {
        # Register for an API key here: https://home.openweathermap.org/users/sign_up
        'open_weather_map_api_key': 'YOUR-KEY',
        'location': 'Enfield,uk',
    },
    'wifi': {
        'auth_type': 'WPA',
        'password': 'password',
        'ssid': 'wifi_name'
    }
}


if __name__ == "__main__":
    import json
    print(json.dumps(config))
