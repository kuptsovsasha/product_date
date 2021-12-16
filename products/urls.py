from django.urls import path

from products.views import item_list, StartList, patch_new_date, search_products, add_products

urlpatterns = [
    path('list/', item_list, name='item-list'),
    path('', StartList.as_view(), name='start_list'),
    path('update/', patch_new_date, name='update_date'),
    path('search/', search_products, name='search'),
    path('add_new/', add_products, name='add_new'),

]