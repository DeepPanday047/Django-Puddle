from django.shortcuts import render
from items.models import Item
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request,'index.html',
                  {'items':items,})