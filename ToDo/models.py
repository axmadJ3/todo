from django.db import models

class Todo(models.Model):
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False, choices=[(True, 'Выполнено'), 
                                                          (False, 'Не выполнено')])
    
    def __str__(self):
        return self.title
