FROM ubuntu:focal

LABEL description="Docker image based on ubuntu 20.04 with armg toolchain and armhf packages for Raspberry Pi"

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHON 3.9.2

ENV CMAKE /usr/share/cmake-3.19.7/bin/cmake

COPY sources.list /etc/apt/sources.list

WORKDIR /root
RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       sudo ca-certificates \
       make build-essential libssl-dev zlib1g-dev libbz2-dev \
       libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
       xz-utils tk-dev libffi-dev liblzma-dev python-openssl git wget sudo file \
       autotools-dev automake linux-libc-dev subversion subversion-tools ninja-build \
    && ln -s /usr/include/asm-generic/ /usr/include/asm \
    && wget https://github.com/Kitware/CMake/releases/download/v3.19.7/cmake-3.19.7-Linux-x86_64.tar.gz   \
    && tar -xvzf cmake-3.19.7-Linux-x86_64.tar.gz && mv cmake-3.19.7-Linux-x86_64 /usr/share/cmake-3.19.7 \
    && update-alternatives --install /usr/bin/cmake cmake $CMAKE 40 \
    && sudo apt-get install -y --no-install-recommends --no-install-suggests ".*10.*arm-linux-gnueabihf.*" \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcc arm-linux-gnueabihf-gcc /usr/bin/arm-linux-gnueabihf-gcc-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-g++ arm-linux-gnueabihf-g++ /usr/bin/arm-linux-gnueabihf-g++-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov arm-linux-gnueabihf-gcov /usr/bin/arm-linux-gnueabihf-gcov-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov-dump arm-linux-gnueabihf-gcov-dump /usr/bin/arm-linux-gnueabihf-gcov-dump-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov-tool arm-linux-gnueabihf-gcov-tool /usr/bin/arm-linux-gnueabihf-gcov-tool-10 100

COPY arm-cross-compile-sources.list /etc/apt/sources.list.d/arm-cross-compile-sources.list

RUN useradd -ms /bin/bash carlos && echo "carlos:carlos" | chpasswd && adduser carlos sudo
RUN echo "ALL ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER carlos
WORKDIR /home/carlos
ENV PATH /home/carlos/.pyenv/shims:/home/carlos/.pyenv/bin:$PATH
RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash \
    && pyenv init - \
    && pyenv virtualenv-init - \
    && pyenv update \
    && pyenv install $PYTHON \
    && pyenv global $PYTHON

RUN sudo dpkg --add-architecture armhf \
    && sudo apt-get -qq update

COPY profiles/default /home/carlos/.config/default
COPY profiles/rpi /home/carlos/.config/rpi

RUN pip install conan

RUN conan config install /home/carlos/.config/default -tf profiles && \ 
    conan config install /home/carlos/.config/rpi -tf profiles

ENV CONAN_SYSREQUIRES_MODE enabled
ENV PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/lib/arm-linux-gnueabihf/pkgconfig/
ENV PKG_CONFIG_LIBDIR=$PKG_CONFIG_LIBDIR:/usr/lib/arm-linux-gnueabihf/
COPY --chown=carlos conan-packages /home/carlos/conan-packages

RUN conan create conan-packages/opengles/all opengles/system@ -pr:h=rpi -pr:b=default
RUN conan create conan-packages/drm/all drm/system@ -pr:h=rpi -pr:b=default
RUN conan create conan-packages/gbm/all gbm/system@ -pr:h=rpi -pr:b=default
RUN conan create conan-packages/libvlc/all libvlc/system@ -pr:h=rpi -pr:b=default
