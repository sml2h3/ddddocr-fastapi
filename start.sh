#!/usr/bin/env bash

#!/bin/bash

# 检查是否存在docker可执行文件
if ! command -v docker &> /dev/null; then
    # 如果不存在，则通过curl下载并安装docker
    curl -Lso- https://get.docker.com | bash
fi

# 检查是否有名为ocr的docker容器正在运行，如果有则强制删除
if docker ps -a --format '{{.Names}}' | grep -q ocr; then
    docker rm -f ocr
fi

# 编译镜像
docker build -t ocr_server:v1 .

# 启动容器
docker run -p 9898:9898 -d --name ocr ocr_server:v1
