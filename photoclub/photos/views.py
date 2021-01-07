from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.urls import reverse_lazy

# Create your views here.
# from django.views.generic import CreateView

from photoclub.core.clean_up import clean_up_files
from photoclub.photos.forms.comment_form import CommentForm
from photoclub.photos.forms.photo_form import PhotoForm
from photoclub.photos.models import Photo, Comment, Like


def list_photos(request):
    context = {
        'photos': Photo.objects.all()
    }
    return render(request, 'photos/photos_list.html', context)


@login_required
def details_or_comment_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'photo': photo,
            'form': CommentForm(),
            'can_delete': request.user == photo.user.user,
            'can_edit': request.user == photo.user.user,
            'can_like': request.user != photo.user.user,
            'has_like': photo.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != photo.user.user,

        }
        return render(request, 'photos/photos_details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'], )
            comment.photo = photo
            comment.user = request.user.userprofile
            comment.save()
            return redirect('photo details or comment', pk)
        context = {
            'photo': photo,
            'form': form,
        }
        return render(request, 'photos/photos_details.html', context)


@login_required
def like_photo(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, photo_id=pk).first()
    if like:
        like.delete()
    else:
        photo = Photo.objects.get(pk=pk)
        like = Like(user=request.user.userprofile)
        like.photo = photo
        like.save()
    return redirect('photo details or comment', pk)


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if photo.user.user != request.user:
        # forbiden
        pass
    if request.method == 'GET':
        context = {
            'photo': photo,
        }
        return render(request, 'photos/photo_delete.html', context)
    else:
        photo.delete()
        return redirect('list photos')


# def edit_photo(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = PhotoForm(instance=pet)
#         context = {
#             'form': form,
#             'photo': photo,
#         }
#         return render(request, 'photo_edit.html', context)
#     else:
#         form = PhotoForm(request.POST, instance=photo)
#         if form.is_valid():
#             form.save()
#             return redirect('photo details or comment', photo.pk)
#         context = {
#             'form': form,
#             'photo': photo,
#         }
#         return render(request, 'photo_edit.html', context)


# def create_photo(request):
#
#     if request.method == 'GET':
#         form = PhotoForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'photo_create.html', context)
#     else:
#         form = PhotoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list photo')
#         context = {
#             'form': form,
#         }
#         return render(request, 'photo_create.html', context)


def persist_photo(request, photo, template_name):
    if request.method == 'GET':
        form = PhotoForm(instance=photo)
        context = {
            'form': form,
            'photo': photo,
        }
        return render(request, f'{template_name}', context)
    else:
        old_image = photo.image
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            if old_image:
                clean_up_files(old_image.path)
            photo = form.save(commit=False)
            photo.user = request.user.userprofile
            photo.save()
            form.save()
            Like.objects.filter(photo_id=photo.id).delete()
            return redirect('photo details or comment', photo.pk)
        context = {
            'form': form,
            'photo': photo,
        }
        return render(request, f'{template_name}', context)


@login_required
def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    return persist_photo(request, photo, 'photos/photo_edit.html')


@login_required
def create_photo(request):
    photo = Photo()
    return persist_photo(request, photo, 'photos/photo_create.html')


