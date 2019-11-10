import csv
import requests 
import time
from utils import confirm_dir

class Predictit():
    def __init__(self):
        self.pull_data()
        self.get_ids()

    def _fetch_data(self): 
        url = 'https://www.predictit.org/api/marketdata/all/'
        self.last_pull_time = time.time()
        return requests.get(url).json()['markets']

    def pull_data(self, ignore_time=False):
        if hasattr(self, 'last_pull_time'):
            if ignore_time:
                self.data = self._fetch_data()
            else:
                current_time = time.time()
                elapsed = current_time - self.last_pull_time
                if elapsed >= 60:
                    print('%s seconds elapsed since last data pull')
                    print('Pulling fresh data..')
                    self.data = self._fetch_data()
                    print('Fresh data collected at %s' % (time.strftime("%H:%M:%S", time.localtime(current_time))))
        else:
            self.data = self._fetch_data()

    def get_ids(self):
        self.ids = []
        self.parent_ids = []
        for parent_market in self.data:
            self.parent_ids.append(parent_market['id'])
            for sub_market in parent_market['contracts']:
                self.ids.append(sub_market['id'])

    def get_data_by_id(self, market_id, greedy=False):
        # all contracts will return if market_id is a parent market id
        if market_id in self.parent_ids:
            for market in self.data:
                if market['id'] == market_id:
                    return market
        else:
            # if market_id is a contract id, only that contract data will return
            for parent_market in self.data:
                if type(parent_market['contracts']) is dict: # (then only 1 contract available)
                    if parent_market['contracts']['id'] == market_id:
                        market = parent_market['contracts']
                        return market
                    else:
                        pass
                else:
                    for sub_contract in parent_market['contracts']:
                        if sub_contract['id'] == market_id:
                            if not greedy:
                                market = parent_market
                            else:
                                market = sub_contract
                            return market

    def list_sub_markets(self):
        d = {}
        for parent_market in self.data:
            if type(parent_market['contracts']) is dict:
                d[parent_market['contracts']['id']] = parent_market['contracts']['name']
            else:
                for sub_market in parent_market['contracts']:
                    d[sub_market['id']] = sub_market['name']
        return d

    def list_parent_markets(self):
        d = {}
        for parent_market in self.data:
            d[parent_market['id']] = parent_market['name']
        return d
