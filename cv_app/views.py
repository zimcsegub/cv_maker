from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CV
from .forms import CVForm

def home(request):
    return render(request, 'cv_app/home.html')

@login_required
def create_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            return redirect('view_cv')
    else:
        form = CVForm()
    return render(request, 'cv_app/create_cv.html', {'form': form})

@login_required
def view_cv(request):
    cv = CV.objects.get(user=request.user)
    return render(request, 'cv_app/view_cv.html', {'cv': cv})

# Create your views here.
