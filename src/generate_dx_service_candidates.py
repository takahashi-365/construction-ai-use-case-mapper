from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_CSV = BASE_DIR / "input" / "construction_ai_use_cases_v001.csv"
OUTPUT_DIR = BASE_DIR / "output"

MAPPING_INPUT = OUTPUT_DIR / "ai_use_case_mapping_v001.csv"

DX_SERVICE_OUTPUT = OUTPUT_DIR / "dx_service_candidates_v001.csv"
DEEP_DIVE_OUTPUT = OUTPUT_DIR / "deep_dive_targets_v001.csv"
DISCUSSION_REPORT_OUTPUT = OUTPUT_DIR / "discussion_reference_report_v001.md"


REQUIRED_MAPPING_COLUMNS = [
    "UseCaseId",
    "UseCaseName",
    "Domain",
    "WorkPhase",
    "RecommendedApproach",
    "RAGSuitable",
    "BISuitable",
    "AutomationSuitable",
    "RuleBasedCheckSuitable",
    "HumanReviewRequired",
    "DeepDiveRequired",
    "CandidateDXService",
    "Reason",
    "RequiredData",
    "ExpectedOutput",
    "OutOfScope",
]


REQUIRED_INPUT_COLUMNS = [
    "UseCaseId",
    "Stakeholders",
    "DeepDiveRequired",
    "DeepDiveReason",
    "DeepDiveQuestion",
]


DX_SERVICE_COLUMNS = [
    "UseCaseId",
    "UseCaseName",
    "CandidateDXService",
    "RecommendedApproach",
    "Reason",
    "RAGSuitable",
    "BISuitable",
    "AutomationSuitable",
    "RuleBasedCheckSuitable",
    "HumanReviewRequired",
    "DeepDiveRequired",
    "DiscussionPoint",
]


DEEP_DIVE_COLUMNS = [
    "UseCaseId",
    "UseCaseName",
    "Stakeholders",
    "DeepDiveRequired",
    "DeepDiveReason",
    "DeepDiveQuestion",
    "ExpectedAdditionalInformation",
]


def normalize_bool(value) -> bool:
    """Convert TRUE/FALSE-like values to boolean."""
    if pd.isna(value):
        return False

    if isinstance(value, bool):
        return value

    text = str(value).strip().lower()
    return text in {"true", "yes", "1", "y"}


