FROM python:3.10 
WORKDIR /code 

COPY ./configuration /code/configuration
COPY ./data /code/data
COPY ./docs /code/docs
COPY ./dumps /code/dumps
COPY ./reports /code/reports
COPY ./src /code/src
COPY ./tests /code/tests
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock 

RUN pip install poetry 
RUN poetry lock
RUN poetry install
CMD ["poetry", "run", "pizzeria"]

