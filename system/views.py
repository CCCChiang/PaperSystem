from datetime import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.db import connection
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from mltdc.models import Owner, Paper, Field, Project, Methodology, MLTDC_Join_Table, Implement_Join_Table, Evaluation
from collections import defaultdict
import datetime
import requests
import json

# Create your views here.
# @csrf_exempt
def index(request):

    # ownerid
    cursor = connection.cursor()
    sql_ownerid = '''
        select 
             ownerid
        from 
            mltdc_tdb.mltdc_owner as mo 
    '''
    cursor.execute(sql_ownerid)
    all_data = cursor.fetchall()
    
    ownerid_mapping = []
    for ownerid in all_data:
        # for id, _ownerid in ownerid:
        ownerid_mapping.append(ownerid[0])
    print(ownerid_mapping)

    # field
    cursor = connection.cursor()
    sql_field = '''
        select 
             field
        from 
            mltdc_tdb.mltdc_field as mf 
    '''
    cursor.execute(sql_field)
    all_data = cursor.fetchall()
    
    field_mapping = []
    for field in all_data:
        # for id, _field in field:
        field_mapping.append(field[0])
    print(field_mapping)

    # project
    sql_project = '''
        select 
             project
        from 
            mltdc_tdb.mltdc_project as mp 
    '''
    cursor.execute(sql_project)
    all_data = cursor.fetchall()
    
    project_mapping = []
    for project in all_data:
        # for id, _project in project:
        project_mapping.append(project[0])
    print(project_mapping)

    # methodology
    sql_methodology = '''
        select 
             methodology
        from 
            mltdc_tdb.mltdc_methodology as mm 
    '''
    cursor.execute(sql_methodology)
    all_data = cursor.fetchall()
    
    methodology_mapping = []
    for methodology in all_data:
        # for id, _methodology in methodology:
        methodology_mapping.append(methodology[0])
    print(methodology_mapping)

    # paper
    sql_paper = '''
        select 
             title
        from 
            mltdc_tdb.mltdc_paper as mp 
    '''
    cursor.execute(sql_paper)
    all_data = cursor.fetchall()
    
    paper_mapping = []
    for paper in all_data:
        # for id, _paper in paper:
        paper_mapping.append(paper[0])
    print(paper_mapping)

    # year
    year = list(map(lambda x: str(x), reversed(range(2000, 2023))))

    # button url mapping

    Button_url = [
        'http://127.0.0.1:8000/mltdc/index/timeseries/',
        'http://127.0.0.1:8000/mltdc/index/decision/',
        'http://127.0.0.1:8000/mltdc/index/saving/'
    ]

    for i in range(len(field_mapping)-3):
        Button_url.append('#')

    context = {
        'title': 'MLTDC TDB', 
        'Year' : year,
        'OwnerID' : ownerid_mapping,
        'Field' : field_mapping,
        'Project' : project_mapping,
        'Methodology' : methodology_mapping,
        'Paper' : paper_mapping,
        'Button_url' : list(zip(Button_url, field_mapping))
    }

    return render(request, 'index.html', context)

@csrf_exempt
def login_index(request):
    context = {'title': 'MLTDC TDB-login'}

    return render(request, 'login.html', context)

@csrf_exempt
def modify_index(request):
    # field
    cursor = connection.cursor()
    sql_field = '''
        select 
             field
        from 
            mltdc_tdb.mltdc_field as mf 
    '''
    cursor.execute(sql_field)
    all_data = cursor.fetchall()
    
    field_mapping = []
    for field in all_data:
        # for id, _field in field:
        field_mapping.append(field[0])
    print('------field_mapping: ', field_mapping)

    # project
    sql_project = '''
        select 
             project
        from 
            mltdc_tdb.mltdc_project as mp 
    '''
    cursor.execute(sql_project)
    all_data = cursor.fetchall()
    
    project_mapping = []
    for project in all_data:
        # for id, _project in project:
        project_mapping.append(project[0])
    print('------project_mapping: ', project_mapping)

    # methodology
    sql_methodology = '''
        select 
             methodology
        from 
            mltdc_tdb.mltdc_methodology as mm 
    '''
    cursor.execute(sql_methodology)
    all_data = cursor.fetchall()
    
    methodology_mapping = []
    for methodology in all_data:
        # for id, _methodology in methodology:
        methodology_mapping.append(methodology[0])
    print('------methodology_mapping: ', methodology_mapping)

    # Button_url = [
    #     'http://127.0.0.1:8000/mltdc/index/timeseries/',
    #     'http://127.0.0.1:8000/mltdc/index/decision/',
    #     'http://127.0.0.1:8000/mltdc/index/saving/'
    # ]

    # for i in range(len(field_mapping)-3):
    #     Button_url.append('#')

    context = {
        'title': 'MLTDC TDB-signup',
        # 'Button_url' : list(zip(Button_url, field_mapping)),
        'Field' : field_mapping,
        'Project' : project_mapping,
        'Methodology' : methodology_mapping
        }

    return render(request, 'modify.html', context)

@csrf_exempt
def paper_signup_index(request):

    # field
    cursor = connection.cursor()
    sql_field = '''
        select 
             field
        from 
            mltdc_tdb.mltdc_field as mf 
    '''
    cursor.execute(sql_field)
    all_data = cursor.fetchall()
    
    field_mapping = []
    for field in all_data:
        # for id, _field in field:
        field_mapping.append(field[0])
    print(field_mapping)

    # project
    sql_project = '''
        select 
             project
        from 
            mltdc_tdb.mltdc_project as mp 
    '''
    cursor.execute(sql_project)
    all_data = cursor.fetchall()
    
    project_mapping = []
    for project in all_data:
        # for id, _project in project:
        project_mapping.append(project[0])
    print(project_mapping)

    # methodology
    sql_methodology = '''
        select 
             methodology
        from 
            mltdc_tdb.mltdc_methodology as mm 
    '''
    cursor.execute(sql_methodology)
    all_data = cursor.fetchall()
    
    methodology_mapping = []
    for methodology in all_data:
        # for id, _methodology in methodology:
        methodology_mapping.append(methodology[0])
    print(methodology_mapping)

    # paper
    sql_paper = '''
        select 
             title
        from 
            mltdc_tdb.mltdc_paper as mp 
    '''
    cursor.execute(sql_paper)
    all_data = cursor.fetchall()
    
    paper_mapping = []
    for paper in all_data:
        # for id, _paper in paper:
        paper_mapping.append(paper[0])
    print(paper_mapping)

    # year
    year = list(map(lambda x: str(x), reversed(range(2000, 2023))))

    # button url mapping

    Button_url = [
        'http://127.0.0.1:8000/mltdc/index/timeseries/',
        'http://127.0.0.1:8000/mltdc/index/decision/',
        'http://127.0.0.1:8000/mltdc/index/saving/'
    ]

    for i in range(len(field_mapping)-3):
        Button_url.append('#')

    context = {
        'title': 'MLTDC TDB- paper signup', 
        'Year' : year,
        # 'OwnerID' : ownerid_mapping,
        'Field' : field_mapping,
        'Project' : project_mapping,
        'Methodology' : methodology_mapping,
        'Paper' : paper_mapping,
        'Button_url' : list(zip(Button_url, field_mapping))
    }

    return render(request, 'paper-signup.html', context)

