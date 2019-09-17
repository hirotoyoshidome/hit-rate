# hit_rate

## 使い方

chromeのバージョンにあったchromedriverをダウンロードして解凍

```
unzip xxx.zip
```

解凍したものをmain.pyと同ディレクトリに配置
(私の環境で適用したものを配置しておく)
※　importで対応できなかったため

http://chromedriver.chromium.org/downloads


```
docker build -t cache_hit_rate_tool .

docker run --rm cache_hit_rate_tool:latest https:google.com/

```


dockerでうまく行かない場合は、

```
Dockerfileでpipでインストールしているモジュールを入れて実行
python3 main.py https://google.com/
```

でヒット率の確認ができます。


### サンプル実行

```
$ python3 main.py https://repetto.jp/
total hit count : 164
hit percentage  : 49.390243902439025
```
