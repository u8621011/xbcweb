# Genereate Translation file.
1. python -m django-admin makemessages -l en
2. modify the encoding method of open to utf8
src: https://sites.google.com/site/zhoubx/computer/django
with open(django_po, 'rU', encoding='utf8') as fp:
3. modify system default encoding (not workable in python3)
http://stackoverflow.com/questions/492483/setting-the-correct-encoding-when-piping-stdout-in-python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')