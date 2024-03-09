FROM runpod/base:0.5.1-cpu
WORKDIR /workspace
COPY . .
RUN pip install -r
CMD ["sh", "server.sh"]
