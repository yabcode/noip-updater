# No-IP Updater

## No-IP アカウント情報設定

```json:config.json
{
    "no_ip": {
        "username": "ユーザー名",
        "password": "パスワード"
    }
}
```

## Docker Image 作成

```bash
$ docker build -t noip-updater .
```
## 実行

```bash
$ docker run -t --rm noip-updater
```
