# Timeline
## 10/5/2024, 12:00:00 AM
**Action:** Possible reconnaissance phase observed  
**Tool/Command:**  
```
let ips =
PassiveDns
| where domain == "valdoriavotesgov.com"
| distinct ip;
InboundNetworkEvents
| where src_ip in (ips)
| distinct timestamp, src_ip, url
```
**Observation (facts):** `valdoriavotesgov.com` resolves to hacker's IP 55.49.227.170 that was found in poster. Two additional IPs were found that resolves to same domain.  
**Evidence IDs:** [E-001](evidence/E-001_Hacking_group_poster.md), [E-002](evidence/E-002_Hacker_IP_resolve.md), [E-003](evidence/E-003_Possible_Reconnaissance_Phase.md)
## 10/7/2024, 10:07:45 AM
**Action:** Attacker sent phishing email to multiple employees.  
**Tool/Command:**  
```
Email
| where links contains "valdoriavotesgov.com"
| project-away reply_to, verdict
```
**Observation (facts):** Attacker used email address `new-hire-verification@protonmail.com`.  
**Evidence IDs:** [E-012](E-012_Phishing_email.md)  
**Next Step:** Check if any of employees clicked link.
## 10/7/2024, 10:46:47 AM
**Action:** Credential harvest on fake portal  
**Tool/Command:** 
```
OutboundNetworkEvents
| where url contains "valdoriavotesgov.com"
```
**Observation (facts):** Anderson Snooper entered credentials to `https://valdoriavotesgov.com/login`  
**Interpretation (analysis):** Likely that account was compromised via phishing.  
**Evidence IDs:** [E-004](evidence/E-004_Employee_credential_harvest_on_fake_portal.md)  
**Next Step:** Check successful login attempts from malicious IPs to Anderson's account  
## 10/7/2024, 3:46:45 PM
**Action:** Successful login to Anderson's email account with stolen credentials  
**Tool/Command:**  
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
**Observation (facts):** Attacker logged in to Anderson's email account from IP `157.100.244.104`  
**Evidence IDs:** [E-005](evidence/E-005_Successful_login_to_Andersons_email_account.md)  
**Next Step:** Check if any emails were sent from Anderson's email address.  
## 10/8/2024, 12:52:34 PM
**Action:** Attacker contacted Barry Schmelly using Anderson's email.  
**Tool/Command:** 
```
Email
| where (sender == "anderson_snooper@valdoriavotes.gov" and recipient == "barry_schmelly@valdoriavotes.gov") or (sender == "barry_schmelly@valdoriavotes.gov" and recipient == "anderson_snooper@valdoriavotes.gov")
| where timestamp >= datetime(2024-10-07 15:46:45)
| project-away reply_to, verdict
```
**Observation (facts):** Attacker is interested in accessing voting machines. Hypothesis H-002 confirmed.  
**Interpretation (analysis):** Barry is also temp employee, so he does not have access to AI system that is related to voting machines.  
**Evidence IDs:** [E-006](evidence/E-006_Conversation_between_attacker_and_Barry_Shmelly.md)  
**Next Step:** Find evidence of attacker trying to locate AI system  
## 10/15/2024, 4:13:58 PM
**Action:** Attacker located AI system  
**Tool/Command:**  
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
**Observation (facts):** AI system domain: `https://elections-chatbot.valdoriavotes.gov`  
**Interpretation (analysis):** Attacker created prompts with questions about voting machines.  
**Evidence IDs:** [E-007](evidence/E-007_Attacker_located_AI_system.md), [E-008](evidence/E-008_AI_chat_with_attacker.md)  
**Next Step:** Get full conversation with AI system.  
## 10/15/2024, 4:17:49 PM
**Action:** Attacker got information, related to voting machines (vendor and who can contact).  
**Tool/Command:**  
```
// To see what table is made of
AIPrompts
| take 10

// To find conversation ID
AIPrompts
| where prompt contains "How do I access the voting machines"
```
**Observation (facts):**  Vendor "Dominos Voting Systems". Who can contact them: Election Commissioner Arrack Bobama.  
**Interpretation (analysis):** Attacker might try to contact the vendor to attempt onsite access.  
**Evidence IDs:** [E-008](evidence/E-008_AI_chat_with_attacker.md)  
**Next Step:** Contact Arrack Bobama to advice to be cautious of any suspicious emails.  
## 10/15/2024 after work hours
**Action:** Vishing attack against company helpdesk.  
**Observation (facts):** Attacker convinced helpdesk employee to reset Arrack Bobama's password and give temporary one.  
**Evidence IDs:** [E-009](evidence/E-009_Helpdesk_reseted_Arracks_password.md)  
**Next Step:** Check if Arrack has MFA enabled. If not, check authentication logs to see if attacker made login attempts.  
## 10/16/2024, 12:00:00 AM
**Action:** Attacker logged in to Arrack Bobama's machine.  
**Tool/Command:**  
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
**Observation (facts):** Successful login to `QDPG-DESKTOP`from IP `214.85.104.248`  
**Interpretation (analysis):** Attacker used temporary password to access Arrack Bobama's machine to possibly contact with voting machines vendor via email.  
**Evidence IDs:** [E-010](evidence/E-010_Successful_login_to_Bobamas_machine.md)  
**Next Step:** Check emails to see if emails were sent to vendor.  
## 10/16/2024, 4:35:26 PM
**Action:** Attacker contacted voting machines vendor.  
**Tool/Command:**  
```
// To find out vendor's email address and when did attacker contacted them
let bobamas_email =
Employees
| where name == "Arrack Bobama"
| distinct email_addr;
Email
| where sender in (bobamas_email)
| where recipient contains "dominos"
| where timestamp >= datetime(2024-10-15 12:00:00)

// To see full conversation between attacker and vendor
let bobamas_email =
Employees
| where name == "Arrack Bobama"
| distinct email_addr;
Email
| where (sender in (bobamas_email) and recipient == "help@dominosvotingsystems.com") or (sender == "help@dominosvotingsystems.com" and recipient in (bobamas_email))
| where timestamp >= datetime(2024-10-15 12:00:00)
| project-away reply_to, verdict
```
**Observation (facts):** Voting machines are not connected to internet. Access can be done strictly on-site. Vendor sent voting machine's guide.  
**Evidence IDs:** [E-011](evidence/E-011_Email_transcript_between_attacker_and_vendor.md)  
**Next Step:** Contact company's board and vendor. Initiate voting machines checks and precautions.