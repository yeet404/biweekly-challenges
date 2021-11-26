# considering that I'm using the same form for both madlibs this is so inefficient

from django.shortcuts import render
from django import forms

class MadLib(forms.Form):
    adj1 = forms.CharField(label="Adjective")
    v1 = forms.CharField(label="Verb (past tense)")
    adj2 = forms.CharField(label="Adjective")
    adj3 = forms.CharField(label="Adjective")
    v2 = forms.CharField(label="Verb (past tense)")

# Create your views here.
def index(request):
    return render(request, "wk3/index.html")

def sussy(request):
    if request.method == "POST":
        form = MadLib(request.POST)
        if form.is_valid():
            results = list(form.clean().values())
            return render(request, "wk3/sussy.html", {
                    "form": form,
                    "result": f"The very {results[0]} impostor vented to medbay. The impostor {results[1]} cyan. Red saw the very {results[2]} do it so red was {results[1]} as well. Thankfully, the {results[3]} player spotted the impostor's shenanigans and the very {results[0]} impostor was {results[4]}."
                })
        else:
            return render(request, "wk3/sussy.html", {
                "form": form
            })
    return render(request, "wk3/sussy.html", {
        "form": MadLib()
    })
def bob(request):
    if request.method == "POST":
        form = MadLib(request.POST)
        if form.is_valid():
            results = list(form.clean().values())
            return render(request, "wk3/bob.html", {
                    "form": form,
                    "result": f"Bob the {results[0]} builder {results[1]} to the farmer's market. He bought some {results[2]} vegetables and {results[3]} fruits. Then he {results[4]} home."
                })
        else:
            return render(request, "wk3/bob.html", {
                "form": form
            })
    return render(request, "wk3/bob.html", {
        "form": MadLib()
    })
