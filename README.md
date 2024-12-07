![](./Screenshot%20from%202024-12-07%2012-58-31.png)

Описание проблемы
- Создание HTTP-запроса:
Пользователь может сформировать HTTP-запрос, содержащий вредоносное содержимое. Это может привести к различным уязвимостям, если сервер не проверяет входящие данные.
- Присвоение вредоносного значения переменной '$id':
Вредоносное значение может быть присвоено переменной '$id'. Это значение может содержать код или данные, которые могут быть использованы для атаки на систему.
- Конкатенация строк:
Вредоносное содержимое конкатенируется в строку. Этот процесс может привести к тому, что вредоносный код будет включен в новую строку.
- Присвоение вредоносного значения переменной $id 
 '$id'. Это значение также может содержать потенциально опасные данные.
- Небезопасный вызов:
Вызов, который использует переменную с вредоносным значением, является небезопасным. Вредоносное значение может быть использовано в качестве аргумента.


## Исправленный код находится в source_correct.php
Объяснение изменений:
- Подготовленные выражения: Используется метод prepare() для создания подготовленного выражения, что предотвращает SQL-инъекции.
- Привязка параметров: Метод bind_param() используется для привязки переменной $id к запросу. Это гарантирует, что значение будет обработано как целое число (или другой тип, если необходимо).
- Закрытие ресурсов: Закрываются подготовленный запрос и соединение с базой данных после выполнения.


## Использование улитилиты sqlmap на уязвимый к SQL Injection на страницу с кодом source.php, полный вывод в файле sqlmap_result.txt

![](./Screenshot%20from%202024-12-07%2014-56-07.png)
