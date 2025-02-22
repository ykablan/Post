from django.shortcuts import render , redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Customer, Contact
from .form import CustomerForm, ContactForm
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date

def index(request):
    if request.user.is_staff == False:
        return redirect('/home/')
    
    customers_list = Customer.objects.all()   
    
    query = request.GET.get('q')
    if query:
        customers_list = customers_list.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(contacts__name__icontains=query) | 
            Q(contacts__email__icontains=query) |
            Q(contacts__phone__icontains=query)                                  
            ).distinct()
        
    paginator = Paginator(customers_list, 5) # Show 25 contacts per page
    page = request.GET.get('sayfa')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:        
        customers = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:        
        customers = paginator.page(paginator.num_pages)    # If page is out of range (e.g. 9999), deliver last page of results.
        
    
    context = {
        'customers': customers,
        
    }
    return render(request, 'customer/index.html', context)

def create(request):
    if request.user.is_staff == False:
        return redirect('/home/')
    
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("customer:index")
    context = {
        'form': form
    }
    return render(request, 'customer/form.html', context)

def detail(request, pk):
    if request.user.is_staff == False:
        return redirect('/home/')
    
    customer = get_object_or_404(Customer, pk=pk)

    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.customer = customer
        contact.save()
        return HttpResponseRedirect(customer.get_absolute_url())
    
    form = ContactForm()

    contacts = customer.contacts.all()


    context = {
        'customer': customer,
        'form': form,
        'contacts': contacts        
    }
    return render(request, 'customer/detail.html', context)

def update(request, pk):
    if request.user.is_staff == False:
        return redirect('/home/')
    
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
    if request.user.is_staff == False:
        return redirect('/home/')
    
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect("customer:index")


def contact_update(request, pk):
    if request.user.is_staff == False:
        return redirect('/home/')
    
    contact = get_object_or_404(Contact, pk=pk)    
    customer= get_object_or_404(Customer, id = contact.customer_id)

    if request.user.is_authenticated == False:
        return redirect('postt:index')
    form = ContactForm(request.POST or None, request.FILES or None, instance=contact)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellendi.', extra_tags='mesaj-basarili-guncelleme')  
        return HttpResponseRedirect(customer.get_absolute_url())     

    context = {
        'form': form
    }
    return render(request, 'post/form.html', context)

def contact_delete(request, pk):
    if request.user.is_staff == False:
        return redirect('/home/')
    
    contact = get_object_or_404(Contact, pk=pk)
    customer = get_object_or_404(Customer, id = contact.customer_id)
    if request.user.is_authenticated == False:
        return redirect('postt:index')

    contact.delete()
    return HttpResponseRedirect(customer.get_absolute_url())
