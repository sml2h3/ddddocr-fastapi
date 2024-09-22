include common.mk

.PHONY: build-image push-image 

build-image: 
	docker build --pull \
		-t="$(DOCKERHUB_ORGANIZATION)/$(DOCKERHUB_IMAGE):$(DOCKERHUB_TAG)" \
		-f Dockerfile .

push-image: 
	docker login --username=$(DOCKERHUB_USERNAME) -p $(DOCKERHUB_PASSWORD) $(DOCKERHUB_REGISTRY)
	docker push "$(DOCKERHUB_ORGANIZATION)/$(DOCKERHUB_IMAGE):$(DOCKERHUB_TAG)"
