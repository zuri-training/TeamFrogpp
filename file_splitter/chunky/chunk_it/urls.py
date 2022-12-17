from django.views.generic import TemplateView
from django.urls import path
from .views import signup, signin,  ChunkFile,  Dashboard, ContactUs, Privacy, Forget

app_name = "chunk_it"
urlpatterns = [
    # User authentication urls
    path('', TemplateView.as_view(template_name="chunk_it/landingpg.html"), name='landingpg'),
    path('signup', signup, name ='signup'),
    path('login', signin, name='login'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('chunkfile', ChunkFile.as_view(),name='chunk'),
    # path('download', download, name='download'),
    path('contact', ContactUs.as_view(), name='contact'),
    path('privacy', Privacy.as_view(), name='privacy'),
    path('forget', Forget.as_view(), name='forget'),

]