@csrf_exempt
def implement_signup_index(request):
    # field
    cursor = connection.cursor()
    sql_field = '''
        select 
             field
        from 
            mltdc_tdb.mltdc_field as mf 
    '''
    cursor.execute(sql_field)
    all_data = cursor.fetchall()
    
    field_mapping = []
    for field in all_data:
        # for id, _field in field:
        field_mapping.append(field[0])
    print(field_mapping)

    # project
    sql_project = '''
        select 
             project
        from 
            mltdc_tdb.mltdc_project as mp 
    '''
    cursor.execute(sql_project)
    all_data = cursor.fetchall()
    
    project_mapping = []
    for project in all_data:
        # for id, _project in project:
        project_mapping.append(project[0])
    print(project_mapping)

    # paper
    sql_paper = '''
        select 
             title
        from 
            mltdc_tdb.mltdc_paper as mp 
    '''
    cursor.execute(sql_paper)
    all_data = cursor.fetchall()
    
    paper_mapping = []
    for paper in all_data:
        # for id, _paper in paper:
        paper_mapping.append(paper[0])
    print(paper_mapping)

    # button url mapping

    Button_url = [
        'http://127.0.0.1:8000/mltdc/index/timeseries/',
        'http://127.0.0.1:8000/mltdc/index/decision/',
        'http://127.0.0.1:8000/mltdc/index/saving/'
    ]

    for i in range(len(field_mapping)-3):
        Button_url.append('#')

    context = {
        'title': 'MLTDC TDB- implement signup', 
        # 'Year' : year,
        # 'OwnerID' : ownerid_mapping,
        'Field' : field_mapping,
        'Project' : project_mapping,
        # 'Methodology' : methodology_mapping,
        'Paper' : paper_mapping,
        'Button_url' : list(zip(Button_url, field_mapping))
    }

    return render(request, 'implement-signup.html', context)

@csrf_exempt
def permission_setting_index(request):
    # ownerid
    cursor = connection.cursor()
    sql_owner = '''
        select 
             ownerid
        from 
            mltdc_tdb.mltdc_owner
    '''
    cursor.execute(sql_owner)
    all_data = cursor.fetchall()
    
    owner_mapping = []
    for owner in all_data:
        # for id, _field in field:
        owner_mapping.append(owner[0])
    print(owner_mapping)
    context = {
        'title': 'MLTDC TDB- permission setting',
        'ownerid': owner_mapping
    }

    return render(request, 'permission-setting.html', context)

