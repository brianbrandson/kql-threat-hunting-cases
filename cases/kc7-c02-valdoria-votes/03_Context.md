# Case Context

## Users
| User             | Username   | Role                                   | Email address                        | Notes                                                                              |
| ---------------- | ---------- | -------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------- |
| Hilary Binton    | hibinton   | Deputy Commissioner                    | `hilary_binton@valdoriavotes.gov`    |                                                                                    |
| Barry Schmelly   | baschmelly | Temp Election Support Staff Supervisor | `barry_schmelly@valdoriavotes.gov`   | Contacted by attacker using Anderson's email                                       |
| Anderson Snooper | ansnooper  | Temp Election Support Staff Lead       | `anderson_snooper@valdoriavotes.gov` | Entered login credentials on fake portal. Has no MFA enabled                       |
| Arrack Bobama    | arbobama   | Election Commissioner                  | `arrack_bobama@valdoriavotes.gov`    | Only one who communicates with vendor "Dominos Voting Systems". Has no MFA enabled |

---

## Hosts
| Hostname     | IP Address | Owner            | OS / Version | Notes                  |
| ------------ | ---------- | ---------------- | ------------ | ---------------------- |
| FDA2-DESKTOP | 10.10.0.30 | Hilary Binton    |              |                        |
| GCH3-DESKTOP | 10.10.0.12 | Barry Schmelly   |              |                        |
| NR5A-MACHINE | 10.10.0.4  | Anderson Snooper |              | Attacker gained access |
| QDPG-DESKTOP | 10.10.0.13 | Arrack Bobama    |              | Attacker gained access |

---

## Applications / Services
| Service         | Hostname / Domain                             | Port/Protocol | Notes                                                                     |
| --------------- | --------------------------------------------- | ------------- | ------------------------------------------------------------------------- |
| AI system       | `https://elections-chatbot.valdoriavotes.gov` |               |                                                                           |
| Voting machines | -                                             | -             | Vendor: Dominos Voting Systems<br>Machines are not connected to internet. |
