# AI Use Case Summary

## 1. Purpose

This summary provides an overview of the AI/DX classification results for fictional construction and BIM-related use cases.

This report is part of PoC 2: BIM / Construction AI Use Case Mapper.

The purpose of this PoC is not to make final decisions with AI.  
The purpose is to structure construction and BIM-related business use cases before AI/DX implementation.

---

## 2. Overall Classification Summary

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

## 3. Recommended Approach Summary

| RecommendedApproach | Count |
| --- | --- |
| RAG Assistant + Human Review | 4 |
| Rule-based Check + Human Review | 4 |
| Automation Support | 1 |
| DX Service Candidate Review | 1 |


---

## 4. Domain Summary

| Domain | Count |
| --- | --- |
| BIM | 3 |
| Facility Management | 2 |
| COBie | 1 |
| Construction Management | 1 |
| Design Review | 1 |
| Meeting | 1 |
| RFI | 1 |


---

## 5. Representative Use Cases

### RAG Suitable

| UseCaseId | UseCaseName | RecommendedApproach |
| --- | --- | --- |
| UC-004 | BIM rule explanation assistant | RAG Assistant + Human Review |
| UC-005 | RFI draft support | RAG Assistant + Human Review |
| UC-008 | Drawing revision impact review | RAG Assistant + Human Review |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review |

### BI Suitable

| UseCaseId | UseCaseName | RecommendedApproach |
| --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based Check + Human Review |
| UC-002 | Room name consistency check | Rule-based Check + Human Review |
| UC-007 | Construction issue classification | DX Service Candidate Review |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review |

### Automation Suitable

| UseCaseId | UseCaseName | RecommendedApproach |
| --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based Check + Human Review |
| UC-002 | Room name consistency check | Rule-based Check + Human Review |
| UC-003 | COBie Component.Space validation | Rule-based Check + Human Review |
| UC-004 | BIM rule explanation assistant | RAG Assistant + Human Review |
| UC-006 | Meeting minutes summarization | Automation Support |

### Rule-based Check Suitable

| UseCaseId | UseCaseName | RecommendedApproach |
| --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based Check + Human Review |
| UC-002 | Room name consistency check | Rule-based Check + Human Review |
| UC-003 | COBie Component.Space validation | Rule-based Check + Human Review |
| UC-008 | Drawing revision impact review | RAG Assistant + Human Review |
| UC-009 | Equipment list comparison | Rule-based Check + Human Review |

### Human Review Required

| UseCaseId | UseCaseName | RecommendedApproach |
| --- | --- | --- |
| UC-005 | RFI draft support | RAG Assistant + Human Review |
| UC-007 | Construction issue classification | DX Service Candidate Review |
| UC-008 | Drawing revision impact review | RAG Assistant + Human Review |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review |

### Deep Dive Required

| UseCaseId | UseCaseName | RecommendedApproach |
| --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based Check + Human Review |
| UC-002 | Room name consistency check | Rule-based Check + Human Review |
| UC-003 | COBie Component.Space validation | Rule-based Check + Human Review |
| UC-004 | BIM rule explanation assistant | RAG Assistant + Human Review |
| UC-005 | RFI draft support | RAG Assistant + Human Review |


---

## 6. DX Service Candidate Summary

| Item | Count |
|---|---:|
| DX service candidate rows | 10 |
| Deep dive target rows | 10 |

The DX service candidates are not final proposals.  
They are initial discussion references for stakeholder review and prioritization.

---

## 7. Human Review Required Use Cases

The following use cases require human review because they may involve design, construction, legal, safety, responsibility, or high-impact decisions.

| UseCaseId | UseCaseName | RecommendedApproach | Reason |
| --- | --- | --- | --- |
| UC-005 | RFI draft support | RAG Assistant + Human Review | It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-007 | Construction issue classification | DX Service Candidate Review | It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-008 | Drawing revision impact review | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |


---

## 8. Deep Dive Required Use Cases

The following use cases require additional interviews, source-of-truth confirmation, or detailed workflow review.

| UseCaseId | UseCaseName | RecommendedApproach | Reason |
| --- | --- | --- | --- |
| UC-001 | Door schedule quality check | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-002 | Room name consistency check | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-003 | COBie Component.Space validation | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-004 | BIM rule explanation assistant | RAG Assistant + Human Review | It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-005 | RFI draft support | RAG Assistant + Human Review | It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-006 | Meeting minutes summarization | Automation Support | It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-007 | Construction issue classification | DX Service Candidate Review | It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-008 | Drawing revision impact review | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-009 | Equipment list comparison | Rule-based Check + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |
| UC-010 | Facility management handover data check | RAG Assistant + Human Review | It is suitable for rule-based checking because it uses structured data or clear validation logic. It is suitable for RAG support because it may require reference documents, explanations, or draft generation. It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis. Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions. A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed. |


---

## 9. Out of Scope Use Cases

No items found.


---

## 10. Classification Policy

This PoC classifies use cases into the following AI/DX support patterns.

- RAG suitable
- BI suitable
- Automation suitable
- Rule-based check suitable
- Human review required
- Deep dive required
- Out of scope

The classification is based on input data structure, decision type, risk level, required domain knowledge, human judgment requirements, and candidate AI/DX support patterns.

---

## 11. Important Notes

- AI classification results are not final decisions.
- AI outputs should not be treated as automatic approvals.
- Human review is required for design, construction, legal, safety, cost, contract, or responsibility-related decisions.
- Deep-dive targets require additional interviews, source-of-truth confirmation, or detailed workflow review.
- This PoC does not use real project data, client data, or internal company service details.
- This report is a portfolio output and not a production AI diagnosis system.

---

## 12. Portfolio Interpretation

This PoC demonstrates the ability to structure construction and BIM-related business use cases before AI/DX implementation.

It shows the following capabilities.

- Understanding construction and BIM business contexts
- Mapping business use cases into AI/DX support patterns
- Separating AI-supportable tasks from human decision-making tasks
- Identifying use cases suitable for RAG, BI, automation, and rule-based checking
- Treating AI outputs as discussion references rather than final decisions
- Extracting deep-dive targets for stakeholder interviews and additional information gathering

In short, this PoC demonstrates how real-world construction and BIM workflows can be structured before being handed over to AI, data, or system implementation.
