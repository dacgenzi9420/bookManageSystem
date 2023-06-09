# Generated by Django 3.2 on 2023-06-08 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='图书编号')),
                ('name', models.CharField(max_length=100, verbose_name='图书名称')),
                ('status', models.BooleanField(default=True, verbose_name='是否可借')),
            ],
            options={
                'verbose_name': '图书表',
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_time', models.DateField(auto_created=True, verbose_name='还书时间')),
                ('s_time', models.DateField(auto_created=True, verbose_name='借书时间')),
                ('sdate', models.BooleanField(verbose_name='是否归还')),
                ('name', models.CharField(max_length=50, verbose_name='借书人姓名')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books', verbose_name='借还记录')),
            ],
            options={
                'verbose_name': '借还记录表',
                'db_table': 'record',
            },
        ),
    ]