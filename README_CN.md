#Python 笔记八：瓦片下载器网页版pyMap-webapp

[英文文档](README.md)

> 源码github地址在此，记得点星：
https://github.com/brandonxiang/pyMap_webapp

紧接着[Python 笔记八：简单瓦片下载工具pyMap](http://www.jianshu.com/p/a3b2e01f602f)，有人和我说命令行并不是很好用，我决心做一个网页版本。结合[pyMap](https://github.com/brandonxiang/pyMap)和[Mapviewer](https://github.com/brandonxiang/MapViewer)，在网页上实现一体化的选择区域，表单提交下载图片。

## 版本

目前版本alpha v0.12

## 依赖

- python 3.5
- [Flask](https://github.com/pallets/flask)
- [pyMap](https://github.com/brandonxiang/pyMap)
- [Mapviewer](https://github.com/brandonxiang/MapViewer)

## 安装

```
pip install -r requirement
```

## 使用

- 用矩形工具画一个区域
- 双击该区域下载地图
- 填入属性

## 开发

开发在develop分支，而稳定版在master分支。


## TODO

- 图片选择RGBA或RGB
- 下载功能
- 下载进度条

## License

[MIT](LICENSE)