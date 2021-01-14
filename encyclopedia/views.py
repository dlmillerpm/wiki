from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search1(request, name):
    return render(request, "encyclopedia/entry.html", {
        "entries": util.get_entry(name)
    })

def entry(request, name):
    return render(request, "encyclopedia/entry.html", {
        "entries": util.get_entry(name)
    })

