from django.shortcuts import redirect, render
from .forms import ExpenseForm  # Corrected import statement
from .models import Expense
from django.db.models import Sum

def index(request):
    if request.method == "POST":
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
    
    
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(total_amount=Sum('amount'))
    expense_form = ExpenseForm()  # Changed variable name to match typo corrected import statement
    return render(request, 'myapp/index.html', {'expense_form': expense_form,'expenses':expenses,'total_expenses':total_expenses})  # Corrected variable name in context dictionary


def edit(request,id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    return render(request,'myapp/edit.html',{'expense_form': expense_form})


def delete(request,id):
    if request.method == "POST" and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('myapp:index')