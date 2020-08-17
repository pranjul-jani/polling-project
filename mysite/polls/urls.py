from django.urls import path, include
from .views import IndexView, DetailView, ResultView, vote

# this is url namespace this is included so that any html page can recognize which url from this app needs to be,
# addressed in case there are multiple apps with same url name for eg:- many url will have detail name

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultView.as_view(), name='results'),
    path('<int:pk>/vote/', vote, name='vote'),
]