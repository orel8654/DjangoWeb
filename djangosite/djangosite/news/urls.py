from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import mycv.views
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='cat'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add_news/', add_news, name='add_news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)