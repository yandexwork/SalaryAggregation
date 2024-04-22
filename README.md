# Агрегатор зарплат

Телеграм бот, который принимает на вход json запросы и выдает агрегированную информацию по зарплатам.  
Стек: async_pymongo, aiogram, asyncio, MongoDB.

## Запуск

1) Заполнить .env_example и переименовать в .env
2) Запустить MondoDB в Docker: docker compose down && docker compose build && docker compose up -d
3) Установить зависимости из папки src: pip install -r requiremets.txt
4) Запустить бота: python main.py

## Ввод/вывод

Формат ввода/запроса:  
{  
&nbsp;&nbsp;"dt_from":"2022-09-01T00:00:00",  
&nbsp;&nbsp;"dt_upto":"2022-12-31T23:59:00",  
&nbsp;&nbsp;"group_type":"month"  
}

Формат вывода:  
{  
&nbsp;&nbsp;"dataset": [5906586, 5515874, 5889803, 6092634],  
&nbsp;&nbsp;"labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00:00:00", "2022-12-01T00:00:00"]  
}

Пример работы:  
  
<img width="456" alt="Снимок экрана 2024-04-22 в 18 50 44" src="https://github.com/yandexwork/SalaryAggregation/assets/134307672/3f181f3f-0f6d-4dd3-b5a2-1b1bfb8c5585">

## Возможные улучшения
1) Поместить бота в Docker;
2) Написать тесты;
3) Добавить докстринги в коде.
