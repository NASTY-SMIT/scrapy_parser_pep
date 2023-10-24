# Асинхронный парсер PEP

## Функционал

#### Сбор актуальной информации о статусах PEP

### Используемые технологии
- Python 3.9
- Scrapy 2.5.1

## Как запустить проект

Клонировать репозиторий:
```
git clone git@github.com:NASTY-SMIT/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Создать и активировать виртуальное окружение:
Linux: 
```
python3 -m venv env
source venv/bin/activate
```
Windows: 
```
python -m venv env
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
## Как работать с парсером - запустить паука

```
scrapy crawl pep
```

## Результат работы:
Парсер выводит собранную информацию в два файла .csv:
- В первый файл выводится список всех PEP: номер, название и статус.
- Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла в колонке «Статус» стоит слово Total, а в колонке «Количество» — общее количество всех документов.

Автор [Nasty Shmidt](https://github.com/NASTY-SMIT)
[Telegram](https://t.me/nastyShmidt)