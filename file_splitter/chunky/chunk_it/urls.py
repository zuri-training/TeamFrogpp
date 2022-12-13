
from django.urls import path
from .views import signup,signin,signout, ChunkFile, History, landingpage, download

app_name = "chunk_it"
urlpatterns = [
    # User authentication urls
    path('', landingpage, name='landingpg'),
    path('signup/', signup, name ='signup'),
    path('signin/', signin, name = 'login'),
    path('signout/', signout, name = 'logout'),

    path('chunkfile/', ChunkFile.as_view(),name='chunk'),
    path('history/', History.as_view()),
    path('download/', download, name='download'),

]