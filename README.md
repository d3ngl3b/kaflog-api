<a name="top"></a>
[![Logging_API_Header](https://logging-api-documentation.s3.us-east-1.amazonaws.com/LoggingAPI_header.png)](https://social-network-documentation.s3.us-east-1.amazonaws.com/SN_HEADER.png)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)]()
[![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)]()
[![ApacheKafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)]()
[![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)]()
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)]()
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-FF9900?style=for-the-badge&logo=amazons3&logoColor=white)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-3069DE?style=for-the-badge&logo=kubernetes&logoColor=white)]()



## Table of Contents
- [About](#-about)
- [What's New](#-whats-new)
- [K8s cluster](#-kubernetes-cluster)
- [Usage-example](#-usage-example)
- [Contacts](#-contacts)

## 🚀 About

This project is a **Logging API** service built with **Python**, acting as a wrapper around Apache Kafka to provide scalable and modular log processing through pluggable appenders such as **PostgreSQL** and **Amazon S3**.

### Main Features

* Receive and process structured log data via a REST API built with **FastAPI**
* Publish logs asynchronously to **Apache Kafka** for reliable message queuing
* Route and store logs through modular **appenders** (currently PostgreSQL and Amazon S3)
* Ensure fault-tolerant, scalable, and decoupled logging pipelines
* Easily extendable with additional appenders or processing backends

### Technologies Used

* **Backend:** FastAPI with Apache Kafka for asynchronous message streaming
* **Database Appender:** PostgreSQL implemented with **SQLAlchemy** ORM
* **Cloud Storage Appender:** AWS S3 integration via **Boto3**
* **Containerization:** All components (API, Appenders, Nginx) are packaged using Docker and managed by **Kubernetes** under **Minikube**.
* **Architecture:** Modular appender system allowing simple integration of new storage or processing backends

This setup provides a fast, modular, and scalable logging infrastructure, combining **FastAPI’s performance** and **Kafka’s reliability** to ensure seamless data flow from ingestion to persistent storage across **PostgreSQL** and **S3** backends.

## ✨ What's New

### Version 1.0.0 (Latest)

This section will be regularly updated as new features and improvements are added to the project.  
Future updates may include additional functionality, performance enhancements.  
Check back here for the latest changes and development progress.
> **Migration Note**: This is the first version released.

## 📝 Kubernetes Cluster

This diagram provides a simplified overview of the AWS infrastructure and system architecture used in the application.

[![AWS_map](https://logging-api-documentation.s3.us-east-1.amazonaws.com/kaflogK8s.png)]()
*Figure 1: K8s resources diagram.*

## ⚙️ Usage Example

The following images illustrate a simple example of the system in action, demonstrating how log data flows from the FastAPI endpoint through Kafka and into the configured appenders.

[![API](https://logging-api-documentation.s3.us-east-1.amazonaws.com/api.png)]()
*Figure 2: API Swagger.*

[![Kafka](https://logging-api-documentation.s3.us-east-1.amazonaws.com/kafka.png)]()
*Figure 3: Kafka UI.*

[![Postgres](https://logging-api-documentation.s3.us-east-1.amazonaws.com/db.png)]()
*Figure 4: Postgres.*

[![S3](https://logging-api-documentation.s3.us-east-1.amazonaws.com/s3.png)]()
*Figure 4: Postgres.*

## 🗨️ Contacts

- **Email**:  gleb@adenisov.com.
- **LinkedIn**: [link to account.](https://www.linkedin.com/in/gleb-denisov-40b5472a4/)

[Back to top](#top)