@csrf_exempt
def timeseries_index(request):
    # cursor = connection.cursor()
    # sql = '''
    #     select 
    #         ID, ov.OwnerID, Field, Year, Title, Author, Periodical, Conditions, Experiments, Conclusions,
    #         Advantages, Disadvantages, Keywords, Link, ov.Doi, od.OwnerID, Date, OwnerDo, DataSource,
    #         Resource, Environment, Runtime, Note
    #     from 
    #         mltdc_ownerreview as ov 
    #     inner join 
    #         mltdc_ownerdo as od 
    #     on 
    #         ov.Doi=od.Doi 
    #     where 
    #         Field='Time Series'
    # '''
    # cursor.execute(sql)
    # all_data = cursor.fetchall()

    # col = ['ID', 'OwnerID', 'Field', 'Year', 'Title', 'Author', 
    #     'Periodical', 'Conditions', 'Experiments', 'Conclusions', 'Advantages', 'Disadvantages', 'Keywords', 'Link',
    #     'Doi', 'Ownerdo_OwnerID', 'Date', 'OwnerDo', 'DataSource', 'Resource', 'Environment', 'Runtime', 'Note']
    # paper_data = {}
    # for paper in all_data:
    #     for i, c in enumerate(col):
    #         if (type(paper[i]) == str) & (str(paper[i]).find(";")!=-1):
    #             paper_data.setdefault(c, []).append(paper[i].split(';'))
    #         elif (type(paper[i]) == str) & (str(paper[i]).find(";")==-1):
    #             paper_data.setdefault(c, []).append(paper[i])

    #         if c=='Date':
    #             paper_data.setdefault(c, []).append(paper[i].strftime('%Y-%m-%d'))
    # print(paper_data)   
    # context = {
    #     'title': 'MLTDC TDB - Time Series',
    #     'results': paper_data,
    #     'OwnerID' : paper_data['OwnerID'],
    #     'Field' : paper_data['Field'],
    #     'Year' : paper_data['Year'],
    #     'Title' : paper_data['Title'],
    #     'Author' : paper_data['Author'],
    #     'Periodical' : paper_data['Periodical'],
    #     'Conditions' : paper_data['Conditions'],
    #     'Experiments' : paper_data['Experiments'],
    #     'Conclusions' : paper_data['Conclusions'],
    #     'Advantages' : paper_data['Advantages'],
    #     'Disadvantages' : paper_data['Disadvantages'],
    #     'Keywords' : paper_data['Keywords'],
    #     'Link' : paper_data['Link'],
    #     'Doi' : paper_data['Doi'],
    #     'Date' : paper_data['Date'],
    #     'Ownerdo_OwnerID' : paper_data['Ownerdo_OwnerID'],
    #     'OwnerDo' : paper_data['OwnerDo'],
    #     'DataSource' : paper_data['DataSource'],
    #     'Resource' : paper_data['Resource'],
    #     'Environment' : paper_data['Environment'],
    #     'Runtime' : paper_data['Runtime'],
    #     'Note' : paper_data['Note']
    #     }
    # print('-----', context)     
    # field
    cursor = connection.cursor()
    sql_field = '''
        select 
             field
        from 
            mltdc_tdb.mltdc_field as mf 
    '''
    cursor.execute(sql_field)
    all_data = cursor.fetchall()
    
    field_mapping = []
    for field in all_data:
        # for id, _field in field:
        field_mapping.append(field[0])
    print(field_mapping)

    Button_url = [
        'http://127.0.0.1:8000/mltdc/index/timeseries/',
        'http://127.0.0.1:8000/mltdc/index/decision/',
        'http://127.0.0.1:8000/mltdc/index/saving/'
    ]

    for i in range(len(field_mapping)-3):
        Button_url.append('#')
        
    sql_MLTDC_Join_Table = '''
        select 
            ownerid, year, periodical, title, author, abstract,
            conditions, conclusions, advantages, disadvantages,
            keywords, paperlink, githublink, project, method, 
            field, createtime, hitcount
        from 
            mltdc_tdb.mltdc_join_table as m 
        left join 
            mltdc_tdb.mltdc_paper as paper
        on 
            m.paperid = paper.paperid
        left join 
            mltdc_tdb.mltdc_field as field
        on 
            m.fieldid = field.fieldid
        left join
            mltdc_tdb.mltdc_project as project
        on
            m.projectid = project.projectid
        where 
            Field='Time Series'
        and
            m.methodologyid in (
                SELECT 
                    MIN(mltdc_tdb.mltdc_join_table.methodologyid) 
                FROM 
                    mltdc_tdb.mltdc_join_table 
                GROUP BY 
                    paperid
                )
    '''
    cursor.execute(sql_MLTDC_Join_Table)
    all_data = cursor.fetchall()
    # all_data = OwnerReview.objects.filter(Field__icontains='Time').values()
    print('heeee---', all_data)
    paper_link = []
    owner_id = []
    paper_name = []
    for paper in all_data:
        paper_link.append(paper[11])
        owner_id.append(paper[0])
        paper_name.append(paper[3])
  
    paper_data = []
    col = ['ownerid', 'year', 'periodical', 'title', 'author', 'abstract',
            'conditions', 'conclusions', 'advantages', 'disadvantages',
            'keywords', 'paperlink', 'githublink', 'project', 'method', 
            'field', 'createtime','hitcount']

    for paper in all_data:
        _paper_data = {}
        # paper_data.append(paper)
        for i, c in enumerate(col):
            print(i)
            print(c)
            if type(paper[i]) == str:
                if c=='method':
                    _paper_data[c] = eval(paper[i])
                # if value.find(';')!=-1:
                else:
                    _paper_data[c] = paper[i].split(';')
            else:
                if (c=='implementdate')|(c=='createtime'):
                    _paper_data[c] = [paper[i].strftime('%Y-%m-%d')]           
                # if type(paper[i]) == int:
                else:
                    _paper_data[c] = str(paper[i]).split(';')

            # if (c=='implementdate')|(c=='createtime'):
            #     _paper_data[c] = [paper[i].strftime('%Y-%m-%d')]

            
            print(_paper_data)
        paper_data.append(_paper_data)
    context = {
        'title': 'MLTDC TDB - Time Series',
        'results' : list(zip(list(range(len(paper_name))), paper_link, owner_id, paper_name, paper_data)),
        'distillation_index' : list(map(lambda x: x+1, [1,2,3,5,6,7,8,9,12,16,17])),
        'Button_url' : list(zip(Button_url, field_mapping))
        }
    print('-----', context)


    # paper_link = []
    # paper_doi = []
    # paper_name = []
    # for paper in all_data:
    #     paper_link.append(paper['Link'])
    #     paper_doi.append(paper['Doi'])
    #     paper_name.append(paper['Title'])
        
    # paper_data = []
    # for paper in all_data:
    #     # paper_data.append(paper)
    #     for key, value in paper.items():
    #         if type(value) == str:
    #             # if value.find(';')!=-1:
    #             paper[key] = value.split(';')
    #         else:
    #             paper[key] = value
    #     paper_data.append(paper)
    # context = {
    #     'title': 'MLTDC TDB - Time Series',
    #     'results' : list(zip(list(range(len(paper_doi))), paper_link, paper_doi, paper_name, paper_data))
    #     }

    # cursor = connection.cursor()
    # cursor.execute("select * from mltdc_ownerreview as ov inner join mltdc_ownerdo as od on ov.Doi=od.Doi")
    # zz = cursor.fetchall()
    # print("----", zz)
    # queryset = OwnerReview.objects.all().extra(tables=['mltdc_ownerdo'], where=['mltdc_ownerdo.Doi = mltdc_ownerreview.Doi']).values()
    # print(queryset)
    # context = {
    #     'title': 'MLTDC TDB - Time Series',
    #     'results' : all_data,
    #     'link' : all_data['Link'][0],
    #     'doi' : all_data['Doi'][0],
    #     'name' : all_data['Title'][0]
    #     }

    return render(request, 'timeseries-index.html', context)

