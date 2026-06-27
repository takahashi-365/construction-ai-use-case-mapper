from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

OUTPUT_DIR = BASE_DIR / "output"

MAPPING_INPUT = OUTPUT_DIR / "ai_use_case_mapping_v001.csv"
DX_SERVICE_INPUT = OUTPUT_DIR / "dx_service_candidates_v001.csv"
DEEP_DIVE_INPUT = OUTPUT_DIR / "deep_dive_targets_v001.csv"

SUMMARY_OUTPUT = OUTPUT_DIR / "ai_use_case_summary_v001.md"


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


def build_count_table(mapping_df: pd.DataFrame) -> str:
    """Build a summary count table."""
    total_count = len(mapping_df)
    rag_count = int(mapping_df["RAGSuitable"].apply(normalize_bool).sum())
    bi_count = int(mapping_df["BISuitable"].apply(normalize_bool).sum())
    automation_count = int(mapping_df["AutomationSuitable"].apply(normalize_bool).sum())
    rule_based_count = int(mapping_df["RuleBasedCheckSuitable"].apply(normalize_bool).sum())
    human_review_count = int(mapping_df["HumanReviewRequired"].apply(normalize_bool).sum())
    deep_dive_count = int(mapping_df["DeepDiveRequired"].apply(normalize_bool).sum())
    out_of_scope_count = int(mapping_df["OutOfScope"].apply(normalize_bool).sum())

    return f"""| Item | Count |
|---|---:|
| Total use cases | {total_count} |
| RAG suitable | {rag_count} |
| BI suitable | {bi_count} |
| Automation suitable | {automation_count} |
| Rule-based check suitable | {rule_based_count} |
| Human review required | {human_review_count} |
| Deep dive required | {deep_dive_count} |
| Out of scope | {out_of_scope_count} |
"""


def build_representative_use_cases(mapping_df: pd.DataFrame) -> str:
    """Build representative use case sections."""
    sections = []

    category_definitions = [
        ("RAG Suitable", "RAGSuitable"),
        ("BI Suitable", "BISuitable"),
        ("Automation Suitable", "AutomationSuitable"),
        ("Rule-based Check Suitable", "RuleBasedCheckSuitable"),
        ("Human Review Required", "HumanReviewRequired"),
        ("Deep Dive Required", "DeepDiveRequired"),
    ]

    for title, column in category_definitions:
        target_df = mapping_df[mapping_df[column].apply(normalize_bool)].copy()
        target_df = target_df[["UseCaseId", "UseCaseName", "RecommendedApproach"]].head(5)

        sections.append(f"### {title}\n")
        sections.append(build_markdown_table(target_df, ["UseCaseId", "UseCaseName", "RecommendedApproach"]))

    return "\n".join(sections)


def build_recommended_approach_summary(mapping_df: pd.DataFrame) -> str:
    """Build a table grouped by RecommendedApproach."""
    approach_counts = (
        mapping_df.groupby("RecommendedApproach")
        .size()
        .reset_index(name="Count")
        .sort_values(by=["Count", "RecommendedApproach"], ascending=[False, True])
    )

    return build_markdown_table(approach_counts, ["RecommendedApproach", "Count"])


def build_domain_summary(mapping_df: pd.DataFrame) -> str:
    """Build a table grouped by Domain."""
    domain_counts = (
        mapping_df.groupby("Domain")
        .size()
        .reset_index(name="Count")
        .sort_values(by=["Count", "Domain"], ascending=[False, True])
    )

    return build_markdown_table(domain_counts, ["Domain", "Count"])


def generate_summary_report(
    mapping_df: pd.DataFrame,
    dx_service_df: pd.DataFrame,
    deep_dive_df: pd.DataFrame,
) -> str:
    """Generate the AI use case summary report as Markdown."""
    dx_service_count = len(dx_service_df)
    deep_dive_count = len(deep_dive_df)

    human_review_df = mapping_df[mapping_df["HumanReviewRequired"].apply(normalize_bool)]
    deep_dive_mapping_df = mapping_df[mapping_df["DeepDiveRequired"].apply(normalize_bool)]
    out_of_scope_df = mapping_df[mapping_df["OutOfScope"].apply(normalize_bool)]

    report = f"""# AI Use Case Summary

## 1. Purpose

This summary provides an overview of the AI/DX classification results for fictional construction and BIM-related use cases.

This report is part of PoC 2: BIM / Construction AI Use Case Mapper.

The purpose of this PoC is not to make final decisions with AI.  
The purpose is to structure construction and BIM-related business use cases before AI/DX implementation.

---

## 2. Overall Classification Summary

{build_count_table(mapping_df)}

---

## 3. Recommended Approach Summary

{build_recommended_approach_summary(mapping_df)}

---

## 4. Domain Summary

{build_domain_summary(mapping_df)}

---

## 5. Representative Use Cases

{build_representative_use_cases(mapping_df)}

---

## 6. DX Service Candidate Summary

| Item | Count |
|---|---:|
| DX service candidate rows | {dx_service_count} |
| Deep dive target rows | {deep_dive_count} |

The DX service candidates are not final proposals.  
They are initial discussion references for stakeholder review and prioritization.

---

## 7. Human Review Required Use Cases

The following use cases require human review because they may involve design, construction, legal, safety, responsibility, or high-impact decisions.

{build_markdown_table(human_review_df, ["UseCaseId", "UseCaseName", "RecommendedApproach", "Reason"])}

---

## 8. Deep Dive Required Use Cases

The following use cases require additional interviews, source-of-truth confirmation, or detailed workflow review.

{build_markdown_table(deep_dive_mapping_df, ["UseCaseId", "UseCaseName", "RecommendedApproach", "Reason"])}

---

## 9. Out of Scope Use Cases

{build_markdown_table(out_of_scope_df, ["UseCaseId", "UseCaseName", "RecommendedApproach", "Reason"])}

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
"""

    return report


def main() -> None:
    """Generate the AI use case summary report."""
    if not MAPPING_INPUT.exists():
        raise FileNotFoundError(
            f"Mapping CSV not found: {MAPPING_INPUT}. Run src/classify_ai_use_cases.py first."
        )

    if not DX_SERVICE_INPUT.exists():
        raise FileNotFoundError(
            f"DX service candidate CSV not found: {DX_SERVICE_INPUT}. Run src/generate_dx_service_candidates.py first."
        )

    if not DEEP_DIVE_INPUT.exists():
        raise FileNotFoundError(
            f"Deep dive target CSV not found: {DEEP_DIVE_INPUT}. Run src/generate_dx_service_candidates.py first."
        )

    mapping_df = pd.read_csv(MAPPING_INPUT, encoding="utf-8-sig")
    dx_service_df = pd.read_csv(DX_SERVICE_INPUT, encoding="utf-8-sig")
    deep_dive_df = pd.read_csv(DEEP_DIVE_INPUT, encoding="utf-8-sig")

    validate_required_columns(mapping_df, REQUIRED_MAPPING_COLUMNS, "mapping CSV")

    summary_text = generate_summary_report(
        mapping_df=mapping_df,
        dx_service_df=dx_service_df,
        deep_dive_df=deep_dive_df,
    )

    SUMMARY_OUTPUT.write_text(summary_text, encoding="utf-8")

    print("AI use case summary generation completed.")
    print("Summary output: output/ai_use_case_summary_v001.md")


if __name__ == "__main__":
    main()