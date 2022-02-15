from django.db import models


class reports(models.Model):
    uid = models.AutoField(primary_key=True)
    report_name = models.CharField(max_length=50)
    report_function = models.CharField(max_length=150)

    def __str__(self):
        return self.report_name