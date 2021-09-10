export CMS_LOCAL_HTTP_PORT=80
export CMS_CONTAINER_HTTP_PORT=80
export CMS_CONTAINER_NAME="cms-one"
export CMS_CONTAINER_IMAGE="igaki/cms-one:1.0"
export CMS_DOCKER_FILE="./Dockerfile-local"

# 環境の初期化
echo "initialize environment"
echo "stop container"
docker-compose down

# ビルド
docker-compose up -d

