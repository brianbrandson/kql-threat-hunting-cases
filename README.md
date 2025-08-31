# KQL Threat Hunting Cases

Hands-on, case-based **KQL** investigations for blue-team threat hunting and incident response.  
Sources include **KC7** scenarios and my **homelab** data. Each case folder contains a timeline, queries, hypotheses, context, summary, and a normalized evidence catalog.

**Skills showcased:** KQL (Kusto), hunting → detection engineering, incident documentation, ATT&CK mapping, SOC workflows.

---

## Cases

| Case                            | Source | Focus                                                                                                                                                                          | Links                                                                                                     |
| ------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **C01 – A Scandal in Valdoria** | KC7    | Phishing → PowerShell (PS) → `plink` tunneling → data exfiltration                                                                                                             | [folder](cases/kc7-c01-scandal-in-valdoria/) · [queries](cases/kc7-c01-scandal-in-valdoria/01_Queries.md) |
| **C02 – Valdoria Votes**        | KC7    | Phishing → credential harvest (fake portal) → valid-account mailbox access → vishing helpdesk reset → workstation compromise → AI assistant probing (no voting-machine breach) | [folder](cases/kc7-c02-valdoria-votes/) · [queries](cases/kc7-c02-valdoria-votes/01_Queries.md)           |

_Additional cases will appear here as I publish them._

---

## Repo Map

- `cases/` – Complete investigations (timeline, queries, hypotheses, summary, evidence).
- `detections/` – “Productionized” rules (e.g., Microsoft Sentinel analytics) — *soon*.
- `workbooks/` – Hunting/IR workbooks (JSON) — *soon*.
- `lib/` – Reusable KQL functions/snippets — *soon*.
- `assets/` – Screenshots/diagrams used in docs — *soon*.

---

## How to Reproduce

Open a case folder, then run the queries in **`01_Queries.md`** in the order referenced by **`00_Timeline.md`**.  
KC7 cases rely on the KC7 dataset; homelab cases include case-specific notes in `04_Summary.md` or `Reproduce.md`.

---

## Conventions

- **Folders:** `cases/kc7-cXX-<slug>` (KC7) and `cases/lab-cXX-<slug>` (homelab).
- **Evidence:** each artifact in its own file under `Evidence/` (plus `images/` if needed).
- **Hypotheses:** one file per case (`02_Hypotheses.md`) until the case is very large.

---

## License

- Code/KQL (`/lib`, `/detections`, `/workbooks`): **MIT**  
- Documentation (`/cases`, `/assets`): **CC BY-NC 4.0**

