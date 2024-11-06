from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Item, Catergory
from .forms import NewItemForm


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'detail.html', context)


@login_required('login/')
def new_item(request):
    form = NewItemForm()
    context = {
        'form': form,
        'title': 'New Item',
    }
    return render(request, 'form.html', context)
