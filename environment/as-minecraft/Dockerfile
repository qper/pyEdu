#docker build -t as-minecraft:latest -f Dockerfile .

#xhost +
#sudo modprobe snd-aloop index=2

#docker run -it --rm \
#--env="DISPLAY" \
#--env "NO_AT_BRIDGE=1" \
#--device /dev/snd \
#-e ALSADEV=hw:2,0 \
#--device=/dev/dri:/dev/dri \
#--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
#--volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
#as-minecraft:latest

FROM ubuntu:16.04

ARG TERM=xterm
ARG LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install --yes --no-install-recommends apt-utils && \
    apt-get install --yes --no-install-recommends apt-transport-https && \
    apt-get install --yes --no-install-recommends software-properties-common && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        gdebi-core \
        wget \
    && \
    wget --no-check-certificate -O Minecraft.deb https://launcher.mojang.com/download/Minecraft.deb && \
    gdebi -qn Minecraft.deb && \
    rm -f Minecraft.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV NO_AT_BRIDGE=1

CMD minecraft-launcher
