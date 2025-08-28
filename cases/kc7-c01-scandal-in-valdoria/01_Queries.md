### What is the Editorial Intern's name?
```
Employees
| where role == "Editorial Intern"
```
---
### What's Clark Kent email address?
```
Employees
| where name == "Clark Kent"
```
### How many total emails has Clark Kent received?
```
Email
| where recipient == "clark_kent@valdoriantimes.news"
```
---
### What was the subject line of this email?
```
Email
| where recipient == "clark_kent@valdoriantimes.news"
| where timestamp between (datetime("2024-01-31T00:00:00") .. datetime("2024-01-31T23:59:59"))
```
---
### What is Sonia's job role? (also information like email address, IP, hostname, etc.)
```
Employees
| where name == "Sonia Gose"
```
---
### What email address was used to send this email?
```
Email
| where sender == "newspaper_jobs@gmail.com" and recipient == "sonia_gose@valdoriantimes.news"
```
---
### Check if Sonia clicked the link
```
OutboundNetworkEvents
| where src_ip == "10.10.0.3"
| where url contains "promotionrecruit.com"
```
---
### When did the downloaded docx file first show up on Sonia's machine?
```
FileCreationEvents
| where hostname == "UL0M-MACHINE"
| where filename == "Valdorian_Times_Editorial_Offer_Letter.docx"
```
---
### What is the name of the file (.ps1) that was written to disk immediately after the docx was downloaded?
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
---
### How many Process Events are there related to this PowerShell script on Sonia's machine?
```
ProcessEvents
| where process_commandline contains "hacktivist_manifesto.ps1"
| where hostname == "UL0M-MACHINE"
```
---
### What six-letter command did the attackers run to figure out which user they are logged on as on the computer?
```
ProcessEvents
| where parent_process_name == "cmd.exe" and process_name == "cmd.exe"
| where hostname == "UL0M-MACHINE"
```
---
### How many total emails were sent by this email sender (`valdorias_best_recruiter@gmail.com`) to users at The Valdorian Times?
```
Email
| where sender == "valdorias_best_recruiter@gmail.com"
| count 
```
---
### When did `valdorias_best_recruiter@gmail.com` send an email to Ronnie McLovin?
```
Email
| where sender == "valdorias_best_recruiter@gmail.com" and recipient == "ronnie_mclovin@valdoriantimes.news"
```
---
### When did Ronnie click on the link in the email from `valdorias_best_recruiter@gmail.com`?
```
let ronnies_ip =
Employees
| where name == "Ronnie McLovin"
| distinct ip_addr;
OutboundNetworkEvents
| where src_ip in (ronnies_ip) // 10.10.0.19
| where url contains "promotionrecruit.org"
```
---
### When was this docx file downloaded?
```
let ronnies_host =
Employees
| where name == "Ronnie McLovin"
| distinct hostname;
FileCreationEvents
| where filename == "Editorial_J0b_Openings_2024.docx"
| where hostname in (ronnies_host) // A37A-DESKTOP
```
---
### When was the .ps1 file dropped to Ronnie's machine?
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
---
### What IP address was used with plink on Ronnie's machine?
```
ProcessEvents
| where hostname == "A37A-DESKTOP"
| where process_commandline contains "plink.exe"
```
---
### How many discovery commands were run on Ronnie's machine?
```
ProcessEvents
| where hostname == "A37A-DESKTOP"
| where parent_process_name == "cmd.exe" and process_name == "cmd.exe"
```
---
### What is the full URL fakestory.docx was downloaded from? (+ Ronnie's IP address)
```
let ronnies_ip =
Employees
| where name == "Ronnie McLovin"
| distinct ip_addr;
OutboundNetworkEvents
| where src_ip in (ronnies_ip)
| where url contains "fakestory.docx"
```
---
### What is the sha256 hash of fakestory.docx on Ronnie's machine?
```
FileCreationEvents
| where hostname == "A37A-DESKTOP"
| where filename == "fakestory.docx"
```
---
### What is the new path for the document?
```
ProcessEvents
| where hostname == "A37A-DESKTOP"
| where process_commandline contains "fakestory.docx"
```

---
### When was OpEdFinal_to_print.docx emailed from Ronnie's account to Clark Kent?
```
Email
| where sender == "ronnie_mclovin@valdoriantimes.news" and recipient == "clark_kent@valdoriantimes.news"
| where link contains "OpEdFinal_to_print.docx"
```

---
### How many total commands were run in this timeframe?
```
let ronnies_host =
Employees
| where name == "Ronnie McLovin"
| distinct hostname;
ProcessEvents
| where timestamp between (datetime(2024-01-21 07:00:00) .. datetime(2024-01-21 12:00:00))
| where hostname in (ronnies_host)
```

---
### What is the name of the .7z file that contains the stolen memes?
```
ProcessEvents
| where hostname == "A37A-DESKTOP"
| where process_commandline contains ".7z"
```
---
### Was data stolen from any other devices and uploaded to hirejob.com?
```
ProcessEvents
| where process_commandline contains "https://hirejob.com/exfil_processor/upload.php"
```