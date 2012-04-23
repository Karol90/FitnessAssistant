# Create your views here.
from posilki.forms import ProduktForm,PosilekForm,PositionForm
from posilki.models import Produkt
from django.shortcuts import render_to_response, redirect

def add_product(request):
    if request.method == 'POST':
        a=1
    else:
        add_product_form = ProduktForm()
        return render_to_response("posilki/add_product.html", {
                                                                'add_product_form':
                                                                add_product_form,
                                                                })
        

        
def add_meal(request):
    if request.method == 'POST':
        a=1
    else:
        add_meal_form = PosilekForm()
        add_position_form = PositionForm()
        return render_to_response("posilki/add_meal.html", {
                                                                'add_meal_form':
                                                                add_meal_form,
                                                                'add_position_form':
                                                                add_position_form,
                                                                })