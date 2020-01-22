from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db.models.functions import Lower

from django.views import generic
from .models import Client

from .forms import ClientForm
# Insert views here


def listClient(request):

    client_list = Client.objects.all().order_by('-id')

    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    suburb = request.GET.get('suburb')
    order = request.GET.get('order')
    sort = request.GET.get('sort')

    # a search by client name, email address, phone number, client suburb
    if name != '' and name is not None:
        client_list = client_list.filter(name__icontains=name)

    if email != '' and email is not None:
        client_list = client_list.filter(email__icontains=email)

    if phone != '' and phone is not None:
        client_list = client_list.filter(phone__icontains=phone)

    if suburb != '' and suburb is not None:
        client_list = client_list.filter(suburb__icontains=suburb)

    # the ability to order by name, email address, phone number and suburb
    if order != '' and order is not None:
        if sort == 'desc':
            client_list = client_list.order_by(Lower(order)).reverse()
        else:
            client_list = client_list.order_by(Lower(order))

    context = {
        'client_list': client_list,
        'order': order,
        'sort': sort
    }

    return render(request, 'python_test/client_list.html', context)


def newClient(request):

    # create a new Client.
    form = ClientForm()

    context = {
        'form': form
    }

    # POST Submission
    if request.method == "POST":

        submitted_form = ClientForm(request.POST)

        # if is_valid save and return to client list
        if submitted_form.is_valid():
            submitted_form.save()
            return HttpResponseRedirect(reverse('client_list'))
        else:
            # Adding is-invalid class for bootsrap 4
            for field in submitted_form.errors:
                submitted_form[field].field.widget.attrs['class'] += ' is-invalid'

            context = {
                'form': submitted_form
            }

    return render(request, 'python_test/client_form.html', context)


def editClient(request, id=0):

    # update a given Client record.
    try:
        client_record = Client.objects.get(pk=id)
    except:
        return HttpResponseRedirect(reverse('client_list'))

    form = ClientForm(instance=client_record)

    context = {
        'form': form
    }

    # POST Submission
    if request.method == "POST":

        submitted_form = ClientForm(request.POST, instance=client_record)

        # if is_valid save and return to client list
        if submitted_form.is_valid():
            submitted_form.save()
            return HttpResponseRedirect(reverse('client_list'))
        else:
            # Adding is-invalid class for bootsrap 4
            for field in submitted_form.errors:
                submitted_form[field].field.widget.attrs['class'] += ' is-invalid'

            context = {
                'form': submitted_form
            }

    return render(request, 'python_test/client_form.html', context)


def deleteClient(request, id):
    try:
        client = Client.objects.get(pk=id)
    except:
        return HttpResponseRedirect(reverse('client_list'))

    if client:
        client.delete()

    return HttpResponseRedirect(reverse('client_list'))
