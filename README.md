# 概要
FastAPI+rye+Dockerの環境を構築する自分用のテンプレート

# 作成方法

```
docker compose up -d
```

### ローカル実行時のAPI
http://localhost:8080/

http://localhost:8080/items/5?q=somequery

#### docs
http://localhost:8080/docs#/

# 終了方法
```
docker compose down
```

# GC-Cloud RUN　実行時

```
L33~36を以下に変更

# ENTRYPOINT ["/app/.venv/bin/uvicorn", "src.
# main:app", "--host", "0.0.0.0", "--port", "8080"]

CloundRun実行の際
ENTRYPOINT ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "$PORT"]
```
Container Registoryにpushする
```
docker build . -t app

docker tag app gcr.io/[GCPプロジェクト名]/[GCP内でのイメージ名]

docker push gcr.io/[GCPプロジェクト名]/[GCP内でのイメージ名]
```


# ディレクトリ

```
.
├── README.md
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── src
│   └── main.py
├── compose.yml
├── .python-version
├── requirements-dev.lock
├── requirements.lock
└── pyproject.toml

```
