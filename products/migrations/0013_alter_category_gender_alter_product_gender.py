# Generated by Django 4.2.4 on 2023-10-13 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_category_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('man', 'man'), ('woman', 'woman'), ('boy', 'boy'), ('girl', 'girl')], max_length=5, verbose_name='Для кого'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('man', 'man'), ('woman', 'woman'), ('boy', 'boy'), ('girl', 'girl')], max_length=5, verbose_name='Для кого'),
        ),
    ]
