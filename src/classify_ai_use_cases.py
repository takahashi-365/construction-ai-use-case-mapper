from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_CSV = BASE_DIR / "input" / "construction_ai_use_cases_v001.csv"
OUTPUT_DIR = BASE_DIR / "output"

MAPPING_OUTPUT = OUTPUT_DIR / "ai_use_case_mapping_v001.csv"
HUMAN_REVIEW_OUTPUT = OUTPUT_DIR / "human_review_required_use_cases_v001.csv"
RAG_OUTPUT = OUTPUT_DIR / "rag_candidate_use_cases_v001.csv"
AUTOMATION_OUTPUT = OUTPUT_DIR / "automation_candidate_use_cases_v001.csv"
BI_OUTPUT = OUTPUT_DIR / "bi_candidate_use_cases_v001.csv"
RULE_BASED_CHECK_OUTPUT = OUTPUT_DIR / "rule_based_check_candidate_use_cases_v001.csv"

REQUIRED_COLUMNS = [
    "UseCaseId",
    "Domain",
    "WorkPhase",
    "Role",
    "UseCaseName",
    "CurrentTask",
    "InputData",
    "OutputData",
    "CurrentTool",
    "PainPoint",
    "DecisionType",
    "RiskLevel",
    "RequiresDomainKnowledge",
    "RequiresDesignJudgment",
    "RequiresLegalJudgment",
    "RequiresConstructionJudgment",
    "DataStructuredness",
    "Frequency",
    "CandidateAIUse",
    "CandidateDXService",
    "Stakeholders",
    "DeepDiveRequired",
    "DeepDiveReason",
    "DeepDiveQuestion",
]


