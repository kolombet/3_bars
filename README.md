# Ближайшие бары

Скрипт bars.py используя слепок данных [data.mos.ru](data.mos.ru) расчитывает
- Самый большой бар
- Самый маленький бар
- Самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры).

Например, если ввести коодинаты 55.740575, 37.616892 найдет заведение "red code bar"

# Как использовать скрипт

При запуске скрипта
- В слепке данных ищутся бары с минимальным/максимальным количеством мест, и названия соответсвующих баров и количество мест в них, выводятся в консоль.
- У пользователя запрашивается долгота/широта, и по этим данным в слепке ищется бар, ближайший к этим координатам, пользователю возвращается название бара и координаты

# Как запустить
 
Для работы программы JSON файл необходим, требуется:
1. Зарегистрироваться на сайте [data.mos.ru](data.mos.ru)
2. Получить ключ api в личном кабинете
3. Скачать файл через rest api, по ссылке https://apidata.mos.ru/v1/features/1796?api_key={api_key}. 
4. Назвать его bars.json и положить его в директорию с скриптом bars.py

По умолчанию скрипт ищет в директории файл bars.json, однако можно указать файл в ручную с помощью параметра -file или --f

```

$ python3 ./bars.py --f custom.json
using bars file: custom.json

```

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python3 ./bars.py
using bars file: bars.json
smallest bar name: Сушистор seats count: 0
biggest bar name: Спорт бар «Красная машина» seats count: 450
please input your coordinates to get nearest bar name
enter longitude:
55.863474
enter latitude:
37.605457
closest bar: ПИВНОЙ РАЙ(55.860711275878366 37.61269351269725)

```

Запуск на Windows происходит аналогично.



# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
