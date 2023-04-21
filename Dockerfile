FROM ubuntu:latest

RUN apt-get update && \
    apt-get install curl -y && \
    apt-get install git -y && \
    apt-get install links -y && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m stk

RUN curl -fsSL https://stk.stackspot.com/install.sh | bash && \
mv /root/.stk/bin/* /usr/local/bin

RUN chmod 755 /usr/local/bin/stk

USER stk

WORKDIR /home/stk

CMD ["bash"]
