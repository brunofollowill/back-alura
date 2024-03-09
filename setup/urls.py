from django.contrib import admin
from django.urls import path, include
from menueasy.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAlunos, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Clunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAlunos.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
    
]
