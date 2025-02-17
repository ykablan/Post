from django.shortcuts import render , redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Customer
from .form import CustomerForm
from django.db.models import Q

def index(request):
    customers = Customer.objects.all()

    query = request.GET.get('q')
    if query:
        customers = customers.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query)             
            ).distinct()
        

    context = {
        'customers': customers,
    }
    return render(request, 'customer/index.html', context)

def create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("customer:index")
    context = {
        'form': form
    }
    return render(request, 'customer/form.html', context)

def detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
        'customer': customer,
    }
    return render(request, 'customer/detail.html', context)

def update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(customer.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'customer/form.html', context)

def delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect("customer:index")
