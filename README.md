# LuffyCtiy

---
当前环境   环境安装导出模块
``` bash
pip freeze > requirements.txt 
项项目环境  安装
pip install -r requirements.txt
```

---
```
Path Intellisense
topper
Bracket Pair Colorizer
```

数据库初始化
```
python3 manage.py  makemigrations 
python3 manage.py migrate
```
上线提示 
```sql
    class Meta:
        verbose_name = "10-评价表"
        db_table = verbose_name  #上线 禁止使用db_table 
        verbose_name_plural = verbose_name

```