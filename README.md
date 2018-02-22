# Ближайшие бары

Скрипт bars.py используя слепок данных [data.mos.ru](data.mos.ru) (data.json) расчитывает
⋅⋅*самый большой бар;
⋅⋅*самый маленький бар;
⋅⋅*самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры).

Например, если ввести коодинаты 55.740575, 37.616892 найдет заведение "red code bar"

# Problems

I used min/max functions to find smallest/biggest bar. Not sure, what means - "самый большой бар", what function needs to search - seats count, bar area or something else. And what function needs to return: size of bar, name, coordinates or just dictionary  from json, containing all those properties.  Conditions of task are blurry, so they would be misinterpreted.

And I haven't found, how to use min/max functions, to get index of dictionary in list, not just value. Not sure if it possible at all.


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# FIXME вывести пример ответа скрипта

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
