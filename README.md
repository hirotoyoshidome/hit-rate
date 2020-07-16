# hit_rate
CDNでのヒット率の確認ができます。

## 手順最新版(2020.07.16)

```
docker build -t cache_hit_rate_tool .
docker run --rm -it -d -v $(pwd):/usr/src --name cache_hit_late cache_hit_rate_tool:latest
docker exec -it cache_hit_late sh
python main.py https://google.com/
docker stop cache_hit_late
```

### サンプル実行

```
$ python main.py https://repetto.jp/
total hit count : 155
hit percentage  : 47.74193548387097
error count : 2
```
