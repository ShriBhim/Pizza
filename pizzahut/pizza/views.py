from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

# Create your views here
def homepage(request):
    return render(request,'pizza/home.html')

def order(request):
    created_pizza_pk = None
    multiple_pizza_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks your order %s, %s ,%s pizza was placed successfully'%(filled_form.cleaned_data['topping1'],
                                                                                     filled_form.cleaned_data['topping2'],
                                                                                     filled_form.cleaned_data['size'])
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id

        else:
            note = 'please tryagain..'
        new_form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': new_form,
                                                                         'note':note,
                                                                         'multiple_pizza_form':multiple_pizza_form,
                                                                          'created_pizza_pk':created_pizza_pk})

    else:
        form = PizzaForm()
        return render(request,'pizza/order.html',{'pizzaform':form,
                                                                       'multiple_pizza_form':multiple_pizza_form})
def pizzas(request):
    no_of_pizzas = 2
    if request.method == 'GET':
        filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
        if filled_multiple_pizza_form.is_valid():
            no_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
        print(no_of_pizzas)
    PizzaFormset = formset_factory(PizzaForm,extra=no_of_pizzas)
    formset = PizzaFormset() #empty formset
    if request.method == 'POST':
        filled_formset = PizzaFormset(request.POST)
        if filled_formset.is_valid():
            note = 'Thanks you order is placed'
            for forms in filled_formset:
                forms.save()
        else:
            note = 'sorry,order is not placed !... pls retry'


        return render(request,'pizza/pizzas.html',{'note':note})

    return render(request,'pizza/pizzas.html',{'formset':formset})

def edit(request,pk):
    note = ''
    print(pk) #pk--> model class --> model obj --> formclass -->form obj -- front end
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        edited_form = PizzaForm(request.Post,instance=pizza)
        if edited_form.is_valid():
            note = 'order successfully'
            edited_form.save()
        else:
            note = 'please try again'
    return render(request,'pizza/edit.html',{'pizzaform':form,'pk':pk,'note':note})