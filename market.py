import re
from predictit import Predictit

class Market(Predictit):

    def _get_markets_to_check(self, search_parent=True, search_contracts=True):
        markets_to_check = {}
        if search_parent:
            parent_markets = self.list_parent_markets()
            markets_to_check.update(parent_markets)
        if search_contracts:
            contract_markets = self.list_sub_markets()
            markets_to_check.update(contract_markets)
        return markets_to_check

    def _get_market_by_function(self, fx, search_parent, search_contracts, **kwargs):
        # applies market functions for market selection
        self.pull_data() # pulls fresh data if elapsed time > 60s
        markets_to_check = self._get_markets_to_check(search_parent, search_contracts)

        ids_to_return = []
        for i, name in markets_to_check.items():
            if fx(i, name, **kwargs):
                ids_to_return.append(i)
        
        if len(ids_to_return) == 0:
            return
        else:
            markets = []
            for i in ids_to_return:
                markets.append(self.get_data_by_id(i))
        return markets

    def _regex_function(self, i, name, regex):
        if re.match(regex, name, re.IGNORECASE) is not None:
            return True
        else:
            return False

    def get_market_by_regex(self, regex, search_parent=True, search_contracts=True):
        markets = self._get_market_by_function(
            self._regex_function, 
            regex=regex, 
            search_parent=search_parent, 
            search_contracts=search_contracts
            )
        return markets

    def _contains_function(self, i, name, x, ignore_case):
        if ignore_case:
            name = name.lower()
            x = x.lower()
        if name.find(x) != -1:
            return True
        else:
            return False

    def get_market_that_contains(self, x, search_parent=True, search_contracts=True, ignore_case=True):
        markets = self._get_market_by_function(
            self._contains_function, 
            search_parent=search_parent, 
            search_contracts=search_contracts,
            x=x,
            ignore_case=ignore_case
            )
        return markets
