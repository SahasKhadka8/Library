from django.urls import path
from .import views
from logsin.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns=[
    path('home',views.library,name='Home'),
    path('upload',views.upload,name='upload-book'),
    path('update/<int:book_id>',views.update_book,name='update'),
    path('delete/<int:book_id>',views.delete_book,name='delete'),
    path('logout',views.LogoutPage,name='logout')
]

if DEBUG:
    urlpatterns+= static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns+= static(MEDIA_URL,document_root=MEDIA_ROOT)