def validate_required_columns(df: pd.DataFrame, required_columns: list[str], file_label: str) -> None:
    """Check that the DataFrame contains all required columns."""
    missing_columns = [column for column in required_columns if column not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns in {file_label}: {missing_columns}")

def build_discussion_point(row: pd.Series) -> str:
    """Create a discussion point for each DX service candidate."""
    points = []

    if normalize_bool(row["OutOfScope"]):
        points.append("This use case should not be treated as an AI/DX implementation target without scope review.")

    if normalize_bool(row["HumanReviewRequired"]):
        points.append("Clarify where human review and final approval are required.")

    if normalize_bool(row["DeepDiveRequired_mapping"]):
        points.append("Confirm detailed requirements, stakeholders, and source-of-truth documents before defining a service outline.")

    if normalize_bool(row["RAGSuitable"]):
        points.append("Identify reference documents that should be used for RAG support.")

    if normalize_bool(row["BISuitable"]):
        points.append("Define metrics, categories, and aggregation views for reporting or dashboarding.")

    if normalize_bool(row["AutomationSuitable"]):
        points.append("Confirm which repeated steps can be automated safely.")

    if normalize_bool(row["RuleBasedCheckSuitable"]):
        points.append("Define clear validation rules and exception handling.")

    if not points:
        points.append("Clarify the business purpose and required data before selecting an AI/DX support pattern.")

    return " ".join(points)


def build_expected_additional_information(row: pd.Series) -> str:
    """Create expected additional information for deep-dive targets."""
    items = []

    deep_dive_reason = str(row.get("DeepDiveReason", "")).strip()

    if deep_dive_reason:
        items.append("Detailed reason and background for the deep-dive requirement")

    stakeholders = str(row.get("Stakeholders", "")).strip()

    if stakeholders:
        items.append("Stakeholder roles and review responsibilities")

    items.extend(
        [
            "Source-of-truth documents or data",
            "Decision criteria",
            "Input data format",
            "Expected output format",
            "Exception cases",
            "Human review scope",
            "Approval workflow",
        ]
    )

    return "; ".join(items)


def create_dx_service_candidates(merged_df: pd.DataFrame) -> pd.DataFrame:
    """Create a DX service candidate list from the mapping results."""
    rows = []

    for _, row in merged_df.iterrows():
        rows.append(
            {
                "UseCaseId": row["UseCaseId"],
                "UseCaseName": row["UseCaseName"],
                "CandidateDXService": row["CandidateDXService"],
                "RecommendedApproach": row["RecommendedApproach"],
                "Reason": row["Reason"],
                "RAGSuitable": normalize_bool(row["RAGSuitable"]),
                "BISuitable": normalize_bool(row["BISuitable"]),
                "AutomationSuitable": normalize_bool(row["AutomationSuitable"]),
                "RuleBasedCheckSuitable": normalize_bool(row["RuleBasedCheckSuitable"]),
                "HumanReviewRequired": normalize_bool(row["HumanReviewRequired"]),
                "DeepDiveRequired": normalize_bool(row["DeepDiveRequired_mapping"]),
                "DiscussionPoint": build_discussion_point(row),
            }
        )

    return pd.DataFrame(rows, columns=DX_SERVICE_COLUMNS)


def create_deep_dive_targets(merged_df: pd.DataFrame) -> pd.DataFrame:
    """Create a deep-dive target list."""
    target_df = merged_df[merged_df["DeepDiveRequired_mapping"].apply(normalize_bool)].copy()

    rows = []

    for _, row in target_df.iterrows():
        rows.append(
            {
                "UseCaseId": row["UseCaseId"],
                "UseCaseName": row["UseCaseName"],
                "Stakeholders": row["Stakeholders"],
                "DeepDiveRequired": normalize_bool(row["DeepDiveRequired_mapping"]),
                "DeepDiveReason": row["DeepDiveReason"],
                "DeepDiveQuestion": row["DeepDiveQuestion"],
                "ExpectedAdditionalInformation": build_expected_additional_information(row),
            }
        )

    return pd.DataFrame(rows, columns=DEEP_DIVE_COLUMNS)


def format_bool(value) -> str:
    """Format boolean-like value for Markdown."""
    return "Yes" if normalize_bool(value) else "No"


def build_markdown_table(df: pd.DataFrame, columns: list[str]) -> str:
    """Build a simple Markdown table from selected columns."""
    if df.empty:
        return "No items found.\n"

    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"

    lines = [header, separator]

    for _, row in df.iterrows():
        values = []
        for column in columns:
            value = row[column]
            text = "" if pd.isna(value) else str(value)
            text = text.replace("\n", " ").replace("|", "/")
            values.append(text)
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines) + "\n"