OUTPUT_COLUMNS = [
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


def normalize_text(value) -> str:
    """Convert a cell value to a lower-case string for keyword matching."""
    if pd.isna(value):
        return ""
    return str(value).strip().lower()


def normalize_bool(value) -> bool:
    """Convert TRUE/FALSE-like values to boolean."""
    if pd.isna(value):
        return False

    text = str(value).strip().lower()

    return text in {"true", "yes", "1", "y"}


def contains_any(text: str, keywords: list[str]) -> bool:
    """Return True if text contains any keyword."""
    return any(keyword.lower() in text for keyword in keywords)


def validate_required_columns(df: pd.DataFrame) -> None:
    """Check that the input CSV has all required columns."""
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def is_rag_suitable(row: pd.Series) -> bool:
    decision_type = normalize_text(row["DecisionType"])
    input_data = normalize_text(row["InputData"])
    candidate_ai_use = normalize_text(row["CandidateAIUse"])
    candidate_dx_service = normalize_text(row["CandidateDXService"])

    rag_keywords = [
        "document",
        "documents",
        "specification",
        "specifications",
        "manual",
        "manuals",
        "standard",
        "standards",
        "email",
        "emails",
        "rfi",
        "drawing",
        "drawings",
        "reference",
    ]

    return (
        decision_type in {"explanation", "draftsupport"}
        or contains_any(input_data, rag_keywords)
        or contains_any(candidate_ai_use, ["reference", "explain", "draft"])
        or "rag assistant" in candidate_dx_service
    )


def is_bi_suitable(row: pd.Series) -> bool:
    decision_type = normalize_text(row["DecisionType"])
    data_structuredness = normalize_text(row["DataStructuredness"])
    output_data = normalize_text(row["OutputData"])
    pain_point = normalize_text(row["PainPoint"])
    candidate_dx_service = normalize_text(row["CandidateDXService"])

    return (
        decision_type in {"datacheck", "classification"}
        or data_structuredness in {"structured", "semistructured"}
        and contains_any(output_data, ["issue list", "check result", "report", "classified list"])
        or "bi dashboard" in candidate_dx_service
        or contains_any(pain_point, ["compare", "trend", "inconsistent", "difficult to compare"])
    )


def is_automation_suitable(row: pd.Series) -> bool:
    decision_type = normalize_text(row["DecisionType"])
    frequency = normalize_text(row["Frequency"])
    candidate_dx_service = normalize_text(row["CandidateDXService"])
    current_task = normalize_text(row["CurrentTask"])
    risk_level = normalize_text(row["RiskLevel"])

    requires_design = normalize_bool(row["RequiresDesignJudgment"])
    requires_legal = normalize_bool(row["RequiresLegalJudgment"])
    requires_construction = normalize_bool(row["RequiresConstructionJudgment"])

    task_keywords = ["compare", "summarize", "extract", "generate list", "create"]

    judgment_free = not requires_design and not requires_legal and not requires_construction

    return (
        decision_type in {"summarization", "comparison"}
        or frequency in {"daily", "weekly"}
        or "automation support tool" in candidate_dx_service
        or contains_any(current_task, task_keywords)
    ) and risk_level in {"low", "medium"} and judgment_free


def is_rule_based_check_suitable(row: pd.Series) -> bool:
    decision_type = normalize_text(row["DecisionType"])
    data_structuredness = normalize_text(row["DataStructuredness"])
    input_data = normalize_text(row["InputData"])
    candidate_ai_use = normalize_text(row["CandidateAIUse"])
    candidate_dx_service = normalize_text(row["CandidateDXService"])

    structured_keywords = [
        "schedule",
        "spreadsheet",
        "excel",
        "cobie",
        "list",
    ]

    check_keywords = [
        "detect missing",
        "missing values",
        "compare",
        "validate",
        "inconsistent",
        "mismatch",
    ]

    return (
        decision_type in {"datacheck", "comparison"}
        or data_structuredness == "structured"
        or contains_any(input_data, structured_keywords)
        or contains_any(candidate_ai_use, check_keywords)
        or "rule-based quality checker" in candidate_dx_service
    )


def is_human_review_required(row: pd.Series) -> bool:
    risk_level = normalize_text(row["RiskLevel"])
    decision_type = normalize_text(row["DecisionType"])
    candidate_dx_service = normalize_text(row["CandidateDXService"])

    requires_design = normalize_bool(row["RequiresDesignJudgment"])
    requires_legal = normalize_bool(row["RequiresLegalJudgment"])
    requires_construction = normalize_bool(row["RequiresConstructionJudgment"])

    return (
        risk_level == "high"
        or requires_design
        or requires_legal
        or requires_construction
        or decision_type in {"riskreview", "decisionmaking"}
        or "human-reviewed" in candidate_dx_service
    )


def is_deep_dive_required(row: pd.Series) -> bool:
    risk_level = normalize_text(row["RiskLevel"])
    stakeholders = normalize_text(row["Stakeholders"])
    deep_dive_reason = normalize_text(row["DeepDiveReason"])

    requires_design = normalize_bool(row["RequiresDesignJudgment"])
    requires_legal = normalize_bool(row["RequiresLegalJudgment"])
    requires_construction = normalize_bool(row["RequiresConstructionJudgment"])
    input_deep_dive_required = normalize_bool(row["DeepDiveRequired"])

    has_multiple_stakeholders = " and " in stakeholders or "," in stakeholders

    return (
        input_deep_dive_required
        or risk_level == "high"
        or has_multiple_stakeholders
        or deep_dive_reason != ""
        or requires_design
        or requires_legal
        or requires_construction
    )


def is_out_of_scope(row: pd.Series) -> bool:
    """Detect use cases that should not be handled as AI/DX support targets."""
    current_task = normalize_text(row["CurrentTask"])
    candidate_ai_use = normalize_text(row["CandidateAIUse"])

    out_of_scope_keywords = [
        "final decision",
        "automatically approve",
        "approve design",
        "decide construction method",
        "determine legal compliance",
        "determine contract responsibility",
        "guarantee safety",
    ]

    return contains_any(current_task, out_of_scope_keywords) or contains_any(
        candidate_ai_use, out_of_scope_keywords
    )


def decide_recommended_approach(
    rag_suitable: bool,
    bi_suitable: bool,
    automation_suitable: bool,
    rule_based_check_suitable: bool,
    human_review_required: bool,
    deep_dive_required: bool,
    out_of_scope: bool,
) -> str:
    """Decide the recommended initial AI/DX support approach."""
    if out_of_scope:
        return "Out of Scope"

    if human_review_required and rag_suitable:
        return "RAG Assistant + Human Review"

    if human_review_required and rule_based_check_suitable:
        return "Rule-based Check + Human Review"

    if human_review_required:
        return "DX Service Candidate Review"

    if rule_based_check_suitable:
        return "Rule-based Check + Human Review"

    if rag_suitable:
        return "RAG Assistant + Human Review"

    if bi_suitable:
        return "BI Dashboard"

    if automation_suitable:
        return "Automation Support"

    if deep_dive_required:
        return "Deep Dive Required"

    return "Data Structuring First"


def build_reason(
    row: pd.Series,
    rag_suitable: bool,
    bi_suitable: bool,
    automation_suitable: bool,
    rule_based_check_suitable: bool,
    human_review_required: bool,
    deep_dive_required: bool,
    out_of_scope: bool,
) -> str:
    """Generate a simple explanation for the classification result."""
    reasons = []

    if out_of_scope:
        reasons.append(
            "This use case is out of scope because it may require AI to make a final decision."
        )

    if rule_based_check_suitable:
        reasons.append(
            "It is suitable for rule-based checking because it uses structured data or clear validation logic."
        )

    if rag_suitable:
        reasons.append(
            "It is suitable for RAG support because it may require reference documents, explanations, or draft generation."
        )

    if bi_suitable:
        reasons.append(
            "It is suitable for BI or reporting because it can support issue tracking, comparison, or trend analysis."
        )

    if automation_suitable:
        reasons.append(
            "It is suitable for automation support because the task includes repetitive summarization, comparison, extraction, or list generation."
        )

    if human_review_required:
        reasons.append(
            "Human review is required because the task may involve design, construction, legal, risk, responsibility, or high-impact decisions."
        )

    if deep_dive_required:
        reasons.append(
            "A deep dive is required because additional stakeholder confirmation, source-of-truth definition, or detailed criteria may be needed."
        )

    if not reasons:
        reasons.append(
            "This use case should first be structured further before selecting an AI/DX support pattern."
        )

    return " ".join(reasons)


def classify_use_cases(df: pd.DataFrame) -> pd.DataFrame:
    """Classify all use cases and return a mapping DataFrame."""
    output_rows = []

    for _, row in df.iterrows():
        rag_suitable = is_rag_suitable(row)
        bi_suitable = is_bi_suitable(row)
        automation_suitable = is_automation_suitable(row)
        rule_based_check_suitable = is_rule_based_check_suitable(row)
        human_review_required = is_human_review_required(row)
        deep_dive_required = is_deep_dive_required(row)
        out_of_scope = is_out_of_scope(row)

        recommended_approach = decide_recommended_approach(
            rag_suitable=rag_suitable,
            bi_suitable=bi_suitable,
            automation_suitable=automation_suitable,
            rule_based_check_suitable=rule_based_check_suitable,
            human_review_required=human_review_required,
            deep_dive_required=deep_dive_required,
            out_of_scope=out_of_scope,
        )

        reason = build_reason(
            row=row,
            rag_suitable=rag_suitable,
            bi_suitable=bi_suitable,
            automation_suitable=automation_suitable,
            rule_based_check_suitable=rule_based_check_suitable,
            human_review_required=human_review_required,
            deep_dive_required=deep_dive_required,
            out_of_scope=out_of_scope,
        )

        output_rows.append(
            {
                "UseCaseId": row["UseCaseId"],
                "UseCaseName": row["UseCaseName"],
                "Domain": row["Domain"],
                "WorkPhase": row["WorkPhase"],
                "RecommendedApproach": recommended_approach,
                "RAGSuitable": rag_suitable,
                "BISuitable": bi_suitable,
                "AutomationSuitable": automation_suitable,
                "RuleBasedCheckSuitable": rule_based_check_suitable,
                "HumanReviewRequired": human_review_required,
                "DeepDiveRequired": deep_dive_required,
                "CandidateDXService": row["CandidateDXService"],
                "Reason": reason,
                "RequiredData": row["InputData"],
                "ExpectedOutput": row["OutputData"],
                "OutOfScope": out_of_scope,
            }
        )

    return pd.DataFrame(output_rows, columns=OUTPUT_COLUMNS)


def write_outputs(mapping_df: pd.DataFrame) -> None:
    """Write the main mapping output and derived CSV files."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    mapping_df.to_csv(MAPPING_OUTPUT, index=False, encoding="utf-8-sig")

    mapping_df[mapping_df["HumanReviewRequired"]].to_csv(
        HUMAN_REVIEW_OUTPUT, index=False, encoding="utf-8-sig"
    )

    mapping_df[mapping_df["RAGSuitable"]].to_csv(
        RAG_OUTPUT, index=False, encoding="utf-8-sig"
    )

    mapping_df[mapping_df["AutomationSuitable"]].to_csv(
        AUTOMATION_OUTPUT, index=False, encoding="utf-8-sig"
    )

    mapping_df[mapping_df["BISuitable"]].to_csv(
        BI_OUTPUT, index=False, encoding="utf-8-sig"
    )

    mapping_df[mapping_df["RuleBasedCheckSuitable"]].to_csv(
        RULE_BASED_CHECK_OUTPUT, index=False, encoding="utf-8-sig"
    )


def main() -> None:
    """Run the AI use case classification workflow."""
    if not INPUT_CSV.exists():
        raise FileNotFoundError(f"Input CSV not found: {INPUT_CSV}")

    df = pd.read_csv(INPUT_CSV, encoding="utf-8-sig")
    validate_required_columns(df)

    mapping_df = classify_use_cases(df)
    write_outputs(mapping_df)

    print("AI use case classification completed.")
    print("Main output: output/ai_use_case_mapping_v001.csv")
    print("Human review output: output/human_review_required_use_cases_v001.csv")
    print("RAG candidate output: output/rag_candidate_use_cases_v001.csv")
    print("Automation candidate output: output/automation_candidate_use_cases_v001.csv")
    print("BI candidate output: output/bi_candidate_use_cases_v001.csv")
    print("Rule-based check candidate output: output/rule_based_check_candidate_use_cases_v001.csv")


if __name__ == "__main__":
    main()