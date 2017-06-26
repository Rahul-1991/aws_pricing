class Config:

    SPOT_PRICE_URL = 'http://spot-price.s3.amazonaws.com/spot.js'

    REQUIRED_FIELDS = ['InstanceLifecycle', 'InstanceType', 'KeyName', ['Placement', 'AvailabilityZone']]