def generate_discussion_report(
    mapping_df: pd.DataFrame,
    dx_service_df: pd.DataFrame,
    deep_dive_df: pd.DataFrame,
) -> str:
    """Generate the discussion reference report as Markdown."""
    total_count = len(mapping_df)
    rag_count = int(mapping_df["RAGSuitable"].apply(normalize_bool).sum())
    bi_count = int(mapping_df["BISuitable"].apply(normalize_bool).sum())
    automation_count = int(mapping_df["AutomationSuitable"].apply(normalize_bool).sum())
    rule_based_count = int(mapping_df["RuleBasedCheckSuitable"].apply(normalize_bool).sum())
    human_review_count = int(mapping_df["HumanReviewRequired"].apply(normalize_bool).sum())
    deep_dive_count = int(mapping_df["DeepDiveRequired"].apply(normalize_bool).sum())
    out_of_scope_count = int(mapping_df["OutOfScope"].apply(normalize_bool).sum())

    rag_df = mapping_df[mapping_df["RAGSuitable"].apply(normalize_bool)]
    bi_df = mapping_df[mapping_df["BISuitable"].apply(normalize_bool)]
    automation_df = mapping_df[mapping_df["AutomationSuitable"].apply(normalize_bool)]
    rule_based_df = mapping_df[mapping_df["RuleBasedCheckSuitable"].apply(normalize_bool)]
    human_review_df = mapping_df[mapping_df["HumanReviewRequired"].apply(normalize_bool)]

    report = f"""# Discussion Reference Report

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
| Total use cases | {total_count} |
| RAG suitable | {rag_count} |
| BI suitable | {bi_count} |
| Automation suitable | {automation_count} |
| Rule-based check suitable | {rule_based_count} |
| Human review required | {human_review_count} |
| Deep dive required | {deep_dive_count} |
| Out of scope | {out_of_scope_count} |

---

## 4. DX Service Candidates

{build_markdown_table(dx_service_df, ["UseCaseId", "UseCaseName", "CandidateDXService", "RecommendedApproach", "DiscussionPoint"])}

---

## 5. RAG Candidate Use Cases

{build_markdown_table(rag_df, ["UseCaseId", "UseCaseName", "RecommendedApproach", "Reason"])}

---

## 6. BI Candidate Use Cases

{build_markdown_table(bi_df, ["UseCaseId", "UseCaseName", "RecommendedApproach", "Reason"])}

---

## 7. Rule-based Check Candidate Use Cases

{build_markdown_table(rule_based_df, ["UseCaseId", "UseCaseName", "RecommendedApproach", "Reason"])}

---

## 8. Automation Candidate Use Cases

{build_markdown_table(automation_df, ["UseCaseId", "UseCaseName", "RecommendedApproach", "Reason"])}

---

## 9. Human Review Required Use Cases

{build_markdown_table(human_review_df, ["UseCaseId", "UseCaseName", "RecommendedApproach", "Reason"])}

---

## 10. Deep Dive Target Use Cases

{build_markdown_table(deep_dive_df, ["UseCaseId", "UseCaseName", "Stakeholders", "DeepDiveReason", "DeepDiveQuestion"])}

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
"""

    return report


def main() -> None:
    """Generate DX service candidates, deep-dive targets, and discussion report."""
    if not INPUT_CSV.exists():
        raise FileNotFoundError(f"Input CSV not found: {INPUT_CSV}")

    if not MAPPING_INPUT.exists():
        raise FileNotFoundError(
            f"Mapping CSV not found: {MAPPING_INPUT}. Run src/classify_ai_use_cases.py first."
        )

    input_df = pd.read_csv(INPUT_CSV, encoding="utf-8-sig")
    mapping_df = pd.read_csv(MAPPING_INPUT, encoding="utf-8-sig")

    validate_required_columns(input_df, REQUIRED_INPUT_COLUMNS, "input CSV")
    validate_required_columns(mapping_df, REQUIRED_MAPPING_COLUMNS, "mapping CSV")

    merged_df = mapping_df.merge(
        input_df[
            [
                "UseCaseId",
                "Stakeholders",
                "DeepDiveRequired",
                "DeepDiveReason",
                "DeepDiveQuestion",
            ]
        ],
        on="UseCaseId",
        how="left",
        suffixes=("_mapping", "_input"),
    )

    dx_service_df = create_dx_service_candidates(merged_df)
    deep_dive_df = create_deep_dive_targets(merged_df)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dx_service_df.to_csv(DX_SERVICE_OUTPUT, index=False, encoding="utf-8-sig")
    deep_dive_df.to_csv(DEEP_DIVE_OUTPUT, index=False, encoding="utf-8-sig")

    report_text = generate_discussion_report(
        mapping_df=mapping_df,
        dx_service_df=dx_service_df,
        deep_dive_df=deep_dive_df,
    )

    DISCUSSION_REPORT_OUTPUT.write_text(report_text, encoding="utf-8")

    print("DX service candidate generation completed.")
    print("DX service candidates output: output/dx_service_candidates_v001.csv")
    print("Deep dive targets output: output/deep_dive_targets_v001.csv")
    print("Discussion reference report output: output/discussion_reference_report_v001.md")


if __name__ == "__main__":
    main()