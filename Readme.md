# Overview

This tool is not official, this was created by the PH Cloud One Support team for better customer support in migration cases. This project is provided on an ‘AS IS’ and ‘WHEN AVAILABLE’ basis. If there are any issue found with the tool, we might not be able to provide immidiate fix for it. But please do provide some feedback on it, so we can improve upon it when possible.

## Purpose
The tool is intended for migrating policies and tasks from an existing DS Setup (On Premise, Cloud One Workload Security, AWS/Azure) to a newly deployed destination environment (On Premise, Cloud One Workload Security, AWS/Azure). 

* The tool aims to help customers who wants to migrate their existing configurations (policies, scheduled tasks, event-based tasks) to another Deep Security Manager or Cloud One - Workload Security.
* The tool consists of several API calls which are needed to get the necessary configurations and import them to the desired DSM/WS by also using API calls.
* Python was the language used in this application.

## Scopes

1. Policies, Event-Based Tasks (EBT) and Scheduled Tasks (ST) can be migrated.
2. The tool uses RESTful API so it only works for Deep Security Manager 11.1 and above.
3. Anti-Malware Custom Configurations can be migrated if applied to the policy that the tool will migrate.

## Limitation
1. The tool will not work on Deep Security Managers lower than 11.1 since we are using RESTful API
2. Proxy Configuration for Modules cannot be migrated due to RESTful API limitations (no API call for creating the Proxy Configuration). Currently, we are trying to request this one to be available on RESTful.
3. Shared rulesets are cannot be migrated.
4. This tool will overwrite all of the following configuration on the tenant where you wanted to transfer your policy. This is not a problem for a new Cloud One user but might be an issue for other users.
  * IP Lists
  * Mac Lists
  * Port Lists
  * Firewall Stateful Configuration
  * Schedules
  * Contexts

## Known Issues

* All migrated policies will be under the base policy if they have a parent policy. If not, they will be migrated as it is.
* Scheduled Task migration is currently not working.

## Contributing
Pull requests for bug fixes are welcome.