<p align="center">
    <img src='https://raw.githubusercontent.com/TVIP-IPTV/TVIPChannelToM3u/main/assets/tvip-logo.png' alt='Логотип' width='15%'>
</p>

<h2 align="center">
TVIP TMS Channel Check
</h2>

Этот проект предназначен для проверки доступности каналов из TVIP TMS на основе JSON данных и вывода результата в лог.

> [!WARNING]
> Проект проверяет только те каналы, которые включены (enabled = true).
> так же, программа работает на API ADMIN, а не API PROVIDER

## Установка

Перед началом работы убедитесь, что у вас установлены все необходимые зависимости. Вы можете установить их с помощью файла `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Использование

Запустите скрипт `main.py`, чтобы проверить доступность каналов.

```bash
python main.py
```

Следуйте инструкциям на экране:

a. Введите URL TMS.
b. Введите ваш TOKEN для доступа к TMS.

## Пример

При запуске скрипт запросит у вас URL TMS и TOKEN. Затем он получит список каналов через TMS API и проверит их доступность. В результате будет выведена информация о количестве рабочих и нерабочих каналов.

## Структура проекта

```
a. main.py: Основной скрипт для проверки доступности каналов.
b. requirements.txt: Файл с зависимостями для проекта.
```

## Поддержка

Если у вас возникли проблемы или вы нашли ошибку, пожалуйста, оставьте сообщение в разделе Issues на GitHub.

## Лицензия

Этот проект лицензируется под [MIT License](https://github.com/TVIP-IPTV/TVIPChannelsCheck/blob/main/LICENSE).
