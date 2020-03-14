from django.shortcuts import render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def home(request):
    return render(request, 'makesite/makesite.html')
