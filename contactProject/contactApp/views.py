from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactModel
from .forms import ContactForm
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    print("end index")
    allcontacts = ContactModel.objects.all()
    return render(request, 'contactApp/index.html', {'contact_form': allcontacts})

# saves input from form/POST
def contacts(request):
    newForm = ContactForm(request.POST or None)
    if newForm.is_valid():
        newForm.save()
        return redirect('index')
    return render(request, 'contactApp/index.html', {'contactForm': newForm})
# enables to edite the contact info and save it to the database

def editcontacts(request, id):
    contact = get_object_or_404(ContactModel, pk=id)
    edit_form = ContactForm(request.POST or None, instance=contact)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    return render(request, 'contactApp/contacts.html', {'contactForm': edit_form})

# deltes the contact/post
def deletecontact(request, id):
    contact = get_object_or_404(ContactModel, pk=id)
    delete_form = ContactForm(request.POST)
    if delete_form.is_valid():
        delete_form.save()
        return redirect('index')
    return render(request, 'contactApp/delete.html', {'selectedcontact': contact})
