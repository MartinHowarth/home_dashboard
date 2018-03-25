# Home Dashboard
An auto-updating dashboard that displays the following widgets:

- Time & date
- Live bus stop updates (TFL only)
- Live train station updates (National Rail only)
- Upcoming birthdays

Only one bus/train stop is supported.

## Installation

```python
python setup.py install
python home_dashboard/main.py [config_file]
```

## Config file
There are two ways of getting config:
1) From the "ALL_CONFIG" environment variable - this must be a JSON dict of the config.
2) If ALL_CONFIG is not set, then a filename can be passed in with a python dict of the config

In both cases, see `example_config.py`.

To convert the config dictionary to JSON for use in the environment variable, do the following:

```python
import json

config_dict = {...}

print(json.dumps(config_dict))
```
