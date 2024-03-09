FROM runpod/base:0.5.1-cpu
WORKDIR /workspace
COPY . .
RUN pip install -r requirements.txt
CMD ["sh", "server.sh"]
