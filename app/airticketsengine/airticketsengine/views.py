from django.shortcuts import redirect

def redirect_main_page(request):
    return redirect('main_page_url', permanent=True)
