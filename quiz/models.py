from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_title = models.CharField(max_length = 50, default="")
    quiz_description = models.CharField(max_length = 100)
    quiz_difficulty = models.IntegerField(default = 0)

class Question(models.Model):
    quiz_foreign_key = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    question_title = models.CharField(max_length = 50,default="")
    question_text = models.CharField(max_length = 100)
    is_multi_answer = models.BooleanField(default = False)

class Answer(models.Model):
    question_foreign_key = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer_title = models.CharField(max_length = 50,default="")
    answer_text = models.CharField(max_length = 100)
    is_correct_answer = models.BooleanField(default = False)
    number_of_points = models.IntegerField(default = 0)
