import pprint
import re
from pprint import pprint
import csv
with open("phonebook_raw.txt", 'r', encoding='utf8') as f:
    a = csv.reader(f, delimiter=",")
    contacts_list = list(a)
# pprint(contacts_list)

text = ""

for row in contacts_list:
    for word in row:
        text += word
        text += ","



#Приведём номер и добаочный номер к нужному виду:
pattern_number = r'(\+7|8)\s?\(?(\d{3,3})\)?[\s-]?(\d{3,3})[\s-]?(\d{2,2})[\s-]?(\d{2,2})'
phone_number = re.findall(pattern_number, text)
substition_number = r'+7(\2)\3-\4-\5'
new_text_number1 = re.sub(pattern_number, substition_number, text)
print(phone_number)

pattern_adds_number = r'\(?доб.\s(\d*)\)?'
add_phone_nuber = re.findall(pattern_adds_number, text)

substition_add_number = r' доб.\1'
new_text1 = re.sub(pattern_adds_number, substition_add_number, new_text_number1)

#Приведём Имена и профессии к нужному виду:

pattern_name = r'([А-Я][а-я]+)[\s,]+([А-Я][а-я]+)[\s,]+([А-Я][а-я]+)'
substition_name = r'\1 \2 \3'
name = re.findall(pattern_name, new_text1)
new_text2 = re.sub(pattern_name, substition_name, new_text1)

#Объединим дублируемые записи
pattern_duble1 = r'(Мартиняхин Виталий Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий)(,+)'
double1 = re.findall(pattern_duble1, new_text2)
substition_duble1 = r'\1 +7(495)913-00-37,'
new_text3 = re.sub(pattern_duble1, substition_duble1, new_text2)

pattern_duble2 = r'(Лагунцов Иван Алексеевич),+(Минфин,+)(\+7\(495\)913-11-11)\s(доб\.0792)()'
substition_duble2 = r'\1\2\3\4\5, Ivan.Laguntcov@minfin.ru'
double2 = re.findall(pattern_duble2, new_text3)
new_text4 = re.sub(pattern_duble2, substition_duble2, new_text3)

new_text4 = new_text4.replace(',,,', ',').replace(',,', ',')

pattern_del_str1 = r'(Лагунцов Иван,Ivan.Laguntcov@minfin.ru,)'
substition_del1 = " "
str1 = re.findall(pattern_del_str1, new_text4)
new_text5 = re.sub(pattern_del_str1, substition_del1, new_text4)

pattern_del_str2 = r'(Мартиняхин Виталий Геннадьевич,ФНС,\+7\(495\)913-00-37)'
substition_del2 = ""
str2 = re.findall(pattern_del_str2, new_text5)
new_text6 = re.sub(pattern_del_str2, substition_del2, new_text5)
new_text6 = new_text6.replace(', ', '').replace(',,', ', ').replace(',', ', ')
pprint(new_text6)

