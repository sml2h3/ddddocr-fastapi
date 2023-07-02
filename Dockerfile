# 使用python:3.8-slim-buster作为基础镜像
FROM python:3.8-slim-buster

# 创建app目录来存储我们的代码
RUN mkdir /app

# 将工作目录设置为/app，这意味着后续的指令都在/app下执行
WORKDIR /app

# 将当前目录（即你的项目目录）下的所有文件和文件夹复制到镜像的/app目录下
COPY . /app

# 安装Python依赖
RUN pip3 install --no-cache-dir ddddocr flask 


# 定义容器启动时要运行的命令
CMD ["python3", "ocr_server.py", "--port", "9898", "--ocr", "--det"]
