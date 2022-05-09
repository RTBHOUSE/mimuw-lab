# Stream processing part 2 - Kafka Streams

In this laboratory you will learn how to process streams using Kafka
Streams. If you are stuck, ask the instructor for help.

## 1. Run demo app
Open Kafka Streams *[documentation webpage](https://kafka.apache.org/31/documentation/streams/quickstart)*.
Read the entire 'RUN DEMO APP' section and run the examples.

## 2. Write your first app
Follow *[this tutorial](https://kafka.apache.org/31/documentation/streams/tutorial)*
to build your first stream processing app. Make sure that the examples work on your computer.

Note: when running maven command `mvn clean package` you may get a following error:
```
[ERROR] COMPILATION ERROR :
[INFO] -------------------------------------------------------------
[ERROR] /home/wrybak/Desktop/streams_labs/streams.examples/src/main/java/myapps/WordCount.java:[1]
	/*
	^
The type java.lang.Object cannot be resolved. It is indirectly referenced from required .class files
[ERROR] /home/wrybak/Desktop/streams_labs/streams.examples/src/main/java/myapps/WordCount.java:[1]
	/*
	^
The type java.lang.Exception cannot be resolved. It is indirectly referenced from required .class files
[ERROR] /home/wrybak/Desktop/streams_labs/streams.examples/src/main/java/myapps/WordCount.java:[1]
	/*
	^
...
```

This probably means that you don't have `jdt` installed. To use `javac` instead, change line
76 of `pom.xml` from `<compilerId>jdt</compilerId>` to `<compilerId>javac</compilerId>`.

## 3. More examples
Explore more *[examples](https://github.com/confluentinc/kafka-streams-examples/tree/7.0.0-post/src/main/java/io/confluent/examples/streams)*.
With a bit of luck you may find some inspiration for the final assignment.
