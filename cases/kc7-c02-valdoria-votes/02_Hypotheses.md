## H-001
**Statement:** Reconnaissance phase.  
**Supporting Evidence:** [E-003](evidence/E-003_Possible_Reconnaissance_Phase.md)  
**Confidence:** High  
**Status:** Confirmed  
**Notes:** Observed searches about employees at the Elections Board  

## H-002
**Statement:** The attacker’s intention is election interference. Most likely by tampering voting machines.  
**Supporting Evidence:** [E-003](evidence/E-003_Possible_Reconnaissance_Phase.md), [E-006](evidence/E-006_Conversation_between_attacker_and_Barry_Shmelly.md)  
**Confidence:** High  
**Status:** Confirmed  
**Notes:**  
- From search queries attackers made and articles read we can assume this is their intentions.  
- Attacker contacted Barry Schmelly and questioned about possibilities to access voting machines.  

## H-003
**Statement:** Temp Election Support Staff Lead's account compromised via credential harvesting on `https://valdoriavotesgov.com/login`
**Supporting Evidence:** [E-004](evidence/E-004_Employee_credential_harvest_on_fake_portal.md)  
**Confidence:** High  
**Status:** Confirmed  
**Notes:** OutboundNetworkEvents events confirmed successful credential harvesting.

## H-004
**Statement:** Attacker's target - AI system that could lead to accessing voting machines
**Supporting Evidence:** [E-006](evidence/E-006_Conversation_between_attacker_and_Barry_Shmelly.md), [E-007](evidence/E-007_Attacker_located_AI_system.md)  
**Confidence:** Medium  
**Status:** Confirmed    
**Notes:**  Attacker located AI system.  

## H-005
**Statement:** Attacker's next target is Arrack Bobama. Possible spear-phishing attack.  
**Supporting Evidence:** [E-008](evidence/E-008_AI_chat_with_attacker.md), [E-009](evidence/E-009_Helpdesk_reseted_Arracks_password.md)  
**Confidence:** Medium  
**Status:** Refuted  
**Notes:** Attacker got password using vishing attack against company helpdesk.  

## H-006
**Statement:** Attacker contacts vendor by email through Arrack Bobama's machine.  
**Supporting Evidence:** [E-010](evidence/E-010_Successful_login_to_Bobamas_machine.md), [E-011](evidence/E-011_Email_transcript_between_attacker_and_vendor.md) 
**Confidence:** High  
**Status:** Confirmed  
**Notes:** Log confirm the contact with vendor.  

## H-007
**Statement:** Attacker compromise voting machines locally.  
**Supporting Evidence:** [E-011](evidence/E-011_Email_transcript_between_attacker_and_vendor.md)  
**Confidence:** Low  
**Status:** Refuted  
**Notes:** Vendor confirms on-site only; no telemetry of local compromise.  