@csrf_exempt
def decision_index(request):

    cursor = connection.cursor()
    sql_field = '''
        select 
             field
        from 
            mltdc_tdb.mltdc_field as mf 
    '''
    cursor.execute(sql_field)
    all_data = cursor.fetchall()
    
    field_mapping = []
    for field in all_data:
        # for id, _field in field:
        field_mapping.append(field[0])
    print(field_mapping)

    Button_url = [
        'http://127.0.0.1:8000/mltdc/index/timeseries/',
        'http://127.0.0.1:8000/mltdc/index/decision/',
        'http://127.0.0.1:8000/mltdc/index/saving/'
    ]

    for i in range(len(field_mapping)-3):
        Button_url.append('#')
        
    sql_MLTDC_Join_Table = '''
        select 
            ownerid, year, periodical, title, author, abstract,
            conditions, conclusions, advantages, disadvantages,
            keywords, paperlink, githublink, project, method, 
            field, createtime, hitcount
        from 
            mltdc_tdb.mltdc_join_table as m 
        left join 
            mltdc_tdb.mltdc_paper as paper
        on 
            m.paperid = paper.paperid
        left join 
            mltdc_tdb.mltdc_field as field
        on 
            m.fieldid = field.fieldid
        left join
            mltdc_tdb.mltdc_project as project
        on
            m.projectid = project.projectid
        where 
            Field='Decision Intelligence'
        and
            m.methodologyid in (
                SELECT 
                    MIN(mltdc_tdb.mltdc_join_table.methodologyid) 
                FROM 
                    mltdc_tdb.mltdc_join_table 
                GROUP BY 
                    paperid
                )
    '''
    cursor.execute(sql_MLTDC_Join_Table)
    all_data = cursor.fetchall()
    # all_data = OwnerReview.objects.filter(Field__icontains='Time').values()
    print('heeee---', all_data)
    paper_link = []
    owner_id = []
    paper_name = []
    for paper in all_data:
        paper_link.append(paper[11])
        owner_id.append(paper[0])
        paper_name.append(paper[3])
  
    paper_data = []
    col = ['ownerid', 'year', 'periodical', 'title', 'author', 'abstract',
            'conditions', 'conclusions', 'advantages', 'disadvantages',
            'keywords', 'paperlink', 'githublink', 'project', 'method', 
            'field', 'createtime','hitcount']

    for paper in all_data:
        _paper_data = {}
        # paper_data.append(paper)
        for i, c in enumerate(col):
            print(i)
            print(c)
            if type(paper[i]) == str:
                if c=='method':
                    _paper_data[c] = eval(paper[i])
                # if value.find(';')!=-1:
                else:
                    _paper_data[c] = paper[i].split(';')
            else:
                if (c=='implementdate')|(c=='createtime'):
                    _paper_data[c] = [paper[i].strftime('%Y-%m-%d')]           
                # if type(paper[i]) == int:
                else:
                    _paper_data[c] = str(paper[i]).split(';')

            # if (c=='implementdate')|(c=='createtime'):
            #     _paper_data[c] = [paper[i].strftime('%Y-%m-%d')]

            
            print(_paper_data)
        paper_data.append(_paper_data)
    context = {
        'title': 'MLTDC TDB - Decision',
        'results' : list(zip(list(range(len(paper_name))), paper_link, owner_id, paper_name, paper_data)),
        'distillation_index' : list(map(lambda x: x+1, [1,2,3,5,6,7,8,9,12,16,17])),
        'Button_url' : list(zip(Button_url, field_mapping))
        }
    print('-----', context)
    # all_data = OwnerReview.objects.filter(Field__icontains='Decision').values()

    # paper_link = []
    # paper_doi = []
    # paper_name = []
    # for paper in all_data:
    #     paper_link.append(paper['Link'])
    #     paper_doi.append(paper['Doi'])
    #     paper_name.append(paper['Title'])
        
    # paper_data = []
    # for paper in all_data:
    #     # paper_data.append(paper)
    #     for key, value in paper.items():
    #         if type(value) == str:
    #             # if value.find(';')!=-1:
    #             paper[key] = value.split(';')
    #         else:
    #             paper[key] = value
    #     paper_data.append(paper)
    # context = {
    #     'title': 'MLTDC TDB - Time Series',
    #     'results' : list(zip(list(range(len(paper_doi))), paper_link, paper_doi, paper_name, paper_data))
    #     }
    # print(list(context['results']))

    return render(request, 'decision-index.html', context)

@csrf_exempt
def saving_index(request):
    cursor = connection.cursor()
    sql_field = '''
        select 
             field
        from 
            mltdc_tdb.mltdc_field as mf 
    '''
    cursor.execute(sql_field)
    all_data = cursor.fetchall()
    
    field_mapping = []
    for field in all_data:
        # for id, _field in field:
        field_mapping.append(field[0])
    print(field_mapping)

    Button_url = [
        'http://127.0.0.1:8000/mltdc/index/timeseries/',
        'http://127.0.0.1:8000/mltdc/index/decision/',
        'http://127.0.0.1:8000/mltdc/index/saving/'
    ]

    for i in range(len(field_mapping)-3):
        Button_url.append('#')
        
    sql_MLTDC_Join_Table = '''
        select 
            ownerid, year, periodical, title, author, abstract,
            conditions, conclusions, advantages, disadvantages,
            keywords, paperlink, githublink, project, method, 
            field, createtime, hitcount
        from 
            mltdc_tdb.mltdc_join_table as m 
        left join 
            mltdc_tdb.mltdc_paper as paper
        on 
            m.paperid = paper.paperid
        left join 
            mltdc_tdb.mltdc_field as field
        on 
            m.fieldid = field.fieldid
        left join
            mltdc_tdb.mltdc_project as project
        on
            m.projectid = project.projectid
        where 
            Field='Energy Saving'
        and
            m.methodologyid in (
                SELECT 
                    MIN(mltdc_tdb.mltdc_join_table.methodologyid) 
                FROM 
                    mltdc_tdb.mltdc_join_table 
                GROUP BY 
                    paperid
                )
    '''
    cursor.execute(sql_MLTDC_Join_Table)
    all_data = cursor.fetchall()
    # all_data = OwnerReview.objects.filter(Field__icontains='Time').values()
    print('heeee---', all_data)
    paper_link = []
    owner_id = []
    paper_name = []
    for paper in all_data:
        paper_link.append(paper[11])
        owner_id.append(paper[0])
        paper_name.append(paper[3])
  
    paper_data = []
    col = ['ownerid', 'year', 'periodical', 'title', 'author', 'abstract',
            'conditions', 'conclusions', 'advantages', 'disadvantages',
            'keywords', 'paperlink', 'githublink', 'project', 'method', 
            'field', 'createtime','hitcount']

    for paper in all_data:
        _paper_data = {}
        # paper_data.append(paper)
        for i, c in enumerate(col):
            print(i)
            print(c)
            if type(paper[i]) == str:
                if c=='method':
                    _paper_data[c] = eval(paper[i])
                # if value.find(';')!=-1:
                else:
                    _paper_data[c] = paper[i].split(';')
            else:
                if (c=='implementdate')|(c=='createtime'):
                    _paper_data[c] = [paper[i].strftime('%Y-%m-%d')]           
                # if type(paper[i]) == int:
                else:
                    _paper_data[c] = str(paper[i]).split(';')

            # if (c=='implementdate')|(c=='createtime'):
            #     _paper_data[c] = [paper[i].strftime('%Y-%m-%d')]

            
            print(_paper_data)
        paper_data.append(_paper_data)
    context = {
        'title': 'MLTDC TDB - Saving',
        'results' : list(zip(list(range(len(paper_name))), paper_link, owner_id, paper_name, paper_data)),
        'distillation_index' : list(map(lambda x: x+1, [1,2,3,5,6,7,8,9,12,16,17])),
        'Button_url' : list(zip(Button_url, field_mapping))
        }
    print('-----', context)
    # all_data = OwnerReview.objects.filter(Field__icontains='Saving').values()

    # paper_link = []
    # paper_doi = []
    # paper_name = []
    # for paper in all_data:
    #     paper_link.append(paper['Link'])
    #     paper_doi.append(paper['Doi'])
    #     paper_name.append(paper['Title'])
        
    # paper_data = []
    # for paper in all_data:
    #     # paper_data.append(paper)
    #     for key, value in paper.items():
    #         if type(value) == str:
    #             # if value.find(';')!=-1:
    #             paper[key] = value.split(';')
    #         else:
    #             paper[key] = value
    #     paper_data.append(paper)
    # context = {
    #     'title': 'MLTDC TDB - Time Series',
    #     'results' : list(zip(list(range(len(paper_doi))), paper_link, paper_doi, paper_name, paper_data))
    #     }
    # print(list(context['results']))
    
    return render(request, 'saving-index.html', context)

