from django.urls import path, include

from eve.watchlist import views

app_name = 'watchlist'
urlpatterns = [
    path('', views.WatchlistView.as_view(), name='watchlist'),
    path('watchlist_items_save/', views.add_items, name='watchlist-items-save'),
    path('add_table/', views.AddTableView.as_view(), name='add-table'),
    path('<int:pk>/', include([
        path('edit_table/', views.EditTableView.as_view(), name='edit-table'),
        path('delete_table/', views.DeleteTableView.as_view(), name='delete-table'),
    ])),

]