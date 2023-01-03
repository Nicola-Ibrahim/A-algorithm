from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from . import searching

@require_http_methods(['GET', 'POST'])
def display_game(request):
    context = {}
    # if (request.method == 'POST'):
    #     print(request.POST)

    if (request.method == 'GET'):
        
        # start state 
        start = [8, 2, 3, 6, 1, 4, 7, 0, 5]
        
        # target state       
        target = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        
        

        best_path = searching.a_start(start, target)
        context = {
            "content": best_path
        }

    return render(request=request, template_name='display.html', context=context)
