from builders.MySqlDbManager import MySqlDbManager

class MariaDbManager(MySqlDbManager):
    name: str = 'mariadb'
