from datetime import datetime, timedelta

instance_types  = ['c3.xlarge', 'c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge']
region = 'us-east-1'
number_of_days = 10

end = datetime.strftime(datetime.now(), "+%Y-%m-%dT%H:%M:%S")
start = datetime.strftime(datetime.now()-timedelta(days=number_of_days), "+%Y-%m-%dT%H:%M:%S")
print "will process from " + start + " to " + end

import sys
import boto as boto
import boto.ec2 as ec2
import datetime, time

ec2 = boto.ec2.connect_to_region(region)
print ec2

l = []
for instance in instance_types:
    sys.stdout.write("*** processing " + instance + " ***\n")
    sys.stdout.flush()
    prices = ec2.get_spot_price_history(start_time=start, end_time=end, instance_type=instance)
    for price in prices:
        d = {'InstanceType': price.instance_type,
             'AvailabilityZone': price.availability_zone,
             'SpotPrice': price.price,
             'Timestamp': price.timestamp}
        l.append(d)
    next = prices.next_token
    while (next != ''):
        sys.stdout.write(".")
        sys.stdout.flush()
        prices = ec2.get_spot_price_history(start_time='2017-06-16T12:25:26', end_time='2017-06-26T12:25:26', instance_type=instance, next_token=next)
        for price in prices:
            d = {'InstanceType': price.instance_type,
                 'AvailabilityZone': price.availability_zone,
                 'SpotPrice': price.price,
                 'Timestamp': price.timestamp}
            l.append(d)
        next = prices.next_token
    sys.stdout.write("\n")
