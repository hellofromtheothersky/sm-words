# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Classes(models.Model):
    class_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    classname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'classes'


class Enrolment(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'enrolment'
        unique_together = (('user', 'class_field'),)


class Lists(models.Model):
    list_id = models.AutoField(primary_key=True)
    listname = models.CharField(max_length=20)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lists'


class Sentences(models.Model):
    sentences_id = models.AutoField(primary_key=True)
    sentences = models.CharField(max_length=200)
    meaning = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    word_start_pos = models.IntegerField()
    word_end_pos = models.IntegerField()
    list = models.ForeignKey(Lists, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sentences'


class Teaching(models.Model):
    class_field = models.OneToOneField(Classes, models.DO_NOTHING, db_column='class_id', primary_key=True)  # Field renamed because it was a Python reserved word.
    list = models.ForeignKey(Lists, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teaching'
        unique_together = (('class_field', 'list'),)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=15)
    passw = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'users'
