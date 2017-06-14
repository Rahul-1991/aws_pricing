import requests
import json


class BaseCoordinator(object):

    def __init__(self, base_url):
        self.base_url = base_url

    def path_with_slash(self, path):
        return path if path.startswith('/') else '/' + path

    def action(self, path):
        return self.base_url + self.path_with_slash(path)

    def post(self, path, payload=None, headers=None, params=None, data=None, timeout=90, handle_error=True):
        response = requests.post(
            self.action(path), params=params, json=payload, headers=headers, data=data, timeout=timeout)
        return response

    def get(self, path, payload=None, headers=None, timeout=90):
        response = requests.get(
            self.action(path), params=payload, headers=headers, timeout=timeout)
        return response


class PopulateSpotData(BaseCoordinator):

    def __init__(self):
        SPOT_URI = 'http://127.0.0.1:8000'
        super(PopulateSpotData, self).__init__(SPOT_URI)
        self.spot_data = self.get_spot_info()

    @staticmethod
    def get_spot_info():
        url = 'http://spot-price.s3.amazonaws.com/spot.js'
        response = requests.get(url)
        return json.loads(response.text.strip('callback();')).get('config')

    def insert_region_name(self, region):
        url = 'spotdata/createRegion/'
        payload = {'region_name': region.get('region', '')}
        response = self.post(url, data=payload)
        return response.json().get('id')

    def insert_instance_in_region(self, region_id, instance):
        url = 'spotdata/createInstance/'
        payload = {'instance_type': instance.get('type', ''),
                   'region_id': region_id}
        response = self.post(url, data=payload)
        return response.json().get('id')

    def insert_instance_sizeprice(self, instance_id, sizes):
        url = 'spotdata/createSizePrice/'
        payload = {'instance_id': instance_id,
                   'size': sizes.get('size'),
                   'price': sizes.get('valueColumns')[0].get('prices').get('USD')}
        response = self.post(url, data=payload)
        return response.json().get('id')

    def populate_spot_table(self):
        for region in self.spot_data.get('regions'):
            region_id = self.insert_region_name(region)
            for instance in region.get('instanceTypes'):
                instance_id = self.insert_instance_in_region(region_id, instance)
                for sizes in instance.get('sizes'):
                    self.insert_instance_sizeprice(instance_id, sizes)


obj = PopulateSpotData()
obj.populate_spot_table()
