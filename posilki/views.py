# Create your views here.
from posilki.forms import ProduktForm,PosilekForm,PositionForm
from posilki.models import Produkt
from uzytkownicy.models import Uzytkownik
from django.shortcuts import render_to_response, redirect
from django.http import *
from django.forms.formsets import formset_factory, BaseFormSet
from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF

def add_product(request):
    if request.method == 'POST':
        p = ProduktForm(request.POST)
        new_product = p.save(commit=False)
        new_product.save()
        message='Dodano produkt ' + (new_product.nazwa)
        return render_to_response("uzytkownicy/user.html", {
                                                                'message':
                                                               message,
                                                                })
    else:
        add_product_form = ProduktForm()
        return render_to_response("posilki/add_product.html", {
                                                                'add_product_form':
                                                                add_product_form,
                                                                })
            
def add_meal(request):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False
                
    TodoItemFormSet = formset_factory(PositionForm, max_num=10, formset=RequiredFormSet)

    if request.method == 'POST': # If the form has been submitted...
        todo_list_form = PosilekForm(request.POST) # A form bound to the POST data
        # Create a formset from the submitted data
        todo_item_formset = TodoItemFormSet(request.POST, request.FILES)
        
        if todo_list_form.is_valid() and todo_item_formset.is_valid():
            todo_list = todo_list_form.save(commit=False)
            todo_list.uzytkownik = Uzytkownik.objects.get(user=request.user)
            todo_list.save()
            for form in todo_item_formset.forms:
                todo_item = form.save(commit=False)
                todo_item.posilek = todo_list                
                todo_item.save()

            return HttpResponseRedirect('thanks') # Redirect to a 'success' page
    else:
        todo_list_form = PosilekForm()
        todo_item_formset = TodoItemFormSet()
    
    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/ 
    c = {'todo_list_form': todo_list_form,
         'todo_item_formset': todo_item_formset,
        }
    c.update(csrf(request))
    
    return render_to_response('posilki/add_meal.html', c)