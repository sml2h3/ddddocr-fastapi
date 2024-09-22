COMMIT_ID = $(shell git rev-parse --short HEAD || echo "HEAD")

DOCKERHUB_ORGANIZATION = registry.cn-shanghai.aliyuncs.com/muzimu
DOCKERHUB_IMAGE = yohe-ddddocr
DOCKERHUB_TAG = ${COMMIT_ID}

DOCKERHUB_USERNAME = <username>
DOCKERHUB_PASSWORD = <password>
DOCKERHUB_REGISTRY = registry.cn-shanghai.aliyuncs.com
