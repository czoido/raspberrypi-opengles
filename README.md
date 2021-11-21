# raspberrypi-opengles

Cross-compile OpenGLES applications without X from a Docker image with Conan. It has a basic implementation of Conan System Packages  for:

- OpenGLES
- DRM (Direct Rendering Manager)
- GBM (Graphics Buffer Manager)

Build the Docker image and run it:

```
docker build -t rpi-opengles docker_images
docker run -v $(pwd)/kmscube:/home/kmscube -it rpi-opengles
```

Inside the Docker image you can create the application that will be cross-compiled for Raspberry Pi

```
cd /home/kmscube/
conan create . -pr:h=rpi -pr:b=default
```

