Ansible Automation Platform (AAP) secrets to scripts.
=========

This repository will show you how pass secrets to a script in a safe and secure way.

Secrets to localhost (AKA the execution environment)
=========
AAP Credential Type configurations
------------
Input configuration
```yaml
fields:
  - id: DYNATRACE_API_KEY
    type: string
    label: Dynatrace API Token
    secret: true
  - id: freshservice_api_key
    type: string
    label: Fresh Service API Token
    secret: true
required:
  - DYNATRACE_API_KEY
```
Injector configuration
```yaml
env:
  DYNATRACE_API_KEY: '{{ DYNATRACE_API_KEY }}'
  freshservice_api_key: '{{ freshservice_api_key }}'
```
Secrets to a remotehost method 1
=========

Secrets to a remotehost method 2
=========