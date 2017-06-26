from functools import reduce
import operator
import requests
from aws_config import Config
import json


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)


def current_spot_price(instance_name_list):
    url = Config.SPOT_PRICE_URL
    instance_price_info = dict()
    response = requests.get(url)
    if not response.status_code == 200:
        return None
    formatted_response = json.loads(response.text.strip('callback();'))
    regions_info_list = formatted_response.get('config', {}).get('regions', [])
    for region_info in regions_info_list:
        instance_types = region_info.get('instanceTypes')
        for instance in instance_types:
            sizes = instance.get('sizes')
            for size_info in sizes:
                if size_info.get('size') in instance_name_list:
                    instance_price_info.update(
                                            {size_info.get('size'):
                                                size_info.get('valueColumns', [])[0].get('price', {}).get('USD', 0)})
    return instance_price_info

