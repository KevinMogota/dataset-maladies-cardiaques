from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib


class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    sbp = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(600)], null=True)
    tobacco = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)], null=True)
    ldl = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)], null=True)
    adiposity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    famhist = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    type = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    obesity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    alcohol = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)], null=True)		
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], null=True)			
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_cardiac_model.joblib')
        self.predictions = ml_model.predict([[self.sbp, self.tobacco, self.ldl, self.adiposity, self.famhist, self.type, self.obesity, self.alcohol, self.age]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name