from django.urls import path
from.import views

urlpatterns = [
    #fooditem
    path('', views.IndexClassView.as_view(),name='index'),
    #fooditem/id
    path('/<int:pk>',views.FoodDetail.as_view(),name='detail'),
    #addiem
    path('add',views.createItem.as_view(),name='create_item'),
    #uppdate item
    path('update/<int:id>',views.update_item,name="update"),
    #delete item
    path('delete/<int:id>',views.delete_item,name='delete')
]
