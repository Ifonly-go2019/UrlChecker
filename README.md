# UrlChecker

**this is a tool to detect the Web service is ok or not.**

没加header的情况：

![](https://cdn.jsdelivr.net/gh/ifonly-go2019/PicGo//images/20201012225747.png)

添加header后：

![](https://cdn.jsdelivr.net/gh/ifonly-go2019/PicGo//images/20201012232349.png)


写这个小jio本的目的是，在大量子域名或者URL的情况下，不想人为去点每个URL去判断系统正常。虽然有很多大型扫描器有这个功能，比如Xray 的html 导出，但是我就是想写一下。后面慢慢加功能。
## Base on http response status code

200、404、403、500、405

## Multithreading

![](https://cdn.jsdelivr.net/gh/ifonly-go2019/PicGo//images/20201012224014.png)


## TODO

- Output results
- Count the number of OK
- colorful terminal strings 😂

## questions & contact 

https://hack-for.fun/
