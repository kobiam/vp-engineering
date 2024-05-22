# Kafka producer API

## gradle

start the app using `gradle init`

```sh
Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4] 2

Select implementation language:
  1: C++
  2: Groovy
  3: Java
  4: Kotlin
  5: Scala
  6: Swift
Enter selection (default: Java) [1..6] 3

Split functionality across multiple subprojects?:
  1: no - only one application project
  2: yes - application and library projects
Enter selection (default: no - only one application project) [1..2] 

Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Groovy) [1..2] 1

Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no] 
Select test framework:
  1: JUnit 4
  2: TestNG
  3: Spock
  4: JUnit Jupiter
Enter selection (default: JUnit Jupiter) [1..4] 

Project name (default: producer-api-example): 
Source package (default: producer.api.example): 

> Task :init
Get more help with your project: https://docs.gradle.org/7.4.2/samples/sample_building_java_applications.html

BUILD SUCCESSFUL in 56s
2 actionable tasks: 2 executed
```

## build the project

```sh
./gradlew build
```

or

```sh
./gradlew clean build
./gradlew --refresh-dependencies
./gradlew clean build -i
```

## check the artifact

```sh
jar tf app/build/libs/app.jar
```

## generate javadoc

```sh
./gradlew javadoc
```

## make the jar executable

add this to `build.gradle` and check `MANIFEST.MF` file

```config
jar {
  manifest {
    attributes 'Main-Class': application.mainClass
  }
}
```

## build the project again

```sh
./gradlew build
```

## run the jar

```sh
java -jar app/build/libs/app.jar
```

## links

links to kafka API producer client [HERE](https://kafka.apache.org/34/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html)

link to kafka API consumer client [HERE](https://kafka.apache.org/34/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html)
