# Advanced SIEM

## Overview

Advanced SIEM is a Security Information and Event Management platform built using FastAPI, Kafka, PostgreSQL, and React.

The platform collects security events, normalizes logs, performs event correlation, detects brute-force attacks, enriches alerts with threat intelligence, maps detections to MITRE ATT&CK techniques, and provides an analyst investigation dashboard.

## Features

* Event Collection API
* Event Normalization
* Kafka Streaming Pipeline
* Event Correlation Engine
* Brute Force Detection
* PostgreSQL Alert Storage
* Alert Investigation Dashboard
* Alert Status Management
* Threat Intelligence Enrichment
* MITRE ATT&CK Mapping

## Architecture

Windows Events → FastAPI Collector → Kafka → Consumer → Correlation Engine → PostgreSQL → React Dashboard

## Technology Stack

Backend:

* Python
* FastAPI
* Kafka
* PostgreSQL

Frontend:

* React

Infrastructure:

* Docker
* Docker Compose

## Detection Logic

Brute-force detection is triggered when multiple failed logins are followed by a successful login from the same user, IP address, and host.

## Threat Intelligence Enrichment

Alerts are enriched using local threat intelligence feeds.

Example:

* Reputation
* Confidence Score
* Category
* Provider

## MITRE ATT&CK Mapping

Brute Force Login → T1110 (Brute Force)

Tactic:

* Credential Access

## Future Enhancements

* AbuseIPDB Integration
* VirusTotal Integration
* Additional Detection Rules
* MITRE ATT&CK Coverage Expansion
* Containerized Deployment
