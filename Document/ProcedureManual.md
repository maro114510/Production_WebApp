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