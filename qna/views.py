from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Write
from .forms import WriteForm


def writepage(request):
    all_write = Write.objects.all()
    q = request.GET.get('q', '')
    if q:
        all_write = all_write.filter(title__icontains=q)
    return render(request, 'qna/writepage.html', {'all_write': all_write, 'q' : q})


def create(request):
    if request.method == "POST":
        create_form = WriteForm(request.POST, request.FILES)
        if create_form.is_valid():
            rmf = create_form.save()
            rmf.author = request.user
            rmf.save()
            return redirect('writepage')
    else:
        create_form = WriteForm()
    return render(request, 'qna/create.html', {'create_form': create_form})


def detail(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    return render(request, 'qna/detail.html', {'my_write': my_write, "write_id":write_id})


def delete(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    my_write.delete()
    return redirect('writepage')

def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')
