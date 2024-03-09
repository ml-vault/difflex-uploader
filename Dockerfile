FROM runpod/pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04
WORKDIR /workspace
COPY . .
RUN apt-get update -y
RUN apt-get install -y python3-tk python3.10-venv libcairo2-dev \
    libcudnn8=8.7.0.84-1+cuda11.8 libcudnn8-dev=8.7.0.84-1+cuda11.8 --allow-change-held-packages
RUN DEBIAN_FRONTEND=noninteractive TZ=Asia/Tokyo apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
RUN chmod +x server.py
RUN chmod +x server.sh
CMD ["sh", "server.sh"]
