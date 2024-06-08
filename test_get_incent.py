import bittensor as bt
import requests
import time
from io import StringIO
from prettytable import PrettyTable
import pandas as pd

burn_map = {}
my_netuids = [3, 5, 7, 11, 20, 24, 26, 27, 28, 29, 30, 31, 32]
cold_keys = [
    '5DwAELY8mf1Sb6ZFqcumDCvxKcLakqHrVf2tPaGzQVxA1jzS',
    '5Hj9CS67VpVLL4prMRGGXSBB4uY8ZBHPriMyPveUoxdSX9ZR',
]
tele_chat_id = "-4206695854"
tele_report_token = "6882833557:AAHT0H0WeS6Z-VR0vF2PSwwYoWrXgjqfd7Q"
reward_map = {}

hotkeys = {
            # "5FWr1PnUHszMLcYBxMFaV73ZFyBy4vZqnUgRNakuEBaEWS39",
            # "5EuzFvNmxt8Z7XCVbmKWzbUYKJkgZawVTVeyacj6tZQf3y1H",
            # "5FCZ4FbxNwzHfmvjVwqunfJ5wKGw6Ds3r7dPJoyXJVsf5Snm"
        }

def get_subnet_reward(netuid, cold_keys, rewards):
    x = PrettyTable()
    x.field_names = ["HOT", "INCENTIVE", "REWARDS", "RANK"]
    url = 'https://taostats.io/wp-admin/admin-ajax.php'
    data = {
        'action': 'metagraph_table',
        'this_netuid': netuid
    }

    response = requests.post(url, data=data)
    print(response)

if __name__ == "__main__":
    rewards = []
    cold_keys=["5DwAELY8mf1Sb6ZFqcumDCvxKcLakqHrVf2tPaGzQVxA1jzS"]
    get_subnet_reward(31,cold_key,rewards)