# 順番

* 主処理（APIバックエンド部分）のコンテナ作成
	- 実行コマンド

```terminal
$ cd src
$ docker-compose build
$ docker-compose run \
  --entrypoint "poetry init \
    --name main \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  main
$ docker-compose run --entrypoint "poetry install" main
$ docker-compose up
```

---

* GithubActionsによるLinterの導入
* PR・Issueのテンプレート設定
	- 自動テストは記入のみ、現時点ではコメントアウト

---

#### Branch dev 主処理

* ルータの設定
* スキーマの設定

---

#### Branch dev_createSQL MySQLの設定

* MySQLの設定を`docker-compose.yaml`に記述
* コンパイル

* Pythonサイドとの接続
	- 接続ライブラリをインポート

```
$ docker-compose exec main poetry add sqlalchemy aiomysql
```

```
$ docker-compose exec main poetry run python -m api.create_table
```

−−−

