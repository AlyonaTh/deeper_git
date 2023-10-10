from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_eagle', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]