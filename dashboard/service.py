from common_utils.aws_utils import AWSEC2Functions


class DashBoardService(object):

    def __init__(self):
        self.aws_utils = AWSEC2Functions()

    def fetch_spot_price_data(self, personal_aws_data):
        price_info_list = list()
        count = 1
        spot_price_info = self.aws_utils.get_current_instances_price()
        while spot_price_info.get('NextToken') and count < 50:
            price_info_list.extend(spot_price_info.get('SpotPriceHistory'))
            print 'fetching from next token ', count
            count = count + 1
            spot_price_info = self.aws_utils.get_current_instances_price()
        price_info_list.extend(spot_price_info.get('SpotPriceHistory'))
        return price_info_list

    def get_plotting_data(self, personal_aws_data):
        spot_price_data = self.fetch_spot_price_data(personal_aws_data)
        return self.aws_utils.prepare_data_for_plot(spot_price_data)
