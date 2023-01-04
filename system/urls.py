"""tdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from . import views 
from . import testdb

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('index/timeseries/', views.timeseries_index),
    path('index/decision/', views.decision_index),
    path('index/saving/', views.saving_index),
    path('index/login/', views.login_index),
    path('index/modify/', views.modify_index),
    path('index/paper-signup/', views.paper_signup_index),
    path('index/implement-signup/', views.implement_signup_index),
    path('index/permission-setting/', views.permission_setting_index),

    #path('tdb/add/', views.add),
    path('tdb/api/login/', views.login),
    path('tdb/api/paper_add/', views.paper_add),
    path('tdb/api/implement_add/', views.implement_add),
    path('tdb/api/permission_add/', views.permission_add),

    path('tdb/api/field_add/', views.field_add),
    path('tdb/api/project_add/', views.project_add),
    path('tdb/api/methodology_add/', views.methodology_add),
    path('tdb/api/hitcount_add/', views.hitcount_add),
    path('tdb/api/search_add/', views.search_add),

    # path('tdb/getall/', testdb.getALL),
    # re_path(r'tdb/update$', testdb.update),
    path('tdb/api/field_modify/', views.field_modify),
    path('tdb/api/project_modify/', views.project_modify),
    path('tdb/api/methodology_modify/', views.methodology_modify),

    path('tdb/api/field_delete/', views.field_delete),
    path('tdb/api/project_delete/', views.project_delete),
    path('tdb/api/methodology_delete/', views.methodology_delete),

    path('tdb/api/search_add/', views.search_add),
    path('tdb/api/star_add/', views.star_add),
]
