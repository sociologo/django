# Generated by Django 5.1.6 on 2025-02-22 19:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_habilidades_empleado_avatar_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
