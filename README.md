Ansible Automation Platform (AAP) secrets to scripts.
=========

This repository will show you how pass secrets to a script in a safe and secure way.

Secrets to localhost (AKA the execution environment)
=========

This method creates an environment variable on the execution environment that is used by the python script.

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
[Custom Credential playbook]( https://github.com/ericcames/aap.secrets-scripts/blob/main/playbooks/python_secrets_localhost.yml "Custom Credential playbook")

![alt text](https://github.com/ericcames/aap.secrets-scripts/blob/main/images/customcredentialtype.png "Credential Type")
![alt text](https://github.com/ericcames/aap.secrets-scripts/blob/main/images/customcredential.png "Credential")
![alt text](https://github.com/ericcames/aap.secrets-scripts/blob/main/images/template_credential.png "Template")

Secrets to a remotehost method 1
=========

Pass secrets from a vaulted file using
[vars_files playbook]( https://github.com/ericcames/aap.secrets-scripts/blob/main/playbooks/python_secrets_remotehost_method_1.yml "var_files playbook"). For this method to work you will need to create a vault credential in your AAP and relate it to your job template.

![alt text](https://github.com/ericcames/aap.secrets-scripts/blob/main/images/templatewithavault.png "Template with a vaulted credential")

Example vault contents
------------
```yaml
dynatrace_api_key: 123456_secrets_are_here
```

Secrets to a remotehost method 2
=========

Pass secret from an inbeded vault file using
[vars playbook]( https://github.com/ericcames/aap.secrets-scripts/blob/main/playbooks/python_secrets_remotehost_method_2.yml "vars playbook"). For this method to work you will need to create a vault credential in your AAP and relate it to your job template.

![alt text](https://github.com/ericcames/aap.secrets-scripts/blob/main/images/templatewithavault.png "Template with a vaulted credential")

Example vault contents
------------
```yaml
123456_secrets_are_here
```