from apps.catalog.models import Category, Section
from apps.products.models import Product


def get_category_list():
    bikes, _ = Category.objects.get_or_create(
        title='Велосипеды',
        defaults={
            'slug': 'bike',
            'description': ('Колёсное транспортное средство (или спортивный снаряд), '
                            'приводимое в движение мускульной силой человека через '
                            'ножные педали или (крайне редко) через ручные рычаги. '
                            'Наиболее распространены двухколёсные велосипеды, '
                            'но существуют также конструкции с тремя и более колёсами.'),
            'order': 0,
            'is_active': True,
        },
    )
    ski, _ = Category.objects.get_or_create(
        title='Лыжи',
        defaults={
            'slug': 'ski',
            'description': 'Приспособление в виде длинных полозьев для перемещения по снегу.',
            'order': 1,
            'is_active': True,
        },
    )
    return bikes, ski


def get_section_list(bikes, ski):
    road, _ = Section.objects.get_or_create(
        title='Шоссейные',
        category=bikes,
        defaults={
            'slug': 'road',
            'description': 'Для быстрого перемещения по ровной поверхности',
            'order': 0, 'is_active': True,
        }
    )
    hill, _ = Section.objects.get_or_create(
        title='Горные',
        category=bikes,
        defaults={
            'slug': 'hill',
            'description': 'Для преодоления пересеченной местности',
            'order': 1, 'is_active': True,
        }
    )
    child, _ = Section.objects.get_or_create(
        title='Детские',
        category=bikes,
        defaults={
            'slug': 'child',
            'description': 'Для самых маленьких путешественников',
            'order': 2, 'is_active': True,
        }
    )
    nordic, _ = Section.objects.get_or_create(
        title='Беговые',
        category=ski,
        defaults={
            'slug': 'nordic',
            'description': 'Для спортивных тренировок в лесу',
            'order': 0, 'is_active': True,
        }
    )
    alpine, _ = Section.objects.get_or_create(
        title='Горные',
        category=ski,
        defaults={
            'slug': 'alpine',
            'description': 'Для скоростных спусков с вершин',
            'order': 1, 'is_active': True,
        }
    )
    return road, hill, child, nordic, alpine


def add_objects():
    bikes, ski = get_category_list()
    road, hill, child, nordic, alpine = get_section_list(bikes, ski)
