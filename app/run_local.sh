#!/bin/bash

# 環境変数が設定されているかチェック
if [ -z "$NEO4J_HOST" ] || [ -z "$NEO4J_PORT" ] || [ -z "$NEO4J_USER" ] || [ -z "$NEO4J_PASSWORD" ]; then
    echo "Error: Required environment variables are not set."
    echo "Please make sure NEO4J_HOST, NEO4J_PORT, NEO4J_USER, and NEO4J_PASSWORD are set."
    exit 1
fi


# Pythonスクリプトを実行
python ./app/main.py
#chmod +x run_local.shして実行する