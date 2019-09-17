# hit_rate

## 使い方

```
docker build -t cache_hit_rate_tool .

docker run --rm cache_hit_rate_tool:latest https://google.com/

```

dockerでうまく行かない場合は、
解凍したものをmain.pyと同ディレクトリに配置
※　importで対応できなかったため
http://chromedriver.chromium.org/downloads

```
Dockerfileでpipでインストールしているモジュールを入れて実行
python3 main.py https://google.com/
```

でヒット率の確認ができます。


### サンプル実行
Docker実行

```
$ docker run --rm cache_hit_rate_tool:latest https://repetto.jp/
total hit count : 173
hit percentage  : 46.82080924855491
error count : 1

```

手動実行

```
$ python3 main.py https://repetto.jp/
total hit count : 164
hit percentage  : 49.390243902439025
```
