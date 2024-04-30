from django.shortcuts import redirect, render
from .forms import ExpenseForm  # Corrected import statement
from .models import Expense
import datetime
from django.db.models import Sum


def index(request):
    if request.method == "POST":
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
    
    
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(total_amount=Sum('amount'))
    
    #logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(total_amount=Sum('amount'))

    #logic to calculate 30 days expenses
    last_months = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_months)
    monthly_sum = data.aggregate(total_amount=Sum('amount'))

    #logic to calculate 7 days expenses
    week_months = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=week_months)
    week_sum = data.aggregate(total_amount=Sum('amount'))

    #logic to calculate daily expenses
    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))

    print(daily_sums)

    category_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))

    expense_form = ExpenseForm()  


    context = {
        'expense_form': expense_form,
        'expenses':expenses,
        'total_expenses':total_expenses,
        'yearly_sum':yearly_sum,
        'week_sum':week_sum,
        'monthly_sum':monthly_sum,
        'daily_sums':daily_sums ,
        'category_sums':category_sums,
        }

    return render(request, 'myapp/index.html', context)  # Corrected variable name in context dictionary


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