@csrf_exempt 
def paper_add(request):
    if request.method == "POST":
        title = request.POST.get('Title', 'nothing')
        paperlink = request.POST.get('Paperlink', 'nothing')
        githublink= request.POST.get('Githublink', 'nothing')
        author= request.POST.get('Author', 'nothing')
        periodical= request.POST.get('Periodical', 'nothing')
        keywords = request.POST.get('Keywords', 'nothing')
        conditions= request.POST.get('Conditions', 'nothing')
        advantages= request.POST.get('Advantages', 'nothing')
        disadvantages = request.POST.get('Disadvantages', 'nothing')
        abstract= request.POST.get('Abstract', 'nothing')
        conclusions= request.POST.get('Conclusions', 'nothing')
        ownerid = request.POST.get('OwnerID', 'nothing')
        field = request.POST.get('Field', 'nothing')
        year = request.POST.get('Year', 'nothing')
        # project = request.POST.get('Project', 'nothing')
        # methodology = request.POST.get('Methodology', 'nothing')
        methodology = request.POST.getlist('Methodology', 'nothing')
        
        context={
            "status": "OK",
            'title' : title,
            'paperlink' : paperlink, 
            'githublink' : githublink, 
            'author' : author,
            'periodical' : periodical,
            'keywords' : keywords,
            'conclusions' : conclusions,
            'advantages' : advantages,
            'disadvantages' : disadvantages,
            'abstract' : abstract,
            'conclusions' : conclusions,
            'ownerid' : ownerid,
            'field' : field,
            'year' : year,
            # 'project' : project,
            'methodology' : methodology
        }
        # print(context)

        # # Paper
        # test = Paper(year = year,
        #             title = title,
        #             paperlink = paperlink, 
        #             githublink = githublink, 
        #             author = author,
        #             periodical = periodical,
        #             keywords = keywords,
        #             conditions = conditions,
        #             advantages = advantages,
        #             disadvantages = disadvantages,
        #             abstract = abstract,
        #             conclusions = conclusions,
        #             )
        # test.save()
                # Paper
        test = Paper(year = year,
                    title = title,
                    paperlink = paperlink, 
                    githublink = githublink, 
                    author = author,
                    periodical = periodical,
                    keywords = keywords,
                    conditions = conditions,
                    advantages = advantages,
                    disadvantages = disadvantages,
                    abstract = abstract,
                    conclusions = conclusions,
                    method = methodology
                    )
        test.save()
        # try:
        for _method in methodology:

            test_MLTDC_Join_Table = MLTDC_Join_Table(
                owner = Owner.objects.get(ownerid=ownerid),
                paper = Paper.objects.get(title = title, year=year),
                methodology = Methodology.objects.get(methodology = _method),
                field = Field.objects.get(field = field),
                # project = Project.objects.get(project = project),
                createtime = datetime.date.today(),
            )
            test_MLTDC_Join_Table.save()

        # except:

        #     # test = Paper.objects.get(title = title)
        #     # test.delete(title=title)

        #     context={
        #         "status": "fail",
        #         'title' : title,
        #         'paperlink' : paperlink, 
        #         'githublink' : githublink, 
        #         'author' : author,
        #         'periodical' : periodical,
        #         'keywords' : keywords,
        #         'conclusions' : conclusions,
        #         'advantages' : advantages,
        #         'disadvantages' : disadvantages,
        #         'abstract' : abstract,
        #         'conclusions' : conclusions,
        #         'ownerid' : ownerid,
        #         'field' : field,
        #         'year' : year,
        #         'project' : project,
        #         'methodology' : methodology
        #     }

        #     print(context)

    return JsonResponse(context)

@csrf_exempt 
def implement_add(request):
    if request.method == "POST":
        ownerid= request.POST.get('OwnerID', 'nothing')
        implementdate= request.POST.get('Implementdate', 'nothing')
        runtime= request.POST.get('Runtime', 'nothing')
        source = request.POST.get('Source', 'nothing')
        result = request.POST.get('Result', 'nothing')
        field = request.POST.get('Field', 'nothing')
        title= request.POST.get('Title', 'nothing')
        note= request.POST.get('Note', 'nothing')
        project = request.POST.get('Project', 'nothing')

        _title = title.split(",")
        for title in _title:
            # try:
            title = title.strip()
            context={
                "status": "OK",
                "ownerid" : ownerid, 
                "implementdate" : implementdate,
                "source" : source,
                "runtime" : runtime,
                "result" : result,
                "field" : field,
                "title" : title,
                "Note" : note,
                'project' : project
            }
            print(context)

            test = Implement_Join_Table( 
                        paper = Paper.objects.get(title = title),
                        owner = Owner.objects.get(ownerid = ownerid), 
                        field = Field.objects.get(field = field),
                        project = Project.objects.get(project = project),
                        implementdate = implementdate,
                        result = result,
                        runtime = runtime,
                        datasource = source,
                        note = note,
                        createtime = datetime.date.today())
            test.save()

        # except:
        #     context={
        #         "status": "fail",
        #         "ownerid" : ownerid, 
        #         "implementdate" : implementdate,
        #         "source" : source,
        #         "runtime" : runtime,
        #         "result" : result,
        #         "field" : field,
        #         "title" : title,
        #         "Note" : note
        #     }
        #     print(context)

    return JsonResponse(context)

