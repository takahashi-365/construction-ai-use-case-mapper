# Discussion Reference Report

## 1. Purpose

This report summarizes AI/DX support candidates for fictional construction and BIM-related use cases.

The classification results are not final decisions.  
They are discussion references for stakeholder review, prioritization, and deeper investigation.

---

## 2. Important Notes

- AI classification results are not final decisions.
- AI outputs should not be treated as automatic approvals.
- Human review is required for design, construction, legal, safety, cost, contract, or responsibility-related decisions.
- Deep-dive targets require additional interviews, source-of-truth confirmation, or detailed workflow review.
- This PoC does not use real project data, client data, or internal company service details.

---

## 3. Overall Summary

| Item | Count |
|---|---:|
| Total use cases | 10 |
| RAG suitable | 4 |
| BI suitable | 4 |
| Automation suitable | 6 |
| Rule-based check suitable | 6 |
| Human review required | 4 |
| Deep dive required | 10 |
| Out of scope | 0 |

---

## 4. DX Service Candidates

| UseCaseId | UseCaseName | CandidateDXService | RecommendedApproach | DiscussionPoint |
| --- | --- | --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based quality checker | Rule-based Check + Human Review | Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Define metrics, categories, and aggregation views for reporting or dashboarding. Confirm which repeated steps can be automated safely. Define clear validation rules and exception handling. |
| UC-002 | Room name consistency check | Rule-based quality checker | Rule-based Check + Human Review | Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Define metrics, categories, and aggregation views for reporting or dashboarding. Confirm which repeated steps can be automated safely. Define clear validation rules and exception handling. |
| UC-003 | COBie Component.Space validation | Rule-based quality checker | Rule-based Check + Human Review | Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Confirm which repeated steps can be automated safely. Define clear validation rules and exception handling. |
| UC-004 | BIM rule explanation assistant | RAG assistant | RAG Assistant + Human Review | Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Identify reference documents that should be used for RAG support. Confirm which repeated steps can be automated safely. |
| UC-005 | RFI draft support | Human-reviewed AI drafting support | RAG Assistant + Human Review | Clarify where human review and final approval are required. Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Identify reference documents that should be used for RAG support. |
| UC-006 | Meeting minutes summarization | Automation support tool | Automation Support | Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Confirm which repeated steps can be automated safely. |
| UC-007 | Construction issue classification | BI dashboard and classification support | DX Service Candidate Review | Clarify where human review and final approval are required. Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Define metrics, categories, and aggregation views for reporting or dashboarding. |
| UC-008 | Drawing revision impact review | Human-reviewed risk review support | RAG Assistant + Human Review | Clarify where human review and final approval are required. Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Identify reference documents that should be used for RAG support. Define clear validation rules and exception handling. |
| UC-009 | Equipment list comparison | Automation support tool and rule-based checker | Rule-based Check + Human Review | Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Confirm which repeated steps can be automated safely. Define clear validation rules and exception handling. |
| UC-010 | Facility management handover data check | RAG assistant and human-reviewed checklist | RAG Assistant + Human Review | Clarify where human review and final approval are required. Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline. Identify reference documents that should be used for RAG support. Define metrics, categories, and aggregation views for reporting or dashboarding. Define clear validation rules and exception handling. |


---

## 5. RAG Candidate Use Cases

| UseCaseId | UseCaseName | RecommendedApproach | Reason |
| --- | --- | --- | --- |
| UC-004 | BIM rule explanation assistant | RAG Assistant + Human Review | It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-005 | RFI draft support | RAG Assistant + Human Review | It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-008 | Drawing revision impact review | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |


---

## 6. BI Candidate Use Cases

| UseCaseId | UseCaseName | RecommendedApproach | Reason |
| --- | --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-002 | Room name consistency check | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-007 | Construction issue classification | DX Service Candidate Review | It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |


---

## 7. Rule-based Check Candidate Use Cases

| UseCaseId | UseCaseName | RecommendedApproach | Reason |
| --- | --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-002 | Room name consistency check | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-003 | COBie Component.Space validation | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-008 | Drawing revision impact review | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-009 | Equipment list comparison | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |


---

## 8. Automation Candidate Use Cases

| UseCaseId | UseCaseName | RecommendedApproach | Reason |
| --- | --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-002 | Room name consistency check | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-003 | COBie Component.Space validation | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-004 | BIM rule explanation assistant | RAG Assistant + Human Review | It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-006 | Meeting minutes summarization | Automation Support | It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-009 | Equipment list comparison | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |


---

## 9. Human Review Required Use Cases

| UseCaseId | UseCaseName | RecommendedApproach | Reason |
| --- | --- | --- | --- |
| UC-005 | RFI draft support | RAG Assistant + Human Review | It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-007 | Construction issue classification | DX Service Candidate Review | It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-008 | Drawing revision impact review | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |


---

## 10. Deep Dive Target Use Cases

| UseCaseId | UseCaseName | Stakeholders | DeepDiveReason | DeepDiveQuestion |
| --- | --- | --- | --- | --- |
| UC-001 | Door schedule quality check | BIM Coordinator | The checking rules are relatively clear | Which door parameters should be treated as mandatory |
| UC-002 | Room name consistency check | BIM Coordinator and Design Manager | Naming rules may differ by project and need stakeholder confirmation | What room naming rules should be used as the source of truth |
| UC-003 | COBie Component.Space validation | BIM Coordinator and FM Manager | Handover requirements and space naming rules need confirmation | Which space list should be treated as the correct reference for handover |
| UC-004 | BIM rule explanation assistant | BIM Coordinator and Project Manager | Reference documents and rule interpretation need confirmation | Which BIM standards and fix guides should be used as reference sources |
| UC-005 | RFI draft support | Site Manager Design Manager and Project Manager | RFI responses may affect design construction cost or responsibility | Who must approve the final RFI response before sending |
| UC-006 | Meeting minutes summarization | Project Manager | The task is mainly summarization and does not make final decisions | What format should be used for action items and decisions |
| UC-007 | Construction issue classification | Construction Manager and Site Manager | Issue severity and responsibility require construction context | What issue categories and priority rules should be used |
| UC-008 | Drawing revision impact review | Design Manager and BIM Coordinator | Design impact cannot be finalized by AI and requires expert review | Who confirms whether a revision requires BIM model update |
| UC-009 | Equipment list comparison | FM Manager and BIM Coordinator | Handover data sources and naming rules need agreement | Which equipment list should be used as the master list |
| UC-010 | Facility management handover data check | FM Manager BIM Coordinator and Client Representative | FM requirements legal responsibility and owner requirements need confirmation | What information is mandatory for facility management after handover |


---

## 11. Discussion Questions

The following questions should be used when reviewing deep-dive target use cases.

- What is the business purpose of this use case?
- Who creates and maintains the input data?
- Which document or dataset should be treated as the source of truth?
- What criteria are used for final approval?
- Who is responsible for the final decision?
- What exceptions occur in real projects?
- Which parts can be supported by AI or automation?
- Which parts require human review?
- What output format is useful for stakeholders?
- What additional data is required before defining a service outline?

---

## 12. Limitations

This report is a portfolio output based on fictional sample use cases.  
It is not a production AI diagnosis system, consulting deliverable, legal judgment, design judgment, construction judgment, or final DX service proposal.

The purpose is to demonstrate how construction and BIM-related use cases can be structured before AI/DX implementation.
