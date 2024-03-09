FROM runpod/base:0.5.1-cpu

RUN pip install mlvault
CMD ["sh", "server.sh"]
