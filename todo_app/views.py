from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated





class TodoListView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        statuses = self.request.query_params.get('task_status')
        
        if statuses:
            # Link to only pending will be todos/?task_status=PENDING 
            # same for all.
            return Todo.objects.filter(task_status=statuses)
        return Todo.objects.filter(task_user=user)



class TodoDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(task_user=user)