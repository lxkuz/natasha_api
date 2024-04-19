FROM python:3

WORKDIR /usr/src/app

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install natasha
RUN pip install pydantic

COPY . .

CMD [ "/bin/bash", "-c", "uvicorn main:app --reload --host 0.0.0.0 --port 80" ]
