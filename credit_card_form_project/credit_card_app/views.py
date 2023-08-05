from django.shortcuts import render, redirect
from .forms import CreditCardForm

def credit_card_form(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CreditCardForm()
    return render(request, 'credit_card_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
