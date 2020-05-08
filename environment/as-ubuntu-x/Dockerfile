FROM ubuntu:16.04

ARG TERM=xterm
ARG LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean && \
    apt-get update && \
    apt-get install --yes --no-install-recommends apt-utils && \
    apt-get install --yes --no-install-recommends apt-transport-https && \
    apt-get install -y sudo \
        vim \
        openssh-server \
        && \
    useradd -m username -p username && \
    usermod -aG sudo username && \
    echo "ALL ALL=(ALL) NOPASSWD:ALL">/etc/sudoers.d/sudo


# TODO: remove cat from the RUN, due to cat has been used and a debug
RUN cat /etc/ssh/sshd_config | grep PasswordAuthentication && \
    sed -i '/^#PasswordAuthentication /s/^#//' /etc/ssh/sshd_config && \
    cat /etc/ssh/sshd_config | grep PasswordAuthentication && \
    /etc/init.d/ssh restart

RUN apt-get update && \
    apt-get install -y ubuntu-desktop && \
    apt-get install -y vnc4server


USER username

RUN sudo apt-get update && \
    sudo apt-get install -y \
    gnome-panel \
    gnome-settings-daemon \
    metacity \
    nautilus \
    gnome-terminal

COPY ./resources/xstartup ./resources/passwd /home/username/.vnc/
RUN sudo chown -R username /home/username && \
    chmod 0600 /home/username/.vnc/passwd

EXPOSE 5901/tcp

CMD vncserver &> /tmp/vnc_startup.log
