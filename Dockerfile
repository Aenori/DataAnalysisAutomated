FROM python:3.9

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         postgresql-client \
#     && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt 2>/dev/null
COPY . .

EXPOSE 5000
CMD ["python", "application.py"]

