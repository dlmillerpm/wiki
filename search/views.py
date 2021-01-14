from django.shortcuts import render

from . import util


def index(request):
    return render(request, "search/index.html", {
        "entries": util.list_entries()
    })

def search(request, name):
    return render(request, "search/entry.html", {
        "entries": util.get_entry(name)
    })

