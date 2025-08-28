FROM python:3.11-slim


WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


COPY pyproject.toml ./
#COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install uv && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi && \
    if [ -f pyproject.toml ]; then pip install .; fi


COPY . .


EXPOSE 8000


ENV PYTHONUNBUFFERED=1

CMD ["uv","run" ,"app/main.py"]
