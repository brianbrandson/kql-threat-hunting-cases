# Queries
## Section 1
### What is the name of the Deputy Commissioner?
```
Employees
| where role == "Deputy Commissioner"
```
---

### What is Dora Thomas' role?
```
Employees
| where name == "Dora Thomas"
```
---

### What is this (temporary) supervisor's name
```
Employees
| where role contains "supervisor"
| distinct role, name
```
---

### What is Barry Schmelly's IP address?
```
Employees
| where name == "Barry Schmelly"
```
---

### How many emails did Barry Schmelly receive?
```
let barrys_email =
Employees
| where name == "Barry Schmelly"
| distinct email_addr;
Email
| where recipient in (barrys_email)
| count
```
---

### How many distinct commands were run on Barry Schmelly's machine?
```
let barrys_host =
Employees
| where name == "Barry Schmelly"
| distinct hostname;
ProcessEvents
| where hostname in (barrys_host)
| distinct process_commandline
| count
```
---

### How many distinct URLs did employees with the first name William visit?
```
let wills_ip =
Employees
| where name has "William"
| distinct ip_addr;
OutboundNetworkEvents
| where src_ip  in (wills_ip)
| distinct url
| count
```
---

### How many authentication attempts did we see to the accounts of employees with the first name William?
```
let wills_username =
Employees
| where name has "William"
| distinct username;
AuthenticationEvents
| where username in (wills_username)
| count
```
---


## Section 3
### Is there any evidence of traffic from this IP address (found in poster) to our network?
```
InboundNetworkEvents
| where src_ip == "55.49.227.170"
```
---

### How many domains resolved to the IP 55.49.**.***?
```
PassiveDns
| where ip == "55.49.227.170"
```
---

### How many IP addresses did the fraudulent Valdoria government domain resolve to?
```
PassiveDns
| where domain == "valdoriavotesgov.com"
```
---

### How many requests do we see to our network from those IPs?
```
let ips =
PassiveDns
| where domain == "valdoriavotesgov.com"
| distinct ip;
InboundNetworkEvents
| where src_ip in (ips)
| count
```
---

### What group were they specifically interested in?
```
let ips =
PassiveDns
| where domain == "valdoriavotesgov.com"
| distinct ip;
InboundNetworkEvents
| where src_ip in (ips)
| distinct timestamp, src_ip, url
```
---

### Let’s check if there’s any traffic to it—has any of our employees visited that domain for any reason?
```
OutboundNetworkEvents
| where url contains "valdoriavotesgov.com"
```
---

### When did someone first browse to that domain?
```
OutboundNetworkEvents
| where url contains "valdoriavotesgov.com"
```
---

### What is the name of the employee who entered their credentials?
```
Employees
| where ip_addr == "10.10.0.4"
```
---

### When did the threat actor login to Snooper's account?
```
let ips =
PassiveDns
| where domain == "valdoriavotesgov.com"
| distinct ip;
AuthenticationEvents
| where username == "ansnooper"
| where src_ip in (ips)
| where timestamp >= datetime(2024-10-07 10:46:47)
```
---

### What is the email address of the person he was conversing with?
```
Email
| where sender == "anderson_snooper@valdoriavotes.gov"
| where timestamp >= datetime(2024-10-07 15:46:45)
```
---

### What is Schmelly's job role?
```
Employees
| where email_addr == "barry_schmelly@valdoriavotes.gov"
```
---

### "Snooper" was observed asking Schmelly how one might gain access to what devices?
```
Email
| where (sender == "anderson_snooper@valdoriavotes.gov" and recipient == "barry_schmelly@valdoriavotes.gov") or (sender == "barry_schmelly@valdoriavotes.gov" and recipient == "anderson_snooper@valdoriavotes.gov")
| where timestamp >= datetime(2024-10-07 15:46:45)
| project-away reply_to, verdict
```
---

### What term appeared at the end of each url that Snooper guessed?
```
let snoopers_ip =
Employees
| where name == "Anderson Snooper"
| distinct ip_addr;
InboundNetworkEvents
| where src_ip in (snoopers_ip)
| where timestamp >= datetime(2024-10-08 14:40:40)
| where url contains "ai"
```
---

### What was the basketball player-related subdomain that Snooper guessed?
```
let snoopers_ip =
Employees
| where name == "Anderson Snooper"
| distinct ip_addr;
InboundNetworkEvents
| where src_ip in (snoopers_ip)
| where timestamp >= datetime(2024-10-08 14:40:40)
| where url contains "gpt"
```
---

### What was the first subdomain "Snooper" guessed that returned a 200 status code?
```
let snoopers_ip =
Employees
| where name == "Anderson Snooper"
| distinct ip_addr;
InboundNetworkEvents
| where src_ip in (snoopers_ip)
| where timestamp >= datetime(2024-10-08 14:40:40)
| where url contains "gpt"
| where status_code == "200"
```
---

### Which conversation_id is associated with the question about voting machines?
```
// To see what table is made of
AIPrompts
| take 10

// To find conversation ID
AIPrompts
| where prompt contains "How do I access the voting machines"
```
---

### The AI bot told the threat actor to bring a _ and a banana.
```
AIPrompts
| where conversation_id == "94bd6162-1323-402d-bccd-8fceaee5f230"
```
---

### What is the name of the employee with that job role?
```
Employees
| where role == "Election Commissioner"
```
---

### When did they log in to Bobama's account?
```
let arracks_username =
Employees
| where name == "Arrack Bobama"
| distinct username;
let attackers_ips =
PassiveDns
| where domain == "valdoriavotesgov.com"
| distinct ip;
AuthenticationEvents
| where username in (arracks_username)
| where src_ip in (attackers_ips)
| where timestamp >= datetime(2024-10-15)
```
---

### What email address did they send this email to?
```
let bobamas_email =
Employees
| where name == "Arrack Bobama"
| distinct email_addr;
Email
| where sender in (bobamas_email)
| where recipient contains "dominos"
| where timestamp >= datetime(2024-10-15 12:00:00)
```
---

### What PDF did the threat actors receive that might be useful to them later?
```
let bobamas_email =
Employees
| where name == "Arrack Bobama"
| distinct email_addr;
Email
| where (sender in (bobamas_email) and recipient == "help@dominosvotingsystems.com") or (sender == "help@dominosvotingsystems.com" and recipient in (bobamas_email))
| where timestamp >= datetime(2024-10-15 12:00:00)
| project-away reply_to, verdict, links
```