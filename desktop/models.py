from django.db import models


class Desktop(models.model):
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField()
    osArchitecture = models.CharField()
    memory = models.CharField()
    cpuNames = models.CharField()
    cpuCores = models.IntegerField()
    process = models.CharField()
    gpuNames = models.CharField()
    gpuVideoProcessors = models.CharField()
