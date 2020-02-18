from django.shortcuts import redirect

def redirect_airlines(request):
    return redirect('airlines_list_url', permanent=True)
