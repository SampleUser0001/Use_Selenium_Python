# Use_Selenium_Python

SeleniumでWebアクセスを自動化する。

## Selenium Server起動

``` sh
docker-compose -f docker/docker-compose.yml up -d
```

## 実行

``` bash 
docker-compose -f docker/docker-compose.yml exec app /opt/app/start.sh ${pythonファイル名}
```

## 参考

- [10分で理解する Selenium:Qiita](https://qiita.com/Chanmoro/items/9a3c86bb465c1cce738a)
