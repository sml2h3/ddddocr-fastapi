# ocr_api_server
使用ddddocr的最简api搭建项目，支持docker

**建议python版本3.7-3.9 64位**

再有不好好看文档的我就不管了啊！！！

# 运行方式

## 最简单运行方式

```shell
# 安装依赖
pip install -r requirements.txt -i https://pypi.douban.com/simple

# 运行  可选参数如下
# --port 9898 指定端口,默认为9898
# --ocr 开启ocr模块 默认开启
# --old 只有ocr模块开启的情况下生效 默认不开启
# --det 开启目标检测模式

# 最简单运行方式，只开启ocr模块并以新模型计算
python ocr_server.py --port 9898 --ocr

# 开启ocr模块并使用旧模型计算
python ocr_server.py --port 9898 --ocr -old

# 只开启目标检测模块
python ocr_server.py --port 9898  --det

# 同时开启ocr模块以及目标检测模块
python ocr_server.py --port 9898 --ocr --det

# 同时开启ocr模块并使用旧模型计算以及目标检测模块
python ocr_server.py --port 9898 --ocr --old --det

```

## docker运行方式(目测只能在Linux下部署)

```shell
git clone https://github.com/sml2h3/ocr_api_server.git
# docker怎么安装？百度吧

cd ocr_api_server

# 修改entrypoint.sh中的参数，具体参数往上翻，默认9898端口，同时开启ocr模块以及目标检测模块

# 编译镜像
docker build -t ocr_server:v1 .

# 运行镜像
docker run -p 9898:9898 -d ocr_server:v1

```

# 接口

**具体请看test_api.py文件**

```python
# 1、测试是否启动成功，可以通过直接GET访问http://{host}:{port}/ping来测试，如果返回pong则启动成功

# 2、OCR请求

# resp = requests.post("http://{host}:{port}/ocr", files={'image': image_bytes})

# 3、目标检测请求

# resp = requests.post("http://{host}:{port}/det", files={'image': image_bytes})

```
