package main

import (
	"fmt"
	"log"
	"os"
	"os/signal"

	"github.com/IBM/sarama"
)

func main() {
	// Set up configuration
	config := sarama.NewConfig()
	config.Producer.Return.Successes = true
	config.Producer.Return.Errors = true

	// Define Kafka broker addresses
	brokers := []string{"localhost:9092"}

	// Create new sync producer
	producer, err := sarama.NewSyncProducer(brokers, config)
	if err != nil {
		log.Fatalf("Error creating producer: %v", err)
	}
	defer func() {
		if err := producer.Close(); err != nil {
			log.Fatalf("Error closing producer: %v", err)
		}
	}()

	// Define Kafka topic
	topic := "test-topic"

	// Set up signal channel to handle termination
	sigchan := make(chan os.Signal, 1)
	signal.Notify(sigchan, os.Interrupt)

	// Produce messages
	for i := 0; i < 10; i++ {
		message := &sarama.ProducerMessage{
			Topic: topic,
			Value: sarama.StringEncoder(fmt.Sprintf("Message %d", i)),
		}
		partition, offset, err := producer.SendMessage(message)
		if err != nil {
			log.Printf("Failed to produce message: %v", err)
		} else {
			log.Printf("Produced message to topic %s, partition %d, offset %d", topic, partition, offset)
		}
	}

	// Wait for interrupt signal to exit
	<-sigchan
	log.Println("Interrupt signal received, shutting down...")
}
