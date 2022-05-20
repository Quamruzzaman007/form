from django.shortcuts import redirect, render, HttpResponse
from submit_form.models import FormData
from django.contrib import messages

def form(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
            
        if FormData.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect("form")

        elif email.count('@')==1 and email.endswith("@gmail.com"):
            form = FormData(email=email, name=name)
            form.save()
            messages.success(request, 'Form Submitted successfully')

        else:
            messages.warning(request, "Email is not valid")
    return render(request, 'form.html')