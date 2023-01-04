from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def ind(x, key, href):
    if href:
        return "#" + str(x) + str(key)
    else:
        return str(x) + str(key)

@register.simple_tag
def ind_clickall(x, href):
    if href:
        return "#" + "clickall" + str(x)
    else:
        return "clickall" + str(x)

@register.simple_tag
def ind_distillation(x, href):
    if href:
        return "#" + "distillation" + str(x)
    else:
        return "distillation" + str(x)

@register.simple_tag
def tips_mapping(x):
    tips_dict = {
        'ownerid': '閱讀者工號',
        'year': '發表年份',
        'periodical': '刊登期刊',
        'title': '論文名稱',
        'author': '第一作者',
        'abstract': '論文摘要',
        'conditions': '方法使用條件',
        'conclusions': '結論',
        'advantages': '方法優點',
        'disadvantages': '方法缺點',
        'keywords': '關鍵字',
        'paperlink': '論文連結',
        'githublink': '論文github',
        'project': '應用專案',
        'methodology': '相關方法',
        'method': '相關方法',
        'field': '論文領域',
        'createtime' : '上傳時間',
        'hitcount': '點擊次數',
    }

    return tips_dict[x]
    # if type(sentence) == str:
    #     _sentence = sentence.split(';')
    # else:
    #     _sentence = sentence

    # return _sentence

# @register.simple_tag
# def my_input(v1, v2):
#     temp_html = '''
#     <dev class='input-group mb-3'>
#     <span class='input-group-text' id="%s">@</span>
#     <input type='text' class='form-control' placeholder='%s' aria-label='Username'>
#     </dev>
#     '''%(v1, v2)

#     return mark_safe(temp_html)

# @register.filter
# def my_filter(v1, v2):
#     return v1*v2
