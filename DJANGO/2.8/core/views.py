from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class Myviews(TemplateView):
    template_name = 'line_chart.html'

#+------------------------------+#
#| OPEN chartjs                 |#
#+------------------------------+#

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for i in the x-axis."""
        return ["January", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

#+------------------------------+#
#| END chartjs                  |#
#+------------------------------+#


# forma de fazer na doc do django-chart
#line_chart = TemplateView.as_view(template_name='line_chart.html')
#line_chart_json = LineChartJSONView.as_view()