@csrf_exempt 
def field_add(request):
    if request.method == "POST":
        field = request.POST.get('Field', 'nothing')
        if field != 'nothing':
            test = Field(field = field)
            test.save()
            
            context={
                "status": "OK",
                "Field" : field
            }
        else:
            context={
                "status": "fail",
                "Field" : field
            }
    
    return JsonResponse(context)

@csrf_exempt 
def project_add(request):
    if request.method == "POST":
        project = request.POST.get('Project', 'nothing')
        if (project != 'nothing') & (project != ''):
            test = Project(project = project)
            test.save()
            
            context={
                "status": "OK",
                "Field" : project
            }
        else:
            context={
                "status": "fail",
                "Field" : project
            }
    
    return JsonResponse(context)

@csrf_exempt 
def methodology_add(request):
    if request.method == "POST":
        methodology = request.POST.get('Methodology', 'nothing')
        if (methodology != 'nothing') & (methodology != ''):
            test = Methodology(methodology = methodology)
            test.save()
            
            context={
                "status": "OK",
                "Field" : methodology
            }
        else:
            context={
                "status": "fail",
                "Field" : methodology
            }
    
    return JsonResponse(context)

@csrf_exempt
def login(request):
    if request.method == "POST":
        # 取得輸入的帳密與轉跳網址
        account = request.POST.get('Account', 'nothing')
        password= request.POST.get('Password', 'nothing')
    
        # 取得個人基本資訊
        url = "http://autcpmoweb01.corpnet.auo.com/api/UACAccount/UACLogin"
        
        payload = json.dumps({
        "username": account,
        "password": password,
        })
        
        headers = {
        'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload).json()
        
        # 認證通過
        if response['rtnCode'] == 'Pass':
            owner_exist = Owner.objects.filter(ownerid = response['userid'])

            # 若資料已存在，更新內容
            if owner_exist.exists():
                test = Owner.objects.get(ownerid = response['userid'])
                # test.ownerid = response['userid']
                test.name = response['name']
                test.location = response['location']
                test.deptname = response['deptname']
                test.deptno = response['deptno']
                test.email = response['email']
                test.tel = response['tel']
                test.account = response['alias']
                test.save()

            # 若資料尚未存在，新增內容
            else:
                # test = Owner(ownerid = response['userid'], 
                #             name = response['name'], 
                #             location = response['location'],
                #             deptname = response['deptname'],
                #             deptno = response['deptno'],
                #             email = response['email'],
                #             tel = response['tel'],
                #             account = response['alias'])
                # test.save()
                test = Owner(ownerid = response['userid'], 
                            name = response['name'], 
                            location = response['location'],
                            deptname = response['deptname'],
                            deptno = response['deptno'],
                            email = response['email'],
                            tel = response['tel'],
                            account = response['alias'],
                            permission = "member")
                test.save()
            context = {
                'Status' : 'success',
                'ownerid' : response['userid'],
                'permission' : Owner.objects.get(ownerid = response['userid']).permission
            }

            return JsonResponse(context)

        # 認證失敗
        else:
            context = {
                'Status' : 'fail',
            }

            return JsonResponse(context)

@csrf_exempt
def permission_add(request):
    if request.method == "POST":

        ownerid = request.POST.get('Ownerid', 'nothing')
        permission= request.POST.get('permission', 'nothing')
        owner_exist = Owner.objects.filter(ownerid = ownerid)

        # 若資料已存在，更新內容
        if owner_exist.exists():
            test = Owner.objects.get(ownerid = ownerid)
            # test.ownerid = response['userid']
            test.permission = permission
            test.save()

            context = {
                'Status' : 'success',
                'permission' : Owner.objects.get(ownerid = ownerid).permission
            }
        else:
            context = {
                'Status' : 'fail'
            }
        
    return JsonResponse(context)

@csrf_exempt
def hitcount_add(request):
    if request.method == "POST":
        paperid = request.POST.get('Paperid', 'nothing')

        test = Paper.objects.get(paperid = paperid)
        print(test.hitcount)
        if test.hitcount is None:
            test.hitcount = 1
            test.save()
            
            context = {
                "status": "OK",
                "hitcount" : 1,
                'paperid' : test.title
            }

        else:
            test.hitcount = test.hitcount + 1
            test.save()

            context = {
                "status": "OK",
                "hitcount" : test.hitcount,
                'title' : test.title
            }
        # context = {
        #     "status": "OK",
        #     "hitcount" : 'all_data[0][0] + 1',
        #     'title' : title
        # }
    return JsonResponse(context)

@csrf_exempt
def search_add(request):
    if request.method == "POST":
        search_class = request.POST.getlist('Search_class', 'nothing')
        search = request.POST.getlist('Search', 'nothing')[0]
        cursor = connection.cursor()
        print(search_class)

        # query condition in each db
        OwnerID = 'nothing'
        paperid = 'nothing'
        methodologyid = 'nothing'
        fieldid = 'nothing'
        OwnerdoID = 'nothing'
        projectid = 'nothing'

        for _class in search_class:
            print(_class)
            if _class.find("OwnerID")!=-1:
                sql_OwnerID = f'''
                select 
                    ownerid
                from 
                   mltdc_tdb.mltdc_owner
                where
                    ownerid like '%{search}%'
                '''
                print('----------', sql_OwnerID)

                cursor.execute(sql_OwnerID)
                OwnerID = cursor.fetchall()
                OwnerID = OwnerID[0][0] if len(OwnerID)!=0 else 'nothing'

                print("~~~~~", OwnerID)

            elif _class.find("Title")!=-1:
                sql_Title = f'''
                select 
                    paperid
                from 
                    mltdc_tdb.mltdc_paper
                where
                    title like '%{search}%'
                '''
                print('----------', sql_Title)
                
                cursor.execute(sql_Title)
                _paperid = cursor.fetchall()
                paperid = _paperid[0][0] if len(_paperid)!=0 else 'nothing'
                
                print("~~~~~", paperid)

            elif _class.find("Methodology")!=-1:
                sql_Methodology = f'''
                select 
                    methodologyid
                from 
                    mltdc_tdb.mltdc_methodology
                where
                    methodology like '%{search}%'
                '''
                print('--------------------', sql_Methodology)
                
                cursor.execute(sql_Methodology)

                _methodologyid = cursor.fetchall()
                methodologyid = _methodologyid[0][0] if len(_methodologyid)!=0 else 'nothing'

                print("~~~~~", methodologyid)

            elif _class.find("Field")!=-1:
                sql_Field = f'''
                select 
                    fieldid
                from 
                    mltdc_tdb.mltdc_field
                where
                    field like '%{search}%'
                '''
                print('--------------------', sql_Field)
                
                cursor.execute(sql_Field)
                _fieldid = cursor.fetchall()
                fieldid = _fieldid[0][0] if len(_fieldid)!=0 else 'nothing'
                print("~~~~~", fieldid)

            elif _class.find("OwnerdoID")!=-1:
                sql_OwnerdoID = f'''
                select 
                    ownerid
                from 
                    mltdc_tdb.mltdc_owner
                where
                    ownerid like '%{search}%'
                '''
                print('----------', sql_OwnerdoID)

                cursor.execute(sql_OwnerdoID)
                OwnerdoID = cursor.fetchall()
                OwnerdoID = OwnerdoID[0][0] if len(OwnerdoID)!=0 else 'nothing'

                print("~~~~~", OwnerdoID)

            elif _class.find("Project")!=-1:
                sql_Project = f'''
                select 
                    projectid
                from 
                    mltdc_tdb.mltdc_project
                where
                    project like '%{search}%'
                '''
                print('----------', sql_Project)

                cursor.execute(sql_Project)
                projectid = cursor.fetchall()
                projectid = projectid[0][0] if len(projectid)!=0 else 'nothing'

                print("~~~~~", projectid)

        # get paperid which matched above condition
        sql = f'''
            (select
                paperid
            from
                mltdc_tdb.mltdc_join_table as m
            where
                ownerid = '{OwnerID}'
            or
                paperid = '{paperid}'
            or
                methodologyid = '{methodologyid}'
            or
                fieldid = '{fieldid}')
            union
                (select 
                    paperid 
                from 
                    mltdc_tdb.mltdc_implement_join_table as im
                where
                    ownerid = '{OwnerdoID}'
                or
                    projectid = '{projectid}'
                    )

        '''
        print('--------------------', sql)

        cursor.execute(sql)
        search_paper = cursor.fetchall()
        print(search_paper)
        # if len(search_paper)!=0:
        #     if len(search_paper[0])==1:
        #         paper = search_paper[0][0]
        #     else:
        #         paper = search_paper[0]
        # else:
        #     paper = 'nothing'

        if len(search_paper)==0:
            paper = 'nothing'
            info_sql = ""
            implement_sql = ""
        elif len(search_paper)==1:
            paper = search_paper[0][0]

            # get paper info.
            info_sql = f'''

            select
                m.paperid, title, year, field, ownerid, periodical, author, abstract,
                conditions, conclusions, advantages, disadvantages,
                keywords, paperlink, githublink, method, 
                createtime, hitcount
            from
                mltdc_tdb.mltdc_join_table as m
            left join 
                mltdc_tdb.mltdc_paper as paper
            on 
                m.paperid = paper.paperid
            left join 
                mltdc_tdb.mltdc_field as field
            on 
                m.fieldid = field.fieldid
            where
                m.paperid in ('{paper}')
            '''

            # get implement info. 
            implement_sql = f'''
            select 
                paperid, ownerid as ownerdoid, implementdate, result, runtime, datasource, note, project
            from
                mltdc_tdb.mltdc_implement_join_table as im
            left join
                mltdc_tdb.mltdc_project as project
            on
                im.projectid = project.projectid
            where
                paperid in ('{paper}')
            '''
        else:
            paper = tuple(map(lambda x: x[0], search_paper ))

            # get paper info.
            info_sql = f'''

            select
                m.paperid, title, year, field, ownerid, periodical, author, abstract,
                conditions, conclusions, advantages, disadvantages,
                keywords, paperlink, githublink, method, 
                createtime, hitcount
            from
                mltdc_tdb.mltdc_join_table as m
            left join 
                mltdc_tdb.mltdc_paper as paper
            on 
                m.paperid = paper.paperid
            left join 
                mltdc_tdb.mltdc_field as field
            on 
                m.fieldid = field.fieldid
            where
                m.paperid in {paper}
            '''

            # get implement info. 
            implement_sql = f'''
            select 
                paperid, ownerid as ownerdoid, implementdate, result, runtime, datasource, note, project
            from
                mltdc_tdb.mltdc_implement_join_table as im
            left join
                mltdc_tdb.mltdc_project as project
            on
                im.projectid = project.projectid
            where
                paperid in {paper}
            '''
        print("----------", paper)
        
        # # get paper info.
        # info_sql = f'''

        # select
        #     m.paperid, title, year, field, ownerid, periodical, author, abstract,
        #     conditions, conclusions, advantages, disadvantages,
        #     keywords, paperlink, githublink, method, 
        #     createtime, hitcount
        # from
        #     mltdc_tdb.mltdc_join_table as m
        # left join 
        #     mltdc_tdb.mltdc_paper as paper
        # on 
        #     m.paperid = paper.paperid
        # left join 
        #     mltdc_tdb.mltdc_field as field
        # on 
        #     m.fieldid = field.fieldid
        # where
        #     m.paperid in ('{paper}')
        # '''
        print("----------", info_sql)

        if info_sql=="":
            context = {
                "status": "No",
                'search_result' : "No"
            }
        else:
            cursor.execute(info_sql)
            paper_info = cursor.fetchall()
            print(paper_info)

            # # get implement info. 
            # implement_sql = f'''
            # select 
            #     paperid, ownerid as ownerdoid, implementdate, result, runtime, datasource, note, project
            # from
            #     mltdc_tdb.mltdc_implement_join_table as im
            # left join
            #     mltdc_tdb.mltdc_project as project
            # on
            #     im.projectid = project.projectid
            # where
            #     paperid in ('{paper}')
            # '''
            print("----------", implement_sql)

            cursor.execute(implement_sql)
            implement_info = cursor.fetchall()
            print(implement_info)

            outer_col = ['title', 'year', 'field']
            inner_paper_col = [
                'ownerid', 'periodical', 'author', 'abstract',
                'conditions', 'conclusions', 'advantages', 'disadvantages',
                'keywords', 'paperlink', 'githublink', 'method', 'createtime', 'hitcount'
            ]
            inner_implement_col = [
                'ownerdoid', 'implementdate', 'result', 'runtime', 'datasource', 'note', 'project'
            ]

            info_dict = {}
            for info in paper_info:
                info_dict[f'{info[0]}'] = [info[1:4], info[4:]]

                for implement in implement_info:
                    if implement[0]==info[0]:
                        info_dict[f'{info[0]}'].append(implement[1:])

                if len(info_dict[f'{info[0]}'])==2:
                    info_dict[f'{info[0]}'].append(['No Result.']*7)
            print(info_dict)



            context = {
                "status": "OK",
                'search_class' : search_class,
                'search' : search,
                'outer_col' : outer_col,
                'inner_paper_col' : inner_paper_col,
                'inner_implement_col' : inner_implement_col,
                'info_dict' : info_dict
            }
            # print(context)
    # context = {
    #             "status": "OK"
    #         }
    return JsonResponse(context)

@csrf_exempt
def field_modify(request):
    if request.method == "POST":

        oldname = request.POST.get('name', 'nothing')
        newname = request.POST.get('data', 'nothing')
        print(oldname)
        if (oldname=="...")|(oldname==""):

            test = Field(field = newname)
            test.save()
            
            context={
                "status": "OK",
                "Field" : newname
            }
        elif oldname!="...":

            test = Field.objects.get(field = oldname)
            test.field = newname
            test.save()

            context = {
                'status' : 'OK',
                'oldname' : oldname,
                'newname' : newname
            }
        else:
            context={
                "status": "fail",
                'oldname' : oldname,
                'newname' : newname
            }

        print(context)
    return JsonResponse(context)

@csrf_exempt
def project_modify(request):
    if request.method == "POST":

        oldname = request.POST.get('name', 'nothing')
        newname = request.POST.get('data', 'nothing')

        if (oldname=="...")|(oldname==""):

            test = Project(project = newname)
            test.save()
            
            context={
                "status": "OK",
                "project" : newname
            }
        elif oldname!="...":

            test = Project.objects.get(project = oldname)
            test.project = newname
            test.save()

            context = {
                'status' : 'OK',
                'oldname' : oldname,
                'newname' : newname
            }
        else:
            context={
                "status": "fail",
                'oldname' : oldname,
                'newname' : newname
            }

        print(context)
    return JsonResponse(context)

@csrf_exempt
def methodology_modify(request):
    if request.method == "POST":

        oldname = request.POST.get('name', 'nothing')
        newname = request.POST.get('data', 'nothing')

        if (oldname=="...")|(oldname==""):

            test = Methodology(methodology = newname)
            test.save()
            
            context={
                "status": "OK",
                "methodology" : newname
            }
        elif oldname!="...":

            test = Methodology.objects.get(methodology = oldname)
            test.methodology = newname
            test.save()

            context = {
                'status' : 'OK',
                'oldname' : oldname,
                'newname' : newname
            }
        else:
            context={
                "status": "fail",
                'oldname' : oldname,
                'newname' : newname
            }

        print(context)
    return JsonResponse(context)

@csrf_exempt
def signup(request):
    cursor = connection.cursor()
    sql = '''
        select 
            * 
        from 
            mltdc_field as mf 
    '''
    cursor.execute(sql)
    all_data = cursor.fetchall()

    field_mapping = {}
    for fields in all_data:
        for id, field in fields:
            field_mapping[str(id)] = field
    
    context = {
        'Field' : field_mapping
    }
    return render(request, 'index.html', context)

@csrf_exempt  
def field_delete(request):
    if request.method == "POST":

        oldname = request.POST.get('name', 'nothing')
        # newname = request.POST.get('data', 'nothing')
        print(oldname)
        if oldname=="...":
            
            context={
                "status": "OK",
                "Field" : "No Data, do nothing"
            }
        elif oldname!="...":

            test = Field.objects.get(field = oldname)
            test.delete()

            context = {
                'status' : 'OK',
                'Field' : f'delet {oldname}'
            }
        else:
            context={
                "status": "fail",
                'oldname' : oldname
            }
        print(context)
    return JsonResponse(context)

@csrf_exempt  
def project_delete(request):
    if request.method == "POST":

        oldname = request.POST.get('name', 'nothing')
        # newname = request.POST.get('data', 'nothing')
        print("-------------", oldname, "----------------------")
        if oldname=="...":
            
            context={
                "status": "OK",
                "Field" : "No Data, do nothing"
            }
        elif oldname!="...":
            print('---------------im here elif---------------')
            test = Project.objects.get(project = oldname)
            

            print("---", test)
            test.delete()

            context = {
                'status' : 'OK',
                'Project' : f'delet {oldname}'
            }
        else:
            context={
                "status": "fail",
                'oldname' : oldname
            }
        print(context)
    return JsonResponse(context)

@csrf_exempt  
def methodology_delete(request):
    if request.method == "POST":

        oldname = request.POST.get('name', 'nothing')
        # newname = request.POST.get('data', 'nothing')
        
        if oldname=="...":
            
            context={
                "status": "OK",
                "Field" : "No Data, do nothing"
            }
        elif oldname!="...":

            test = Methodology.objects.get(methodology = oldname)
            test.delete()

            context = {
                'status' : 'OK',
                'Methodology' : f'delet {oldname}'
            }
        else:
            context={
                "status": "fail",
                'oldname' : oldname
            }
        print(context)
    return JsonResponse(context)

@csrf_exempt
def star_add(request):
    if request.method == "POST":
        star = request.POST.get('Star', 'nothing')
        paperid = request.POST.get('Paperid', 'nothing')
        ownerid = request.POST.get('Ownerid', 'nothing')

        star_exist = Evaluation.objects.filter(Q(paper = paperid) & Q(owner = ownerid))
        print(star_exist)
        if star_exist.exists():
            test = Evaluation.objects.get(Q(paper = paperid) & Q(owner = ownerid))
            test.star = star
            test.save()

        else:
            test = Evaluation(owner = Owner.objects.get(ownerid = ownerid), 
                              paper = Paper.objects.get(paperid = paperid), 
                              star = star)
            test.save()
        
        context = {
            'status' : 'OK',
            'star': star,
            'paperid': paperid,
            'ownerid': ownerid
        }
    return JsonResponse(context)