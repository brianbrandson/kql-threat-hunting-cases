# Indicators of Compromise (IOC)

| Type          | Value                                  | First seen (UTC)       | Source Evidence                                                       | Confidence | Status    | Notes                                        |
| ------------- | -------------------------------------- | ---------------------- | --------------------------------------------------------------------- | ---------- | --------- | -------------------------------------------- |
| IP            | `55.49.227.170`                        |                        | [E-001](evidence/E-001_Hacking_group_poster.md)                       | High       | Lead      | IP of the hacker can be fake.                |
| Domain        | `valdoriavotesgov.com`                 | 10/4/2024, 1:38:24 PM  | [E-002](evidence/E-002_Hacker_IP_resolve.md)                          | High       | Malicious | Phishing portal                              |
| IP            | `214.85.104.248`                       |                        | [E-002](evidence/E-002_Hacker_IP_resolve.md)                          | High       | Lead      | Confirmed hacker's IP                        |
| IP            | `157.100.244.104`                      |                        | [E-002](evidence/E-002_Hacker_IP_resolve.md)                          | High       | Lead      | Confirmed hacker's IP                        |
| Email address | `new-hire-verification@protonmail.com` | 10/7/2024, 10:07:45 AM | [E-012](E-012_Phishing_email.md)                                      | High       | Lead      | Sent fake login portal to multiple employees |
| URL           | `https://valdoriavotesgov.com/login`   | 10/7/2024, 10:46:45 AM | [E-004](evidence/E-004_Employee_credential_harvest_on_fake_portal.md) | High       | Malicious | Fake login portal                            |
