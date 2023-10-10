
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('count_views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.author')),
            ],
        ),
    ]