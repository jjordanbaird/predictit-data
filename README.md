# Predictit-Data

This package is a simple api wrapper for the predictit.org endpoint: _https://www.predictit.org/api/marketdata/all_
It facilititates extraction of instantaneous political market data.

# Installation
_Before installation, it is recommended that you ensure you have a virtual environment activated._
- Clone this repository and cd into it
- run `python setup.py` 

# Usage
To use this module, import the Market class.

You can use:<br/>
`import predictit_data`<br/>
`m = predictit_data.Market()`<br/>
or<br/>
`from predictit_data.market import Market`
`m = Market()`

`m.data`: Return all market data <br/>
`m.pull_data`: Pulls latest data _(generally unneccessary as other methods check for latest data)_<br/>
`m.get_markets_by_regex`: Returns all markets whose `name` matches a regex pattern<br/>
`m.get_markets_that_contain`: Returns all markets that contain a given string<br/>
`m.get_data_by_id`: Returns market data for a given id<br/>
`m.list_parent_markets`: Returns `{id: name}` for every available parent market<br/>
`m.list_sub_markets`: Returns `{id: name}` for every available sub market<br/>

# Market data structure
Market data is structured as a dictionary. [See Example.](https://github.com/jjordanbaird/predictit-data/blob/master/examples/example_market_structure.json)

Notice that there can be a number of "sub markets" in a given "parent market". <br/>
In this example there are 4 sub markets, each with a unique `id` for a given parent market, that has its own unique `id`.<br/>
Each sub market has pricing data associated with it; note that no parent market will have pricing data associated with it.

# Notes
This wrapper enforces an ask I received from support@predictit.org that the api be called no more than once every 60 seconds. (Note that Predictit only updates the api endpoint once every 60 seconds, so calling it more often than that would be wasteful anyway.)
