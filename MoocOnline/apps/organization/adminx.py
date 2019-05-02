# _*_ coding: utf-8 _*_
__author__ = 'Ren Tingsong'
__date__ = '2019/3/5 0005 下午 7:27'

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'image', 'address', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name', 'desc', 'image', 'address', 'click_nums', 'fav_nums']
    list_filter = ['city', 'name', 'desc', 'image', 'address', 'click_nums', 'fav_nums', 'add_time']
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                   'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
