from .models import Task
def add_variable_to_context(request):
    undone = Task.objects.filter(done=False).count()

    return {
        'not_count':undone
    }