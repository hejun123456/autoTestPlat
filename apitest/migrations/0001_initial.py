# Generated by Django 3.1.6 on 2021-02-06 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20210201_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apitest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apitestname', models.CharField(max_length=64, verbose_name='流程接口名称')),
                ('apitestdesc', models.CharField(max_length=64, null=True, verbose_name='描述')),
                ('apitester', models.CharField(max_length=64, verbose_name='测试负责人')),
                ('apitestresult', models.CharField(max_length=200, verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
            options={
                'verbose_name': '流程场景接口',
                'verbose_name_plural': '流程场景接口',
            },
        ),
        migrations.CreateModel(
            name='Apistep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiname', models.CharField(max_length=100, verbose_name='接口名称')),
                ('apiurl', models.CharField(max_length=200, verbose_name='url地址')),
                ('apistep', models.CharField(max_length=100, null=True, verbose_name='测试步骤')),
                ('apiparamvalue', models.CharField(max_length=800, verbose_name='请求参数和值')),
                ('apimethod', models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, null=True, verbose_name='请求方法')),
                ('apiresult', models.CharField(max_length=200, verbose_name='预期结果')),
                ('apiresponse', models.CharField(max_length=5000, null=True, verbose_name='响应数据')),
                ('apistatus', models.BooleanField(verbose_name='是否通过')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('apitest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitest.apitest')),
            ],
        ),
    ]
