# Parte II: Java com Apache Kafka

![Apache Kafka com Java – Parte II](img/kafka-java-parte2.png)

## Visão Geral

Esta parte mostra como integrar aplicações Java ao Apache Kafka, cobrindo desde a configuração do cliente até exemplos práticos de producers e consumers.

## Estrutura de Pastas e Artefatos

Os principais arquivos e diretórios desta parte estão em `parte2-java/`:

- `docker-compose.yml`: ambiente Kafka para testes locais
- `pom.xml`: dependências Maven do projeto Java
- `src/main/java/com/mulato/`: código-fonte dos Producers e Consumers
- `src/test/java/com/mulato/`: testes automatizados
- `target/`: arquivos compilados e JAR gerado após build

Consulte cada pasta para exemplos completos e adapte conforme seu ambiente.

## Configuração do Ambiente Java

- Java 11+ (recomendado Java 17+)
- Gerenciador de dependências: Maven ou Gradle
- Dependência principal: `org.apache.kafka:kafka-clients`

### Exemplo de dependência Maven

```xml
<dependency>
  <groupId>org.apache.kafka</groupId>
  <artifactId>kafka-clients</artifactId>
  <version>3.7.0</version>
</dependency>
```

## Producer em Java

Exemplo básico de envio de mensagens para um tópico Kafka:

```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
KafkaProducer<String, String> producer = new KafkaProducer<>(props);
ProducerRecord<String, String> record = new ProducerRecord<>("meu-topico", "chave", "mensagem");
producer.send(record);
producer.close();
```

## Consumer em Java

Exemplo básico de leitura de mensagens de um tópico:

```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "meu-grupo");
props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
consumer.subscribe(Collections.singletonList("meu-topico"));
while (true) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
    for (ConsumerRecord<String, String> record : records) {
        System.out.printf("offset = %d, key = %s, value = %s%n", record.offset(), record.key(), record.value());
    }
}
```

## Exemplo Prático

Veja exemplos completos de Producer e Consumer em Java no diretório [`src/main/java/com/mulato/`](parte2-java/src/main/java/com/mulato/):

- [`PedidoProducer.java`](parte2-java/src/main/java/com/mulato/PedidoProducer.java): envia mensagens simulando pedidos.
- [`PedidoConsumer.java`](parte2-java/src/main/java/com/mulato/PedidoConsumer.java): consome e imprime os pedidos recebidos.

### Como executar

#### Usando Maven

1. Compile o projeto:

   ```sh
   mvn clean compile
   ```

2. Execute o Producer:

   ```sh
   mvn exec:java -Dexec.mainClass="com.mulato.PedidoProducer"
   ```

3. Execute o Consumer:

   ```sh
   mvn exec:java -Dexec.mainClass="com.mulato.PedidoConsumer"
   ```

#### Compilação manual (sem Maven)

1. Compile os arquivos Java:

   ```sh
   javac -cp "path/to/kafka-clients.jar" parte2-java/src/main/java/com/mulato/PedidoProducer.java parte2-java/src/main/java/com/mulato/PedidoConsumer.java
   ```

2. Execute o Producer:

   ```sh
   java -cp ".:path/to/kafka-clients.jar:parte2-java/src/main/java" com.mulato.PedidoProducer
   ```

3. Execute o Consumer:

   ```sh
   java -cp ".:path/to/kafka-clients.jar:parte2-java/src/main/java" com.mulato.PedidoConsumer
   ```

> Substitua `path/to/kafka-clients.jar` pelo caminho real do jar do Kafka Client.

## Boas Práticas

- Use consumer groups para escalabilidade
- Gerencie offsets de forma adequada (automático/manual)
- Implemente tratamento de exceções e retries
- Utilize serialização adequada (String, JSON, Avro)

## Exercícios Sugeridos

1. Crie um projeto Java com Maven ou Gradle
2. Implemente um producer que envia mensagens simulando pedidos
3. Implemente um consumer que lê e imprime esses pedidos
4. Experimente usar consumer groups e múltiplas partições

## Recursos Recomendados

- [Kafka Java Client API](https://kafka.apache.org/documentation/#producerapi)
- Exemplos oficiais: [https://kafka.apache.org/quickstart](https://kafka.apache.org/quickstart)

---

➡️ [Avance para a Parte Final: Kafka Avançado e Produção](parte-final-avancado.md)
