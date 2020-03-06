# Generated by Django 3.0.3 on 2020-03-06 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('english_name', models.CharField(max_length=45)),
                ('image', models.URLField(max_length=500)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('english_name', models.CharField(max_length=45)),
                ('number', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.URLField(max_length=500)),
            ],
            options={
                'db_table': 'guides',
            },
        ),
        migrations.CreateModel(
            name='MainTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'main_themes',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation_list', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'recommendations',
            },
        ),
        migrations.CreateModel(
            name='SubTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('main_theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.MainTheme')),
            ],
            options={
                'db_table': 'sub_themes',
            },
        ),
        migrations.CreateModel(
            name='TourProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=200)),
                ('group', models.CharField(max_length=45, null=True)),
                ('duration', models.CharField(max_length=45, null=True)),
                ('language', models.CharField(max_length=45, null=True)),
                ('transportation', models.CharField(max_length=45, null=True)),
                ('description_title', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('notice_title', models.TextField(null=True)),
                ('notice', models.TextField(null=True)),
                ('amenity', models.TextField(null=True)),
                ('non_amenity', models.TextField(null=True)),
                ('meeting_time', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('address_map', models.URLField(null=True)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Country')),
                ('guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Guide')),
                ('main_theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.MainTheme')),
                ('sub_theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.SubTheme')),
            ],
            options={
                'db_table': 'tour_products',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('discount_percent', models.IntegerField()),
                ('tour_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.TourProduct')),
            ],
            options={
                'db_table': 'price',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumnail', models.URLField(max_length=500)),
                ('product_image', models.URLField(max_length=500)),
                ('tour_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.TourProduct')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.URLField(max_length=500)),
                ('tour_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.TourProduct')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Country'),
        ),
    ]
