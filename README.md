### Hexlet tests and linter status:
[![Actions Status](https://github.com/K0Hb/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/K0Hb/python-project-lvl4/actions)
<a href="https://codeclimate.com/github/K0Hb/python-project-lvl4/maintainability"><img src="https://api.codeclimate.com/v1/badges/59a9ee9d3bb66f1e4aa5/maintainability" /></a>
<a href="https://codeclimate.com/github/K0Hb/python-project-lvl4/test_coverage"><img src="https://api.codeclimate.com/v1/badges/59a9ee9d3bb66f1e4aa5/test_coverage" /></a>

[comment]: <> ([![Build Status]&#40;https://app.travis-ci.com/K0Hb/python-project-lvl4.svg?branch=main&#41;]&#40;https://app.travis-ci.com/K0Hb/python-project-lvl4&#41;)
______
###  Простой пример реализации мененджера задач, с помощью framework Django.

Ссылка для просомтра: https://task-manager-app-ru.herokuapp.com/

______
### Запуск сервера с помощью Docker:

`touch .env` - создаем env файл и заполняем его как в файле  `env(example)`

`docker build .` - создание образоа

`docker images` - ищем наш IMAGE ID

`docker run -p 8000:8000` + наш IMAGE ID

CONTROL-C - комманда остановки сервера 
