import peewee as pw

SQL = pw.SQL


def migrate(migrator, database, fake=False, **kwargs):
    """Write your migrations here."""
    @migrator.create_model
    class Social(pw.Model):
        id = pw.AutoField()
        name = pw.TextField()
        specialty = pw.TextField()

        class Meta:
            table_name = "social"


def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""
    migrator.remove_model('social')
