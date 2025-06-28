#!/bin/bash
# Exemplo de backup de tópicos Kafka
kafka-topics.sh --bootstrap-server localhost:9092 --list > topicos.txt
