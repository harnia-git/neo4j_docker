# ベースイメージとしてPython 3.10.13を使用
FROM python:3.10.13-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# requirements.txtをコピーして依存関係をインストール
COPY python_docker/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY app/ .

# コンテナ起動時に実行するコマンド
CMD ["python", "main.py"]
