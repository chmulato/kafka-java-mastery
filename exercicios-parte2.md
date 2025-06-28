# Parte 2 - Java com Kafka

## Dicas Gerais

- Use o `docker-compose.yml` da pasta `parte2-java/` para subir o ambiente Kafka local:

  ```sh
  docker-compose up -d
  ```

- Para criar o tópico `pedidos` com múltiplas partições (exemplo: 3):

  ```sh
  docker exec -it <nome_do_container_kafka> kafka-topics --bootstrap-server localhost:9092 --create --topic pedidos --partitions 3 --replication-factor 1
  ```
  > Use `docker ps` para descobrir o nome do container Kafka.

- Para rodar múltiplos consumers, abra vários terminais e execute:

  ```sh
  mvn exec:java -Dexec.mainClass="ExemploConsumer"
  ```

- Para enviar mensagens com o Producer:

  ```sh
  mvn exec:java -Dexec.mainClass="ExemploProducer"
  ```

- Para compilar o projeto:

  ```sh
  mvn clean compile
  ```

- Consulte a documentação oficial do Kafka para detalhes de configuração.
- Personalize as mensagens, tópicos e lógica conforme desejar.

## Espaço para Respostas

Anote abaixo suas observações, comandos utilizados e aprendizados. Exemplo de preenchimento:

```markdown
### 1. Projeto Maven criado com sucesso
- Comando: mvn archetype:generate ...
- Adicionei a dependência kafka-clients no pom.xml

### 2. Producer implementado
- Mensagens enviadas: Pedido #1, Pedido #2, ...
- Comando: mvn exec:java -Dexec.mainClass="ExemploProducer"

### 3. Consumer implementado
- Mensagens recebidas corretamente
- Comando: mvn exec:java -Dexec.mainClass="ExemploConsumer"

### 4. Teste com múltiplos consumers
- Abri 2 terminais, cada um rodando o Consumer
- Kafka distribuiu as mensagens entre eles

### 5. Teste automatizado
- Implementei um teste de integração semelhante ao KafkaIntegrationTest.java
- Resultado: OK
```

---

Bons estudos!