import peewee as pw

SQL = pw.SQL


def migrate(migrator, database, fake=False, **kwargs):
    """Write your migrations here."""
    @migrator.create_model
    class Medic(pw.Model):
        id = pw.AutoField()
        academic = pw.TextField()
        city = pw.TextField()
        name = pw.TextField()
        specialty = pw.TextField()
        title = pw.TextField()

        class Meta:
            table_name = "medic"


def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""
    migrator.remove_model('medic')
