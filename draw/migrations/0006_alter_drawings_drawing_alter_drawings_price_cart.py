# Generated by Django 4.2.9 on 2024-02-05 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0005_alter_drawings_drawing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawings',
            name='drawing',
            field=models.ImageField(null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('drawing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='draw.drawer')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='draw.drawings')),
            ],
        ),
    ]
