from django.shortcuts import render
from .models import Strategy

def strategy_list(request):
    strategies = Strategy.objects.all()  # Получаем все стратегии из базы данных
    return render(request, 'strategies/strategy_list.html', {'strategies': strategies})
