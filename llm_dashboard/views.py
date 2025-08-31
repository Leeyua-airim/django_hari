from django.shortcuts import render
from django.http import HttpResponse
from .models import Evaluation_results

def llm_dashboard(request):
    evaluate_info = Evaluation_results.objects.all()

    context = {
        'evaluate_info_key' : evaluate_info
    }
    
    return render(
        request=request,
        template_name='llm_dashboard/dashboard.html',
        context=context
    )