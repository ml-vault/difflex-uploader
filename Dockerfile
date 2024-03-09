FROM runpod/base:0.5.1-cpu
WORKDIR /workspace
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x server.py
RUN chmod +x server.sh
CMD ["sh", "server.sh"]
