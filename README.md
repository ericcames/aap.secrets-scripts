Ansible Automation Platform (AAP) secrets to scripts.
=========

This repository will show you how pass secrets to a script using a custom credential in AAP.
    First we will have to create custom credential type.
    Then we will use the credential type to create a credential that holds our secrets.
    Then we will relate that credential to AAP job template.

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
