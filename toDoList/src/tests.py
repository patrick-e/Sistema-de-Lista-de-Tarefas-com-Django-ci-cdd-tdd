from django.test import TestCase

# Create your tests here.
from .models import Task

class TaskTest(TestCase):

    def to_Do_List(self):
        task = Task.objects.count()
        self.assertEqual(task,0)

    def test_represation_string(self):
        task = Task.objects.create(titulo_tarefa="primeiro titulo testado")
        self.assertEqual(str(task),task.titulo_tarefa)