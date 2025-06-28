# Parte Final: Kafka Avançado e Produção

![Apache Kafka com Java – Parte Final](img/kafka-java-parte-final.png)

## Visão Geral

Esta parte é dedicada a tópicos avançados, integração com o ecossistema Kafka, monitoramento, segurança e práticas recomendadas para ambientes de produção.

## Artefatos Práticos

Os principais artefatos para colocar em prática os tópicos avançados desta parte estão organizados na pasta `artefatos-final/` do repositório:

- `docker-compose-multibroker.yml`: Exemplo de configuração de cluster Kafka com múltiplos brokers
- `monitoramento/`: Scripts e exemplos para Prometheus e Grafana
- `seguranca/`: Arquivos de configuração de autenticação/autorização (SASL/SSL, ACLs)
- `schema-registry/`: Exemplo de schema Avro
- `kafka-connect/`: Exemplo de configuração de conector JDBC
- `backup-e-automacao/`: Script de backup de tópicos
- `boas-praticas/`: Checklist de produção

Consulte cada subpasta para exemplos práticos e adapte conforme o seu ambiente.

## Processamento Avançado

### Kafka Streams

- Processamento de dados em tempo real diretamente no Kafka
- Exemplo de uso para agregações, joins e transformações

### Kafka Connect

- Integração com bancos de dados, sistemas legados e APIs
- Uso de conectores prontos (JDBC, Elasticsearch, etc.)

### Schema Registry

- Gerenciamento de esquemas de dados (Avro, Protobuf, JSON Schema)
- Evolução de schemas e compatibilidade

## Monitoramento e Observabilidade

- Monitoramento de brokers, tópicos e consumidores
- Uso de JMX, Prometheus e Grafana para métricas
- Monitoramento de lag de consumidores
- Alertas e dashboards

## Segurança

- Autenticação (SASL, SSL/TLS)
- Autorização (ACLs)
- Boas práticas para ambientes corporativos

## Deploy e Operação

- Deploy em cluster (alta disponibilidade e replicação)
- Kafka em nuvem (Confluent Cloud, AWS MSK, Azure Event Hubs)
- Backup, restauração e upgrades
- Gerenciamento de recursos e tuning de performance

## Boas Práticas para Produção

- Configuração de retenção de dados
- Estratégias de particionamento
- Políticas de replicação
- Testes de resiliência e failover
- Documentação e automação de operações

## Exercícios Sugeridos

1. Configurar um cluster Kafka com múltiplos brokers
2. Implementar monitoramento com Prometheus e Grafana
3. Configurar autenticação e autorização
4. Realizar testes de failover e recuperação
5. Integrar Kafka com outros sistemas usando Kafka Connect

## Recursos Recomendados

- [Confluent Platform Documentation](https://docs.confluent.io/)
- [Kafka Streams Documentation](https://kafka.apache.org/documentation/streams/)
- [Spring Kafka Reference](https://docs.spring.io/spring-kafka/docs/current/reference/html/)

---

## Código-Fonte e Exemplos

Todo o conteúdo, exemplos práticos e arquivos de configuração desta parte estão disponíveis no repositório oficial do projeto no GitHub:

[🔗 github.com/chmulato/kafka-java-mastery](https://github.com/chmulato/kafka-java-mastery)

Acesse, explore e contribua!

Parabéns! Você concluiu o guia completo. Agora está pronto para atuar com Apache Kafka em ambientes profissionais e avançados.

⬅️ [Voltar ao Guia Principal (README)](README.md)
