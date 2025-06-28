# Parte I: Fundamentos do Apache Kafka

![Apache Kafka com Java – Parte I](img/kafka-java-parte1.png)

## Introdução

Esta parte apresenta os conceitos essenciais do Apache Kafka, sua arquitetura, principais componentes e comandos básicos para quem está começando.

## O que é Apache Kafka?

Apache Kafka é uma plataforma distribuída de streaming de eventos, projetada para alta performance, escalabilidade e tolerância a falhas. É amplamente utilizada para processamento de dados em tempo real, integração entre sistemas e pipelines de dados.

## Conceitos Principais

- Broker: Servidor Kafka responsável por armazenar e entregar mensagens.
- Topic: Canal lógico onde as mensagens são publicadas e consumidas.
- Partition: Subdivisão de um tópico para escalabilidade e paralelismo.
- Producer: Aplicação que envia mensagens para o Kafka.
- Consumer: Aplicação que lê mensagens do Kafka.
- Consumer Group: Grupo de consumidores que compartilham a leitura de partições.
- Offset: Posição sequencial de uma mensagem dentro de uma partição.

## Arquitetura Básica

1. Producers publicam mensagens em tópicos.
2. Brokers armazenam as mensagens.
3. Consumers leem as mensagens dos tópicos.
4. O Kafka garante alta disponibilidade e escalabilidade por meio de partições e replicação.

## Instalação Rápida com Docker

```bash
docker-compose up -d
```

## Comandos Essenciais

- Criar um tópico:

```bash
kafka-topics --create --topic meu-topico --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

- Produzir mensagens:

```bash
kafka-console-producer --topic meu-topico --bootstrap-server localhost:9092
```

- Consumir mensagens:

```bash
kafka-console-consumer --topic meu-topico --from-beginning --bootstrap-server localhost:9092
```

## Exercícios Práticos

1. Suba o ambiente Kafka localmente.
2. Crie tópicos com diferentes números de partições.
3. Produza e consuma mensagens usando o terminal.
4. Experimente criar múltiplos consumidores em um mesmo grupo.

## Recursos Recomendados

- [Documentação Oficial do Apache Kafka](https://kafka.apache.org/documentation/)
- Livro: Kafka: The Definitive Guide (O'Reilly)

---

## Exemplo Java: Producer e Consumer Simples

A seguir, um exemplo básico de como produzir e consumir mensagens com Java e Apache Kafka. Para rodar, adicione a dependência do Kafka Client no seu `pom.xml`:

```xml
<dependency>
  <groupId>org.apache.kafka</groupId>
  <artifactId>kafka-clients</artifactId>
  <version>3.7.0</version>
</dependency>
```

### Producer Java

```java
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import java.util.Properties;

public class SimpleProducer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        try (KafkaProducer<String, String> producer = new KafkaProducer<>(props)) {
            producer.send(new ProducerRecord<>("meu-topico", "mensagem de exemplo"));
            System.out.println("Mensagem enviada!");
        }
    }
}
```

### Consumer Java

```java
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import java.util.Collections;
import java.util.Properties;

public class SimpleConsumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "grupo-exemplo");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {
            consumer.subscribe(Collections.singletonList("meu-topico"));
            ConsumerRecords<String, String> records = consumer.poll(java.time.Duration.ofSeconds(5));
            for (ConsumerRecord<String, String> record : records) {
                System.out.printf("Recebido: %s%n", record.value());
            }
        }
    }
}
```

Esses exemplos são apenas para fins didáticos e funcionam em ambientes locais com o Kafka rodando no padrão (`localhost:9092`).

Siga para a Parte II para exemplos mais avançados e integração completa com Java.
