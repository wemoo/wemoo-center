# coding: utf8

from config import environment

from peewee import Model
from peewee import CharField
from peewee import DateTimeField

from peewee import IntegerField

from peewee import FloatField
from peewee import DateField


class Role(Model):
    name = CharField()
    is_athlete = IntegerField()
    height = FloatField()
    sex = IntegerField()
    birthday = DateField()
    server_time = DateTimeField()
    user_id = IntegerField()
    head_portrait_url = CharField()
    gole_weight = FloatField()
    picooc_index_accumulate = IntegerField()
    goal_fat = FloatField()
    step_state_job = IntegerField()
    step_state_life = IntegerField()
    goal_step = IntegerField()
    first_weight = FloatField()
    first_fat = FloatField()
    first_use_time = DateTimeField()

    class Meta:
        database = environment.config.DB
        db_table = 'role'

    @classmethod
    def get_by_id(cls, role_id):
        try:
            role = cls.select().where(cls.id == role_id)
        except cls.DoesNotExist:
            role = None

        return role

    @classmethod
    def find_by_user_id(cls, user_id):
        try:
            roles = cls.select().where(cls.user_id == user_id)
        except cls.DoesNotExist:
            roles = None

        return list(roles)
