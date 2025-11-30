#!/bin/bash

curl -X POST http://localhost:5000/siem-webhook \
     -H "Content-Type: application/json" \
     -d '{
           "id": "case-12345",
           "message": "Failed password for root from 192.168.1.55 port 22 ssh2",
           "source_ip": "192.168.1.55",
           "severity": "high",
           "rule": {"name": "SSH Brute Force"}
         }'