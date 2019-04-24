from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import FileManager
from .forms import FileManagerForm


def file_list(request):
    files = FileManager.objects.all().distinct('file_name')
    context = {'files': files}
    return render(request, 'file_mngmnt/files_list.html', context)


def get_versions(request, file_name):
    files = FileManager.objects.filter(file_name=file_name)
    last_file = files.order_by('version').last()
    context = {'files': files,
               'last_file': last_file}
    return render(request, 'file_mngmnt/get_versions.html', context)


def upload_file(request):

    if request.method == "POST":
        file_form = FileManagerForm(request.POST)

        if file_form.is_valid():
            data = file_form.save(commit=False)
            data.file = request.FILES['file']
            data.file_name = data.file.name
            if FileManager.objects.filter(file_name=data.file_name).exists():
                return HttpResponse(
                    "ERROR::File with same name already exists")
            data.version = '0'
            data.save()
        return HttpResponseRedirect(reverse('file_mngmnt:file_list'))

    else:
        file_form = FileManagerForm()

        context = {
            "form": file_form,
            "title": "Upload a brand new File"
        }
        return render(request, 'file_mngmnt/upload_file.html', context)


def edit_and_upload_file(request, file_id):

    file = get_object_or_404(FileManager, pk=file_id)
    if request.method == "POST":
        version = file.version
        old_name = file.file_name
        new_version = str(int(version) + 1)
        file_form = FileManagerForm(request.POST)

        if file_form.is_valid():
            data = file_form.save(commit=False)
            data.file = request.FILES['file']
            data.file_name = data.file.name
            if data.file.name != old_name:
                return HttpResponse(
                    "ERROR::File name is different")
            data.version = new_version
            data.save()
        return HttpResponseRedirect(reverse
                                    ('file_mngmnt:get_versions',
                                        kwargs={'file_name': file.file_name}))

    else:
        file_form = FileManagerForm()

        context = {
            "form": file_form,
            "title": "Upload Edited File",
            "file": file
        }
        return render(request, 'file_mngmnt/edit_upload_file.html', context)
