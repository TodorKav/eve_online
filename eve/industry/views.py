from django.views.generic import ListView

from eve.industry.mixins import RequiredItemsMixin
from eve.industry.models import CorporationsLpItemTypes


# Create your views here.


class Test(ListView):
    template_name = 'test.html'
    model = CorporationsLpItemTypes
    paginate_by = 100

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('type_id', 'corporation_id')
        queryset = RequiredItemsMixin.display(queryset)
        return queryset

