# Case Summary

**Incident Start:** 10/5/2024, 12:00:00 AM  
**Incident End:** 10/16/2024, 4:35:26 PM  
**Case Lead:** Brian Brandson  

## Scope
- Systems affected: `NR5A-MACHINE`, `QDPG-DESKTOP`
- Users affected: Anderson Snooper, Arrack Bobama
- Business impact: Compromised 2 user accounts, 2 hosts, exploited AI system for confidential information gathering

## Timeline (high-level)
- [ ] 10/5/2024, 12:00:00 AM - Possible reconnaissance phase observed
- [ ] 10/7/2024, 10:07:45 AM - Attacker sent phishing email to multiple employees.
- [ ] 10/7/2024, 10:46:47 AM - Credential harvest on fake portal.
- [ ] 10/7/2024, 3:46:45 PM - Successful login to Anderson's email account with stolen credentials
- [ ] 10/8/2024, 12:52:34 PM - Attacker contacted Barry Schmelly using Anderson's email. 
- [ ] 10/15/2024, 4:13:58 PM - Attacker located AI system 
- [ ] 10/15/2024, 4:17:49 PM - Attacker got information, related to voting machines (vendor and who can contact).
- [ ] 10/15/2024 after work hours - Vishing attack against company helpdesk. 
- [ ] 10/16/2024, 12:00:00 AM - Attacker logged in to Arrack Bobama's machine. 
- [ ] 10/16/2024, 4:35:26 PM - Attacker contacted voting machines vendor. 

## Key Findings
- Successful phishing attack against Anderson
- Successful credential harvesting from Anderson
- Attacker accessed Anderson's email account
- AI system gave information about voting machines vendor and who can contact them
- Successful vishing attack against helpdesk to reset Arrack Bobama's password
- Attacker accessed Arrack's machine and contacted vendor using Arrack's email address
- No telemetry supports compromise of air-gapped voting machines; attacker activity impacted user accounts/endpoints only.

## Confirmed Hypotheses
- H-001 - Reconnaissance phase
- H-002 - Attackers intentions is election interference. Most likely by tampering voting machines.
- H-003 - Temp Election Support Staff Lead's account compromised via credential harvesting on `https://valdoriavotesgov.com/login`
- H-004 - Attacker's target - AI system that could lead to accessing voting machines
- H-006 - Attacker contacts vendor by email through Arrack Bobama's machine. 

## Recommendations
- Short-term: 
	- Isolate machines: `NR5A-MACHINE`, `QDPG-DESKTOP`
	- Temporary disable users: Anderson Snooper, Arrack Bobama
	- Change passwords of compromised users
	- Enable MFA
	- Block IPs, domains, email addresses:
		- `55.49.227.170`
		- `214.85.104.248`
		- `157.100.244.104`
		- `valdoriavotesgov.com`
		- `new-hire-verification@protonmail.com`
- Long-term:
	- Implement security policy for MFA usage
	- Employee training to identify phishing attempts
	- Implement railguards for AI system to not give confidential information about vendors and employees