from django.db import models


class Books(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='图书编号')
    name = models.CharField(max_length=100, verbose_name='图书名称')
    status = models.BooleanField(default=True, verbose_name='是否可借')

    class Meta:
        db_table = 'books'
        verbose_name = '图书表'
    def __str__(self):
        return self.name

class Record(models.Model):
    book = models.ForeignKey('Books',on_delete=models.CASCADE,verbose_name='借还记录')
    sdate = models.BooleanField(verbose_name='是否归还')
    name = models.CharField(max_length=50,verbose_name='借书人姓名')
    s_time = models.DateField(auto_created=True,verbose_name='借书时间')
    e_time = models.DateField(auto_created=True, verbose_name='还书时间')
    class Meta:
        db_table = 'record'
        verbose_name = '借还记录表'
    def __str__(self):
        return self.name
