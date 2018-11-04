# import random


class MasterSlaveDbRouter:

    def db_for_read(self, model, **hints):
        return 'slave1'
        # return random.choice(['slave1', 'slave1', 'slave2', 'slave3'])

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
