from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import foodItem
from.forms import itemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
# def index(request):
#     data=foodItem.objects.all()
#     return render(request,'index.html',{'data':data})
#index class view 
class IndexClassView(ListView):
    model=foodItem
    template_name='index.html'
    context_object_name='data'
    

# def detail(request,item_id):
#     data=foodItem.objects.get(id=item_id)
#     return render(request,'details.html',{'data':data})

#view for food deatails
class FoodDetail(DetailView):
    model=foodItem
    template_name="details.html"
    


#this is afunction base view for creating item
# def create_item(request):
#     form=itemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request,'item_form.html',{'form':form})


#this is a class base view for creating item
class createItem(CreateView):
    model=foodItem
    fields=['item_name','item_desc','item_price','item_image']
    template_name='item_form.html'
    def form_valid(self, form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)


def update_item(request,id):
    data=foodItem.objects.get(id=id)
    form=itemForm(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'item_form.html',{'form':form})

def delete_item(request,id):
    data=foodItem.objects.get(id=id)
    if request.method =='POST':
        data.delete()
        return redirect('index')
    return render(request,'item_delete.html',{'data':data})
