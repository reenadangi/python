from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def rand_word(request):
    if 'count' not in request.session:
        request.session["count"] = 0
    else:
        request.session["word"] = get_random_string(length=14)
        request.session["count"] += 1
    return render(request, "index.html")

def reset(request):
    print('reset')
    request.session.flush()
    return redirect('/')

def test(request):
    return render(request, "index.html")