from django.urls import path

from photoclub.photos.views import list_photos, like_photo, details_or_comment_photo, edit_photo, delete_photo, \
   create_photo

urlpatterns = [
    path('', list_photos, name='list photos'),
    path('detail/<int:pk>/', details_or_comment_photo, name='photo details or comment'),
    path('like/<int:pk>/', like_photo, name='like photo'),
    path('edit/<int:pk>/', edit_photo, name='edit photo'),
    path('delete/<int:pk>/', delete_photo, name='delete photo'),
    path('create/', create_photo, name='create photo'),
    # path('create/', PhotoCreateView.as_view(), name='cbv create photo'),

]
