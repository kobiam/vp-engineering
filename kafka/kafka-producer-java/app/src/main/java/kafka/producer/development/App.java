package kafka.producer.development;

import org.slf4j.Logger;
import java.util.Properties;
import org.slf4j.LoggerFactory;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;


public class App {

    private static final Logger log = LoggerFactory.getLogger(App.class.getSimpleName());

    public String getGreeting() {
        return "Test java app!";
    }
    public static void main(String[] args) {
        // just a message
        System.out.println("Test Kafka Producer");
        log.info("output from log");

        // connecting producer
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "kafka-svc.kafka-kraft.svc.cluster.local:9092");

        // creating producer properties
        properties.put("key.serializer", StringSerializer.class.getName());
        properties.put("value.serializer", StringSerializer.class.getName());

        // add compression
        properties.put(ProducerConfig.COMPRESSION_TYPE_CONFIG, "snappy");

        // creating producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

        // creating producer record
        ProducerRecord<String, String> producerRecord = new ProducerRecord<>("test", "message from producer");

        // sending record
        for(int i = 0; i < 500; ++i)
            producer.send(producerRecord);

        // close producer
        producer.close();
        
        // just a message
        System.out.println("Messages sent");
    }
}