from dataclasses import field
from django.db import models

# Create your models here.
class Owner(models.Model):
    ownerid = models.IntegerField(primary_key=True, null=False, help_text='輸入工號')
    name = models.CharField(max_length=100, null=False, help_text='輸入中文名')
    location = models.CharField(max_length=100, null=False, help_text='輸入廠區代號')
    deptname = models.CharField(max_length=100, null=False, help_text='輸入中文部門')
    deptno = models.CharField(max_length=100, null=False, help_text='輸入部門代號')
    email = models.EmailField(max_length=100, null=False, help_text='輸入公司信箱')
    tel = models.CharField(max_length=100, null=False, help_text='輸入桌機電話號碼')
    account = models.CharField(max_length=100, null=False, help_text='輸入NT帳號')
    permission = models.CharField(max_length=100, null=False, help_text='輸入member/RD/admin')
    # rtnCode = models.CharField(max_length=10, null=False, help_text='輸入認證通過碼')

class Paper(models.Model):
    paperid = models.AutoField(primary_key=True)
    year = models.CharField(max_length=4, null=False, help_text='輸入論文年份')
    title = models.TextField(null=False, help_text='輸入論文標題')
    author = models.CharField(max_length=20, null=False, help_text='輸入論文第一作者')
    periodical = models.CharField(max_length=20, null=False, help_text='輸入論文的刊登期刊')
    conditions = models.TextField(null=False, help_text='輸入論文方法的使用條件')
    abstract = models.TextField(null=False, help_text='輸入論文摘要')
    conclusions = models.TextField(null=False, help_text='輸入論文結論')
    advantages = models.TextField(null=False, help_text='輸入論文方法的優點')
    disadvantages = models.TextField(null=False, help_text='輸入論文方法的缺點')
    keywords = models.TextField(null=True, help_text='輸入論文英文關鍵字')
    paperlink = models.TextField(null=False, help_text='輸入論文pdf檔案連結')
    githublink = models.TextField(null=True, help_text='輸入論文pdf檔案連結')
    method = models.TextField(null=False, help_text='輸入論文使用的方法')
    hitcount = models.IntegerField(null=True, help_text='輸入論文的點擊次數')

class Field(models.Model):
    fieldid = models.AutoField(primary_key=True)
    field = models.CharField(max_length=100, null=False, help_text='輸入論文相關領域')

class Project(models.Model):
    projectid = models.AutoField(primary_key=True)
    project = models.CharField(max_length=100, null=False, help_text='輸入論文有應用到的專案')

class Methodology(models.Model):
    methodologyid = models.AutoField(primary_key=True)
    methodology = models.CharField(max_length=100, null=False, help_text='輸入論文有應用到的方法')

class MLTDC_Join_Table(models.Model):
    mltdcid = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column='ownerid')
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, db_column='paperid')
    methodology = models.ForeignKey(Methodology, on_delete=models.CASCADE, db_column='methodologyid')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, db_column='fieldid')
    # project = models.ForeignKey(Project, on_delete=models.CASCADE, db_column='projectid')
    createtime = models.DateField(null=False, help_text='輸入登打日期')
    
    class Meta:
        db_table='mltdc_join_table' 

class Implement_Join_Table(models.Model):
    implementid = models.AutoField(primary_key=True)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, db_column='paperid')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column='ownerid')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, db_column='fieldid')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, db_column='projectid')
    implementdate = models.DateField(null=False, help_text='輸入開始實作的日期')
    result = models.TextField(null=False, help_text='輸入你實作的結果')
    runtime = models.FloatField(null=False, help_text='輸入你運行的時間(hr)')
    datasource = models.TextField(null=False, help_text='輸入你實作的資料與程式碼連結')
    note = models.TextField(null=True, help_text='輸入任何補充事項')
    createtime = models.DateField(null=False, help_text='輸入登打日期')

class Evaluation(models.Model):
    starid = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column='ownerid')
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, db_column='paperid')
    star = models.IntegerField(null=False, help_text='輸入開始實作的日期')

# class Test(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField(default=0)
#     sex = models.IntegerField(default=0)

# class Owner(models.Model):
#     OwnerID = models.CharField(primary_key=True, max_length=10, null=False, help_text='輸入工號')
#     EName = models.CharField(max_length=10, null=False, help_text='輸入英文名')
#     CName = models.CharField(max_length=10, null=False, help_text='輸入中文名')
#     Email = models.EmailField(max_length=20, null=False, help_text='輸入公司信箱')
#     Account = models.CharField(max_length=50, null=False, help_text='輸入帳號')
#     Password = models.CharField(max_length=50, null=False, help_text='輸入密碼')

# class OwnerReview(models.Model):
#     ID = models.AutoField(primary_key=True)
#     OwnerID = models.CharField(max_length=10, null=False, help_text='輸入工號')
#     Field = models.CharField(max_length=20, null=False, help_text='輸入相關領域')
#     Year = models.CharField(max_length=4, null=False, help_text='輸入年份')
#     Title = models.TextField(null=False, help_text='輸入論文名稱')
#     Author = models.CharField(max_length=20, null=False, help_text='輸入第一作者')
#     Periodical = models.CharField(max_length=20, null=False, help_text='輸入刊登期刊')
#     Conditions = models.TextField(null=False, help_text='輸入方法使用條件')
#     Experiments = models.TextField(null=False, help_text='輸入實驗結果')
#     Conclusions = models.TextField(null=False, help_text='輸入結論')
#     Advantages = models.TextField(null=False, help_text='輸入方法優點')
#     Disadvantages = models.TextField(null=False, help_text='輸入方法缺點')
#     Keywords = models.TextField(null=False, help_text='輸入英文關鍵字')
#     Link = models.TextField(null=False, help_text='輸入論文連結')
#     Doi = models.CharField(max_length=100, null=False, help_text='輸入論文doi')
#     # OwnerID = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column='OwnerID')

# class Technology(models.Model):
#     ID = models.AutoField(primary_key=True)
#     Project = models.CharField(max_length=10, null=False, help_text='輸入專案名稱')
#     Method = models.CharField(max_length=10, null=False, help_text='輸入有用到的方法')
#     Field = models.CharField(max_length=20, null=False, help_text='輸入相關領域')

# class OwnerDo(models.Model):
#     Doi = models.CharField(primary_key=True, max_length=100, null=False, help_text='輸入論文doi')
#     OwnerID = models.CharField(max_length=10, null=False, help_text='輸入工號')
#     Date = models.DateField(null=False, help_text='輸入閱讀日期')
#     OwnerDo = models.TextField(null=True, help_text='輸入實作結果')
#     DataSource = models.TextField(null=True, help_text='輸入實作資料路徑')
#     Resource = models.CharField(max_length=20, null=True, help_text='輸入所需規格')
#     Environment = models.CharField(max_length=10, null=True, help_text='輸入實作環境')
#     Runtime = models.CharField(max_length=10, null=True, help_text='輸入實作運行時間')
#     Note = models.TextField(null=True, help_text='輸入其他注意事項')
    # ownerreview = models.ForeignKey('OwnerReview', on_delete=models.CASCADE, related_name='OwnerDo_to_OwnerReview')


    # OwnerID = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column='OwnerID')
# class DoiMapping(models.Model):
#     Doi = models.CharField(primary_key=True, max_length=100, help_text='輸入論文doi')
#     OwnerID = models.CharField(max_length=10, null=False, help_text='輸入工號')
