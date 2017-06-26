from django.views.generic import TemplateView
from common_utils.aws_utils import AWSEC2Functions
from service import DashBoardService


class Dashboard(TemplateView):

    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        personal_aws_data = AWSEC2Functions().get_required_instance_info_list()
        context = DashBoardService().get_plotting_data(personal_aws_data)
        print context
        # print personal_aws_data
        # price_info = AWSEC2Functions().get_current_instances_price(personal_aws_data)
        # formatted_data = AWSEC2Functions().prepare_data_for_plot(price_info)
        # print formatted_data
        return self.render_to_response({})
