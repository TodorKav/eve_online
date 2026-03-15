from django.db.models import Q, ExpressionWrapper, FloatField, Value, F
from django.db.models.functions import Coalesce, NullIf
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from eve.industry.forms import SearchForm
from eve.industry.models import CorporationsLpItemTypes


# Create your views here.


class ItemList(ListView, BaseFormView):
    template_name = 'industry/items_list.html'
    model = CorporationsLpItemTypes
    form_class = SearchForm
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(type_id__name__icontains=q) | Q(corporation_id__name=q))


        return queryset.select_related('type_id', 'type_id__market_prices', 'corporation_id',).annotate(
            price_pro_lp=ExpressionWrapper(
                (
                    Coalesce(F('type_id__market_prices__adjusted_price'), Value(0.0)) * F('quantity')
                    - Coalesce(F('isk_cost'), Value(0.0))
                    - Coalesce(F('material_cost'), Value(0.0))
                ) / NullIf(Coalesce(F('lp_cost'), Value(1.0)), Value(0.0)),
                output_field=FloatField()
            )
        ).order_by(F('price_pro_lp').desc(nulls_last=True))

    def get_initial(self):
        initial = super().get_initial()
        initial['q'] = self.request.GET.get('q')
        return initial
