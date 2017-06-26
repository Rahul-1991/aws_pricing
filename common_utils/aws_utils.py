import boto3
from aws_config import Config
from helpers import get_from_dict
from datetime import datetime
from dateutil.tz import tzlocal
import pprint


class AWSEC2Functions(object):

    def __init__(self):
        self.ec2_conn = boto3.client('ec2', region_name='us-east-1')
        self.instances_info = self.get_instance_info()

    def get_instance_info(self):
        reservations = self.ec2_conn.describe_instances().get('Reservations', [])
        if reservations:
            return reservations[0].get('Instances', [])
        return list()

    def get_required_instance_info_list(self):
        required_fields = Config.REQUIRED_FIELDS
        instance_info_list = list()
        for reservation in self.instances_info:
            required_info = dict()
            for field in required_fields:
                if isinstance(field, str):
                    required_info.update({field: reservation.get(field)})
                else:
                    required_info.update({field[-1]: get_from_dict(reservation, field)})
            instance_info_list.append(required_info)
        return instance_info_list

    @staticmethod
    def prepare_data_for_plot(spot_price_history):
        formatted_dict = dict()
        for history in spot_price_history:
            time = datetime.strftime(history.get('Timestamp'), "%Y-%m-%d")
            instance_type = history.get('InstanceType')
            current_spot_price = history.get('SpotPrice')
            if time in formatted_dict.keys():
                time_info = formatted_dict.get(time)
                if instance_type in time_info.keys():
                    prev_spot_price = time_info.get(instance_type)
                    if prev_spot_price < current_spot_price:
                        time_info[instance_type] = current_spot_price
                        formatted_dict[time]= time_info
                else:
                    time_info.update({history.get('InstanceType'): history.get('SpotPrice')})
                    formatted_dict[time] = time_info
            else:
                print time
                formatted_dict[time] = {history.get('InstanceType'): history.get('SpotPrice')}
        return formatted_dict

    def get_current_instances_price(self):
        response = self.ec2_conn.describe_spot_price_history(
            EndTime=datetime(2017, 6, 23),
            StartTime=datetime(2017, 5, 1),
            InstanceTypes=['m3.medium', 'm1.large', 'm2.2xlarge'],
            AvailabilityZone='us-east-1c',
            ProductDescriptions=['Linux/UNIX']
        )
        return response

