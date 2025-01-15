# 林木病虫害检测系统
> Developed by Xiaoyu

本系统是基于 [Ultralytics YOLO V11](https://github.com/ultralytics) 开发的，用于检测林木的病虫害情况。

## 项目结构

- **Docker/**: 包含构建Docker镜像所需的`Dockerfile`。
- **trained_models/**: 存放训练后模型文件。
- **data/**: 存放训练和测试数据，包括图像和标签文件。
- **README.md**: 项目的说明文件，包含使用说明、项目结构等信息。

## 使用方法

### 环境搭建

推荐使用 [Docker](https://www.docker.com/) 搭建环境
或者手动搭建Aanaconda + Pytorch + CUDA 环境

#### 1、构建 Docker 镜像

使用项目目录下的 `Docker/Dockerfile` 来构建 Docker 镜像：

```bash
docker build -t xiaoyu/ultralytics .
```

#### 2、启动 Docker 容器

构建完成后，可以使用以下命令来启动 Docker 容器：

```bash
docker run \
  --name yolov11 \
  --volume=/yolo:/ultralytics/ \
  --network=bridge \
  -p 2022:22 \
  -p 6066:6006 \
  --restart=no \
  --runtime=runc \
  -t -d xiaoyu/ultralytics
```

> **注意：**
> - `-p 2022:22` 映射 SSH 端口
> - `-p 6066:6006` 映射 TensorBoard 端口
> - `--volume=/yolo:/ultralytics/` 将主机的 `/yolo` 目录挂载到容器的 `/ultralytics/` 目录

#### 3、使用 PyCharm 远程链接 Docker 容器
略

#### 4、运行 gpu_test.py
测试环境内是否可以正常配置GPU

#### 5、把图片存放至 input_images
图片格式为JPG和PNG

#### 5、运行 predict.py 进行推理和目标检测
直接运行predict.py即可，结果会保存在output_images文件夹中