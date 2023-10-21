# Документация API

## Эндпоинт Заметок

### Создать новую Заметку

- **URL**: `/api/v1/notes/`
- **Method**: `POST`

#### Request
```json
{
  "title": "Note Title",
  "content": "Note Content"
}


#### Response
```json

{
  "id": 1,
  "title": "Note Title",
  "content": "Note Content"
}

### Получить список Заметок


- **URL**: /api/notes/

- **Method**: `GET`

#### Response
```json
[
  {
    "id": 1,
    "title": "Note 1",
    "content": "Content 1"
  },
  {
    "id": 2,
    "title": "Note 2",
    "content": "Content 2"
  },
  ...
]


### Получить Детали Заметки


- **URL**: `/api/notes/{id}/`

- **Method**: `GET`

#### Response
```json
{
  "id": 1,
  "title": "Note Title",
  "content": "Note Content"
}


### Обновить Заметку


- **URL**: `/api/notes/{id}/`

- **Method**: `PUT`

#### Request
```json
{
  "title": "Updated Note Title",
  "content": "Updated Note Content"
}

#### Response
```json
{
  "id": 1,
  "title": "Updated Note Title",
  "content": "Updated Note Content"
}



### Удалить Заметку


- **URL**: `/api/notes/{id}/`

- **Method**: `DELETE`

#### Response
```css
HTTP 204 No Content




### Поиск Заметок


- **URL**: `/api/notes/search/`

- **Method**: `GET`

#### Request
`/api/notes/search/?query=keyword`

#### Response
```json
[
  {
    "id": 1,
    "title": "Note with Keyword",
    "content": "Note Content"
  },
  ...
]



## Использование API
API позволяет пользователям выполнять операции CRUD (Создать, Прочитать, Обновить, Удалить) для заметок. Кроме того, пользователи могут искать заметки по ключевым словам.

### Создание новой Заметки
Чтобы создать новую заметку, отправьте POST запрос на эндпоинт /api/notes/ с параметрами title и content в теле запроса.


Пример запроса:
- **URL**: `/api/v1/notes/`
- **Method**: `POST`
```json
{
  "title": "New Note",
  "content": "This is a new note."
}

####Response
```json

{
  "id": 1,
  "title": "Note Title",
  "content": "Note Content"
}


### Получение списка Заметок
Чтобы получить список всех заметок, выполните GET запрос на эндпоинт `/api/notes/`.


### Получение Деталей Заметки
Чтобы получить детали конкретной заметки, выполните GET запрос на эндпоинт `/api/notes/{id}/`, заменив {id} на идентификатор заметки.

### Обновление Заметки
Чтобы обновить детали заметки, отправьте PUT запрос на эндпоинт `/api/notes/{id}/`, заменив `{id}` на идентификатор заметки. Включите обновленные параметры `title` и `content` в теле запроса.

Пример запроса:
```json
{
  "title": "Updated Note",
  "content": "This is the updated content."
}



### Удаление Заметки
Чтобы удалить заметку, отправьте DELETE запрос на эндпоинт `/api/notes/{id}/`, заменив `{id}` на идентификатор заметки.
### Поиск Заметок
Чтобы найти заметки, содержащие определенное ключевое слово, выполните GET запрос на эндпоинт `/api/notes/search/` с параметром `query` в строке запроса.

Пример запроса: `/api/notes/search/?query=ключевое+слово`
Это вернет список заметок, содержащих указанное ключевое слово.




