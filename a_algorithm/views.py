from django.shortcuts import render

# Create your views here.


def index(request):

    context = {

        "content": {
            "array_1": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ],
            "array_2": [
                [1, 3, 4],
                [6, 0, 2],
                [7, 8, 5]
            ],

        }
    }

    return render(request=request, template_name='display.html', context=context)
