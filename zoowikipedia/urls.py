from django.urls import path, re_path

from .views import *

urlpatterns = [
    # Стартовая страница
    path('', index, name='home'),

    # Страница о сайте
    path('about/', about, name='about'),

    # Страница выбора объекта
    path('action_page/', actionPage, name='action_page'),

    # Страница для добавления нового класса
    path('create_classis/', addClassis, name='create_classis'),

    # Страница для добавления нового отряда
    path('create_ordo/', addOrdo, name='create_ordo'),

    # Страница для добавления нового семейства
    path('create_familia/', addFamilia, name='create_familia'),

    # Удаление поста про класс
    path('delete_classis/<int:id>/', delClassis),

    # Удаление поста про отряд
    path('classis_list/<int:classis_list_id>/delete_ordo/<int:id>/', delOrdo),

    # Удаление поста про семейство
    path('classis_list/<int:classis_list_id>/ordo_list/<int:ordo_list_id>/delete_familia/<int:id>/', delFamilia),

    # Редактирование поста про класс
    path('edit_classis/<int:id>/', editClassis),

    # Редактирование поста про отряд
    path('classis_list/<int:classis_list_id>/edit_ordo/<int:id>/', editOrdo),

    # Редактирование поста про семейство
    path('classis_list/<int:classis_list_id>/ordo_list/<int:ordo_list_id>/edit_familia/<int:id>/', editFamilia),



    # Страница с постом выбранного класса
    path('classis_post/<int:classis_post_id>/', show_classis, name='classis_post'),

    # Отряды выбранного в левом сайдбаре класса
    path('classis_list/<int:classis_list_id>/', list_ordo, name='sidebar_classis_list'),




    # Страница с постом выбранного отряда
    path('classis_list/<int:classis_id>/ordo_post/<int:ordo_post_id>/', show_ordo, name='ordo_post'),

    # Семейства выбранного в левом сайдбаре отряда
    path('classis_list/<int:classis_id>/ordo_list/<int:ordo_list_id>/', list_familia, name='sidebar_ordo_list'),



    # Страница с постом выбранного семейства
    path('classis_list/<int:classis_id>/ordo_list/<int:ordo_id>/familia_post/<int:familia_post_id>/', show_familia, name='familia_post'),
]