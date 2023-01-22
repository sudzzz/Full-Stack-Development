from django.db import models

# Create your models here.
MyValues = ["201", "202", "203", "204"]
class Employee:
    code=""
    name=""

    def RetValues(self):
        return MyValues


