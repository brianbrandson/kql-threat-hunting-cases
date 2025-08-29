## Scenario Overview (KC7 simulated incident)

On the eve of Valdoria’s election, The Valdorian Times published a sensational corruption piece about candidate Luffy that the editor-in-chief hadn’t approved. The newsroom went into crisis, legal pressure mounted, and I was brought in as the incident responder to determine **how a falsified article made it to publication**. Before digging in, I was asked to pull and analyze the company’s security audit logs stored in **Azure Data Explorer (ADX)** using **KQL**—pivoting across email, web, authentication, and host activity to reconstruct the attack, validate hypotheses, and recommend defenses.

*Scenario dataset by [KC7](https://kc7cyber.com/); investigation, queries, and reporting by me.*

**Reproduce:** Run the queries in `01_Queries.md` in the order referenced by `00_Timeline.md` against the KC7 Case 01 dataset.