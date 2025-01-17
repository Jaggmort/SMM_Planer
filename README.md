# SMM Planer

Данный репозитарий представляет собой набор скрипт, который позволяет реализовать планирование и автоматическую рассылку постов в различных соц. сетях.
На данный момемент поодерживются соц-сети:
- VK
- Telegram
- Однокласники
### Как установить

Перед установкой создайте файл **.env** вида:
```
CALLENAR_ID ='ИД вашего календаря'
SPREADSHEET_ID='ИД вашей таблицы для планирования'
VK_IMPLICIT_FLOW_TOKEN=<ваш токен>
VK_GROUP_ID=<ID  группы куда будут выкладывать записи>
TELEGA_KEY='<Ваш токен от телеграмма>'
TG_CHAT_ID='<ID вашего чата>'
OK_SESSION = 'Секретный ключ сессии одноклассников'
OK_PUBLIC_KEY = 'Публичный ключ приложения в одноклассниках'
OK_ACCESS_TOKEN = 'Вечный токен доступа одноклассников'
OK_GROUP_ID = 'ID  группы куда будут выкладывать записи в одноклассниках'
```

- Для получения ID google sheet из URL  можете воспользоваться встроенной функцией
`get_id_from_url`

- Для получения токена для работы с VK  воспользуйтесь документацией которая находится по ссылке
https://dev.vk.com/api/access-token/implicit-flow-user  
так же можете перейти по ссылке указав соотвесвующий client_id
VK_TEST_URL='https://oauth.vk.com/authorize?client_id={}&display=page&scope=photos,groups,wall,offline&response_type=token'

- Для того что бы узнать VK ID  группы, в которой вы собираетесь постить фото вы можете воспользоваться сервисом 
https://regvk.com/id/

- Для получения токена для работы с OK  воспользуйтесь документацией которая находится по ссылке
https://apiok.ru/ext/oauth/ 

- Для того что бы узнать OK ID  группы, в которой вы собираетесь постить фото достаточно открыть группу и скопировать адрес:
https://ok.ru/group/id , где вместо id - будет номер группы

- Так же необходимо положить в основную директорию файл `credential.json`
Вы можете его сгенерировать на странице https://console.cloud.google.com/apis/credential

- Токен для Телеграм бота вы можете получить https://telegram.me/BotFather Чат ID можно узнать в свойствах канала.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Описание функций

- `add_event` - добавляет событие в календарь
- `get_credentials` - необходима для авторизации запросов
- `get_sheet` - чтение диапазона ячеек из google sheets
- `write_cells` - запись в диапазон ячеек
- `read_paragraph_element` - вспомогательная вункция чтения элемента
- `read_docs` извлечение текста из google docs
- `get_id_from_url` извлечение id из url


### Пример запуска

Ниже представлен пример запуска скрипта.

```
SMM_Planer> python .\google_tools.py  
```
### Пример работы
```
Данный раздел будет написан позже
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).