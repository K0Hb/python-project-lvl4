FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /task_manager

WORKDIR /task_manager

COPY ./requirements.txt /task_manager

RUN pip install -r requirements.txt

COPY .  /task_manager

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#  docker run -p 8000:8000  509c05babe06 - запуск контейнера