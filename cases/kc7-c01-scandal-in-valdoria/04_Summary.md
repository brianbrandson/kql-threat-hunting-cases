# Case Summary – A scandal in Valdoria

**Incident Start:**  1/5/2024, 9:42:05 AM  
**Incident End:** 2/1/2024, 2:14:32 AM  
**Case Lead:**  Brian Brandson

## Scope
- **Systems affected**: A37A-DESKTOP, UL0M-MACHINE  
- **Users affected**: Sonia Gose, Ronnie McLovin  
- **Business impact**: Successful phishing attack, fake article released, adversary got access to two company machines, data theft.

## Timeline (high-level)
- [ ] 1/5/2024, 9:42:05 AM - Sonia Gose got suspicious email
- [ ] 1/5/2024, 10:23:17 AM - Sonia clicked link from phishing email
- [ ] 1/5/2024, 10:24:04 AM - Malicious file was downloaded to Sonia's machine
- [ ] 1/5/2024, 10:24:32 AM - File was written to disk after docx was downloaded
- [ ] 1/5/2024, 11:22:44 AM - Scheduled task was created with ExecutionPolicy Bypass
- [ ] 1/5/2024, 11:55:22 AM - PowerShell script executed
- [ ] 1/6/2024, 2:39:35 AM - Host "UL0M-MACHINE" connected to C2 server
- [ ] 1/10/2024, 8:48:16 AM - Intern Ronnie got email from suspicious email 
- [ ] 1/10/2024, 8:55:07 AM - Ronnie clicked a link on email
- [ ] 1/10/2024, 8:55:17 AM - Suspicious file was downloaded to Ronnie's machine
- [ ] 1/10/2024, 8:55:50 AM - File "hacktivist_manifesto.ps1" was written to disk after docx was downloaded
- [ ] 1/11/2024, 3:08:12 AM - Remote connection initiated to C2 server from Ronnie's machine
- [ ] 1/31/2024, 9:47:51 AM - Weird file `fakestory.docx` was downloaded to Ronnie's machine
- [ ] 1/31/2024, 10:26:20 AM - Attacker moved and renamed file
- [ ] 1/31/2024, 11:11:12 AM - Clark Kent got email with fake final article
- [ ] 1/31/2024, 11:44:58 AM - The attackers ran commands to archive data from Ronnie's machine.
- [ ] 2/1/2024, 2:14:32 AM - Archived files exfiltrated
## Key Findings
- Successful phishing attack
- Two company machines remote connected to adversary's C2 server
- Adversary sent fake print from infected machine using intern's email address
- Exfiltrated data from one of the machines

## Confirmed Hypotheses
- H-001 - Successful phishing attack on Sonia Gose
- H-002 - Malicious file downloaded which created scheduled
- H-003 - Successful phishing attack on Ronnie McLovin
- H-004 - Malicious file downloaded which created scheduled
- H-005 - Adversary downloaded file "fakestory.docx" to Ronnie's machine, renamed and moved to another location. Then sent it to Clark Kent as confirmed, final text for printing.
- H-006 - Adversary exfiltrated documents and meme files from Ronnie's

## Recommendations
- Short-term:  
	- Isolate hosts: **A37A-DESKTOP (10.10.0.19)** and **UL0M-MACHINE (10.10.0.3)**
	- Disable users: **romclovin** and **sogose**
	- Block on firewall: `promotionrecruit.com`, `136.130.190.181`, `168.57.191.100`, `hirejob.com`
- Long-term: 
	- Employee training to identify phishing attempts
	- Block/alert on `-ExecutionPolicy Bypass`
	- Create a detection for `plink.exe` invocation, especially with `-R 3389:localhost:3389`; outbound SSH/3389 egress should be deny-by-default with exceptions