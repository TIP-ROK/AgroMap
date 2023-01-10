# Generated by Django 4.1.2 on 2023-01-10 12:41

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTypeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('type_name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категории земель',
                'verbose_name_plural': 'Категории земель',
            },
        ),
        migrations.CreateModel(
            name='DocumentTypeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('type_name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Правоустанавливающие документы',
                'verbose_name_plural': 'Правоустанавливающие документы',
            },
        ),
        migrations.CreateModel(
            name='LandTypeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('type_name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Данные по типам угодьев',
                'verbose_name_plural': 'Данные по типам угодьев',
            },
        ),
        migrations.CreateModel(
            name='PropertyTypeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('type_name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Данные о собственности',
                'verbose_name_plural': 'Данные о собственности',
            },
        ),
        migrations.CreateModel(
            name='LandInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('ink_code', models.CharField(max_length=100, unique=True, verbose_name='Код ИНК')),
                ('main_map', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326, verbose_name='Контур')),
                ('eni_code', models.CharField(blank=True, max_length=35, null=True, verbose_name='ЕНИ Код')),
                ('inn_pin', models.IntegerField(blank=True, null=True, verbose_name='ИНН')),
                ('bonitet', models.IntegerField(blank=True, null=True, verbose_name='Бонитет')),
                ('culture', models.CharField(blank=True, max_length=255, null=True, verbose_name='Культура')),
                ('crop_yield', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='Урожайность')),
                ('document_link', models.FileField(blank=True, null=True, upload_to='document', verbose_name='Ссылка на документ')),
                ('square', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='Фактическая площадь')),
                ('land_legalarea', models.CharField(blank=True, max_length=100, null=True, verbose_name='Юридическая площадь (АСР)')),
                ('longitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Долгота')),
                ('latitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Широта')),
                ('land_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='Земля №')),
                ('territorial_outline', models.CharField(blank=True, max_length=100, null=True, verbose_name='Административно-территориальное деление')),
                ('number_realestateunits', models.CharField(blank=True, max_length=100, null=True, verbose_name='Количество единиц недвижимости')),
                ('circuit_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер контура')),
                ('owner_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Данные о собственнике (АСР)')),
                ('doc_enttitlement', models.CharField(blank=True, max_length=255, null=True, verbose_name='Право на документ')),
                ('use_period', models.CharField(blank=True, max_length=55, null=True, verbose_name='Срок пользования (год/лет)')),
                ('certifying_act', models.CharField(blank=True, max_length=55, null=True, verbose_name='Удостоверяющий акт (прикрепить файл)')),
                ('use_end', models.CharField(blank=True, max_length=55, null=True, verbose_name='Дата завершения пользования')),
                ('agroland_purposes', models.CharField(blank=True, max_length=55, null=True, verbose_name='Земли сельскохозяйственного назначения')),
                ('gfsu', models.CharField(blank=True, max_length=255, null=True, verbose_name='Государственный фонд сельскохозяйственных угодий')),
                ('lands_pop_areas', models.CharField(blank=True, max_length=55, null=True, verbose_name='Земли населенных пунктов')),
                ('othertypes_lands', models.CharField(blank=True, max_length=55, null=True, verbose_name='Другие виды угодий')),
                ('type_of_land', models.CharField(blank=True, max_length=255, null=True, verbose_name='Земельные угодья')),
                ('agro_type_land', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сельскохозяйственный вид угодий')),
                ('desc_brd', models.TextField(blank=True, null=True, verbose_name='Описания ограничения')),
                ('date_of_completion', models.CharField(blank=True, max_length=55, null=True, verbose_name='Дата заполнения')),
                ('perrenial_plant', models.CharField(blank=True, max_length=255, null=True, verbose_name='Многолетние насаждения')),
                ('forest_areas', models.CharField(blank=True, max_length=255, null=True, verbose_name='Лесные площади')),
                ('underwater', models.CharField(blank=True, max_length=255, null=True, verbose_name='Под водой')),
                ('otherlands', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прочие земли')),
                ('collective_gardens_and_veg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Коллективные сады и огороды')),
                ('irrigated', models.CharField(blank=True, max_length=3, null=True, verbose_name='Орошаемые')),
                ('rainfed', models.CharField(blank=True, max_length=3, null=True, verbose_name='Богарные')),
                ('improved_radical', models.CharField(blank=True, max_length=3, null=True, verbose_name='Улучшенные (коренного улучшения)')),
                ('inaccessible', models.CharField(blank=True, max_length=3, null=True, verbose_name='Неиспользуемый из-за труднодоступности')),
                ('intensive_use', models.CharField(blank=True, max_length=3, null=True, verbose_name='Интенсивное использование')),
                ('pasture', models.CharField(blank=True, max_length=255, null=True, verbose_name='Пастбище')),
                ('plant_not_forestfund', models.CharField(blank=True, max_length=255, null=True, verbose_name='Древесно кустарниковые насаждения, не входящие в государственный лесной фонд')),
                ('property_form', models.CharField(blank=True, max_length=255, null=True, verbose_name='Форма собственности')),
                ('disturbed_lands', models.CharField(blank=True, max_length=255, null=True, verbose_name='Нарушенные земли')),
                ('lot_number', models.CharField(blank=True, max_length=55, null=True, verbose_name='Номер участка')),
                ('elementary_sectionnumber', models.CharField(blank=True, max_length=55, null=True, verbose_name='Номер элементарного участка')),
                ('asr_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес участка (АСР)')),
                ('special_purpose_asr', models.CharField(blank=True, max_length=100, null=True, verbose_name='Целевое назначение (АСР)')),
                ('descriptiom_doc', models.TextField(blank=True, null=True, verbose_name='Описание (в случае необходимости)')),
                ('udp', models.CharField(blank=True, max_length=255, null=True, verbose_name='Угодья длительного пользования')),
                ('limite', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ограничения')),
                ('land_factarea_asr', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фактическая площадь (АСР)')),
                ('form_using_asr', models.CharField(blank=True, max_length=55, null=True, verbose_name='Форма использования (АСР)')),
                ('haushold_land', models.CharField(blank=True, max_length=55, null=True, verbose_name='Приусадебные земли и служебные наделы граждан')),
                ('number_of_yards', models.CharField(blank=True, max_length=55, null=True, verbose_name='Число дворов')),
                ('number_of_families', models.CharField(blank=True, max_length=55, null=True, verbose_name='Число семей')),
                ('total_land', models.CharField(blank=True, max_length=55, null=True, verbose_name='Всего земель')),
                ('crmid', models.CharField(blank=True, max_length=55, null=True)),
                ('smcreatorid', models.CharField(blank=True, max_length=55, null=True)),
                ('smownerid', models.CharField(blank=True, max_length=55, null=True)),
                ('modifiedby', models.CharField(blank=True, max_length=55, null=True)),
                ('setype', models.CharField(blank=True, max_length=55, null=True)),
                ('description', models.CharField(blank=True, max_length=55, null=True)),
                ('land_ctg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Категории Земли (Зем. Баланс)')),
                ('status', models.CharField(blank=True, max_length=55, null=True)),
                ('category_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_info', to='hub.categorytypelist', verbose_name='категории земель')),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_info', to='hub.documenttypelist', verbose_name='правоустанавливающие документы')),
                ('land_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_info', to='hub.landtypelist', verbose_name='данные по типам угодьев')),
                ('property_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_info', to='hub.propertytypelist', verbose_name='данные о собственности')),
            ],
            options={
                'verbose_name': 'Главная таблица',
                'verbose_name_plural': 'Главная таблица',
            },
        ),
        migrations.CreateModel(
            name='HistoricalLandInfo',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='время обновления')),
                ('ink_code', models.CharField(db_index=True, max_length=100, verbose_name='Код ИНК')),
                ('main_map', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326, verbose_name='Контур')),
                ('eni_code', models.CharField(blank=True, max_length=35, null=True, verbose_name='ЕНИ Код')),
                ('inn_pin', models.IntegerField(blank=True, null=True, verbose_name='ИНН')),
                ('bonitet', models.IntegerField(blank=True, null=True, verbose_name='Бонитет')),
                ('culture', models.CharField(blank=True, max_length=255, null=True, verbose_name='Культура')),
                ('crop_yield', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='Урожайность')),
                ('document_link', models.TextField(blank=True, max_length=100, null=True, verbose_name='Ссылка на документ')),
                ('square', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True, verbose_name='Фактическая площадь')),
                ('land_legalarea', models.CharField(blank=True, max_length=100, null=True, verbose_name='Юридическая площадь (АСР)')),
                ('longitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Долгота')),
                ('latitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Широта')),
                ('land_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='Земля №')),
                ('territorial_outline', models.CharField(blank=True, max_length=100, null=True, verbose_name='Административно-территориальное деление')),
                ('number_realestateunits', models.CharField(blank=True, max_length=100, null=True, verbose_name='Количество единиц недвижимости')),
                ('circuit_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер контура')),
                ('owner_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Данные о собственнике (АСР)')),
                ('doc_enttitlement', models.CharField(blank=True, max_length=255, null=True, verbose_name='Право на документ')),
                ('use_period', models.CharField(blank=True, max_length=55, null=True, verbose_name='Срок пользования (год/лет)')),
                ('certifying_act', models.CharField(blank=True, max_length=55, null=True, verbose_name='Удостоверяющий акт (прикрепить файл)')),
                ('use_end', models.CharField(blank=True, max_length=55, null=True, verbose_name='Дата завершения пользования')),
                ('agroland_purposes', models.CharField(blank=True, max_length=55, null=True, verbose_name='Земли сельскохозяйственного назначения')),
                ('gfsu', models.CharField(blank=True, max_length=255, null=True, verbose_name='Государственный фонд сельскохозяйственных угодий')),
                ('lands_pop_areas', models.CharField(blank=True, max_length=55, null=True, verbose_name='Земли населенных пунктов')),
                ('othertypes_lands', models.CharField(blank=True, max_length=55, null=True, verbose_name='Другие виды угодий')),
                ('type_of_land', models.CharField(blank=True, max_length=255, null=True, verbose_name='Земельные угодья')),
                ('agro_type_land', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сельскохозяйственный вид угодий')),
                ('desc_brd', models.TextField(blank=True, null=True, verbose_name='Описания ограничения')),
                ('date_of_completion', models.CharField(blank=True, max_length=55, null=True, verbose_name='Дата заполнения')),
                ('perrenial_plant', models.CharField(blank=True, max_length=255, null=True, verbose_name='Многолетние насаждения')),
                ('forest_areas', models.CharField(blank=True, max_length=255, null=True, verbose_name='Лесные площади')),
                ('underwater', models.CharField(blank=True, max_length=255, null=True, verbose_name='Под водой')),
                ('otherlands', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прочие земли')),
                ('collective_gardens_and_veg', models.CharField(blank=True, max_length=255, null=True, verbose_name='Коллективные сады и огороды')),
                ('irrigated', models.CharField(blank=True, max_length=3, null=True, verbose_name='Орошаемые')),
                ('rainfed', models.CharField(blank=True, max_length=3, null=True, verbose_name='Богарные')),
                ('improved_radical', models.CharField(blank=True, max_length=3, null=True, verbose_name='Улучшенные (коренного улучшения)')),
                ('inaccessible', models.CharField(blank=True, max_length=3, null=True, verbose_name='Неиспользуемый из-за труднодоступности')),
                ('intensive_use', models.CharField(blank=True, max_length=3, null=True, verbose_name='Интенсивное использование')),
                ('pasture', models.CharField(blank=True, max_length=255, null=True, verbose_name='Пастбище')),
                ('plant_not_forestfund', models.CharField(blank=True, max_length=255, null=True, verbose_name='Древесно кустарниковые насаждения, не входящие в государственный лесной фонд')),
                ('property_form', models.CharField(blank=True, max_length=255, null=True, verbose_name='Форма собственности')),
                ('disturbed_lands', models.CharField(blank=True, max_length=255, null=True, verbose_name='Нарушенные земли')),
                ('lot_number', models.CharField(blank=True, max_length=55, null=True, verbose_name='Номер участка')),
                ('elementary_sectionnumber', models.CharField(blank=True, max_length=55, null=True, verbose_name='Номер элементарного участка')),
                ('asr_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес участка (АСР)')),
                ('special_purpose_asr', models.CharField(blank=True, max_length=100, null=True, verbose_name='Целевое назначение (АСР)')),
                ('descriptiom_doc', models.TextField(blank=True, null=True, verbose_name='Описание (в случае необходимости)')),
                ('udp', models.CharField(blank=True, max_length=255, null=True, verbose_name='Угодья длительного пользования')),
                ('limite', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ограничения')),
                ('land_factarea_asr', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фактическая площадь (АСР)')),
                ('form_using_asr', models.CharField(blank=True, max_length=55, null=True, verbose_name='Форма использования (АСР)')),
                ('haushold_land', models.CharField(blank=True, max_length=55, null=True, verbose_name='Приусадебные земли и служебные наделы граждан')),
                ('number_of_yards', models.CharField(blank=True, max_length=55, null=True, verbose_name='Число дворов')),
                ('number_of_families', models.CharField(blank=True, max_length=55, null=True, verbose_name='Число семей')),
                ('total_land', models.CharField(blank=True, max_length=55, null=True, verbose_name='Всего земель')),
                ('crmid', models.CharField(blank=True, max_length=55, null=True)),
                ('smcreatorid', models.CharField(blank=True, max_length=55, null=True)),
                ('smownerid', models.CharField(blank=True, max_length=55, null=True)),
                ('modifiedby', models.CharField(blank=True, max_length=55, null=True)),
                ('setype', models.CharField(blank=True, max_length=55, null=True)),
                ('description', models.CharField(blank=True, max_length=55, null=True)),
                ('land_ctg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Категории Земли (Зем. Баланс)')),
                ('status', models.CharField(blank=True, max_length=55, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='hub.categorytypelist', verbose_name='категории земель')),
                ('document_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='hub.documenttypelist', verbose_name='правоустанавливающие документы')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('land_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='hub.landtypelist', verbose_name='данные по типам угодьев')),
                ('property_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='hub.propertytypelist', verbose_name='данные о собственности')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'historical Главная таблица',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
