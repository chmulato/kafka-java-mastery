# Guia Completo: Apache Kafka com Java

Este guia prático está dividido em três partes, acompanhando a estrutura do artigo principal. Ele serve como roteiro para quem deseja aprender Kafka do zero até o uso avançado com Java.

---

## Parte I – Fundamentos do Apache Kafka

**Objetivo:** Compreender o que é o Kafka, sua arquitetura, principais conceitos e realizar os primeiros experimentos práticos.

### Principais Conceitos

- Broker: servidor Kafka que armazena e entrega mensagens.
- Topic: canal lógico para publicação e consumo de mensagens.
- Partition: subdivisão de um tópico para escalabilidade.
- Producer: envia mensagens para o Kafka.
- Consumer: lê mensagens do Kafka.
- Consumer Group: grupo de consumidores que compartilham a leitura.
- Offset: posição sequencial de uma mensagem.

### Passos Práticos

1.Suba o ambiente local com Docker:

   ```bash
docker-compose up -d
```

2.Crie um tópico:

```bash
kafka-topics --create --topic meu-topico --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

3.Produza mensagens:

```bash
kafka-console-producer --topic meu-topico --bootstrap-server localhost:9092
```

4.Consuma mensagens:
```bash
kafka-console-consumer --topic meu-topico --from-beginning --bootstrap-server localhost:9092
```

### Recomendações

- Experimente criar múltiplos consumidores e tópicos.
- Consulte a [documentação oficial](https://kafka.apache.org/documentation/).

---

## Parte II – Java com Kafka

**Objetivo:** Aprender a integrar aplicações Java ao Kafka, criando producers e consumers básicos.

### O que você aprende

- Como adicionar a dependência `org.apache.kafka:kafka-clients` ao seu projeto (Maven ou Gradle).
- Como configurar e implementar um producer e um consumer simples em Java.
- Práticas iniciais de serialização (String).

### Passos Práticos

1. Crie um projeto Java simples.
2. Implemente um producer:
   - Configure as propriedades de conexão.
   - Envie mensagens para um tópico.
3. Implemente um consumer:
   - Configure o group.id e as propriedades de conexão.
   - Consuma mensagens do tópico.

### Recomendações

- Teste com diferentes tópicos e grupos de consumidores.
- Consulte exemplos na [documentação oficial](https://kafka.apache.org/quickstart).

---

## Parte Final – Avançado Essencial

**Objetivo:** Conhecer recursos avançados e boas práticas para produção, sem aprofundar em detalhes de especialista.

### O que você aprende

- Introdução ao Kafka Streams para processamento de dados em tempo real.
- Uso do Kafka Connect para integração com bancos de dados e outros sistemas.
- Noções de monitoramento (Prometheus, Grafana) e segurança (SASL/SSL, ACLs).

### Passos Práticos

1. Explore o Kafka Connect para integrar com bancos ou arquivos.
2. Experimente monitorar o Kafka com Prometheus e Grafana.
3. Conheça o básico de autenticação (SASL/SSL) e permissões (ACLs).

### Recomendações

- Leia sobre Kafka Streams para cenários de processamento.
- Consulte a [Confluent Platform Documentation](https://docs.confluent.io/).
- Use sempre ambientes de teste antes de ir para produção.

---

**Com este guia, você terá o necessário para iniciar projetos reais com Apache Kafka e Java, evoluindo do básico ao avançado com confiança.**
