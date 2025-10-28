
# Db manager

Python with library Qt


### Envirement

```bash
# create env/ install packages
. ./console install
# Enter
. ./console env
# Exit
. ./console exit
```

### Export packages

```
./console freeze
```

### Run Qt designer

GUI User editor

```
./console designer
```


### Migracje

```
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```

