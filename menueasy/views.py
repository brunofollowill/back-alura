from rest_framework import viewsets, generics
from menueasy.models import Aluno, Curso, Matricula
from menueasy.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunosSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CursosViewSet(viewsets.ModelViewSet):
    """Todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
   """Todos os cursos"""
   queryset = Matricula.objects.all()
   serializer_class = MatriculaSerializer
   
class ListaMatriculasAlunos(generics.ListAPIView):
    """Listando as matriculas"""
    def get_queryset(self):
         queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
         return queryset
    serializer_class = ListaMatriculasAlunosSerializer
    

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
 