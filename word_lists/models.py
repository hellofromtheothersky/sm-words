# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


# class Classes(models.Model):
#     class_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey('auth_user', models.DO_NOTHING)
#     classname = models.CharField(max_length=50)
#     class Meta:
#         db_table = "classes"


# class Enrolment(models.Model):
#     user = models.OneToOneField('auth_user', models.DO_NOTHING, primary_key=True)
#     class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
#     class Meta:
#         db_table = "enrolment"


class Lists(models.Model):
    list_id = models.AutoField(primary_key=True)
    listname = models.CharField(max_length=20)
    user = models.ForeignKey(User, models.DO_NOTHING)
    class Meta:
        db_table = "lists"


class Sentences(models.Model):
    sentence_id = models.AutoField(primary_key=True)
    sentence = models.CharField(max_length=200)
    meaning = models.CharField(max_length=50, blank=True, null=True)
    lemma = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    word_start_pos = models.IntegerField()
    word_end_pos = models.IntegerField()
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    class Meta:
        db_table = "sentences"
