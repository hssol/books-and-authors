from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# def index(request):
#     if "counter" in request.session:
#         request.session["counter"] += 1
#     else:
#         request.session['counter'] = 0
#     unique_id = get_random_string(length=14)
#     request.session['word'] = unique_id
    
#     return render(request, "randomWord/index.html")
def index(request):
    context = {
        "authors": Author.objects.all()
        }
    return render(request, "randomWord/index.html", context)

def destroy(request):
    request.session.flush()
    return redirect('/')
    
        
        
        # print("a POST request is being made to this route")
        # return render(request, "randomWord/index.html")