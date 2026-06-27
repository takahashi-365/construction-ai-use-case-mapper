from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest


BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_CSV = BASE_DIR / "input" / "construction_ai_use_cases_v001.csv"

OUTPUT_DIR = BASE_DIR / "output"

MAPPING_OUTPUT = OUTPUT_DIR / "ai_use_case_mapping_v001.csv"
HUMAN_REVIEW_OUTPUT = OUTPUT_DIR / "human_review_required_use_cases_v001.csv"
RAG_OUTPUT = OUTPUT_DIR / "rag_candidate_use_cases_v001.csv"
AUTOMATION_OUTPUT = OUTPUT_DIR / "automation_candidate_use_cases_v001.csv"
BI_OUTPUT = OUTPUT_DIR / "bi_candidate_use_cases_v001.csv"
RULE_BASED_CHECK_OUTPUT = OUTPUT_DIR / "rule_based_check_candidate_use_cases_v001.csv"
DX_SERVICE_OUTPUT = OUTPUT_DIR / "dx_service_candidates_v001.csv"
DEEP_DIVE_OUTPUT = OUTPUT_DIR / "deep_dive_targets_v001.csv"
DISCUSSION_REPORT_OUTPUT = OUTPUT_DIR / "discussion_reference_report_v001.md"
SUMMARY_OUTPUT = OUTPUT_DIR / "ai_use_case_summary_v001.md"


REQUIRED_INPUT_COLUMNS = [
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


REQUIRED_DX_SERVICE_COLUMNS = [
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


REQUIRED_DEEP_DIVE_COLUMNS = [
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


@pytest.fixture(scope="session", autouse=True)
def run_workflow_once():
    """Run all scripts once before testing generated outputs."""
    subprocess.run(
        [sys.executable, "src/classify_ai_use_cases.py"],
        cwd=BASE_DIR,
        check=True,
    )

    subprocess.run(
        [sys.executable, "src/generate_dx_service_candidates.py"],
        cwd=BASE_DIR,
        check=True,
    )

    subprocess.run(
        [sys.executable, "src/generate_ai_use_case_summary.py"],
        cwd=BASE_DIR,
        check=True,
    )


@pytest.fixture()
def input_df() -> pd.DataFrame:
    return pd.read_csv(INPUT_CSV, encoding="utf-8-sig")


@pytest.fixture()
def mapping_df() -> pd.DataFrame:
    return pd.read_csv(MAPPING_OUTPUT, encoding="utf-8-sig")


@pytest.fixture()
def dx_service_df() -> pd.DataFrame:
    return pd.read_csv(DX_SERVICE_OUTPUT, encoding="utf-8-sig")


@pytest.fixture()
def deep_dive_df() -> pd.DataFrame:
    return pd.read_csv(DEEP_DIVE_OUTPUT, encoding="utf-8-sig")


def test_input_csv_has_required_columns(input_df):
    missing_columns = [column for column in REQUIRED_INPUT_COLUMNS if column not in input_df.columns]
    assert missing_columns == []


def test_input_csv_has_ten_sample_use_cases(input_df):
    assert len(input_df) == 10
    assert input_df["UseCaseId"].is_unique
    assert set(input_df["UseCaseId"]) == {
        "UC-001",
        "UC-002",
        "UC-003",
        "UC-004",
        "UC-005",
        "UC-006",
        "UC-007",
        "UC-008",
        "UC-009",
        "UC-010",
    }


def test_mapping_output_has_required_columns(mapping_df):
    missing_columns = [column for column in REQUIRED_MAPPING_COLUMNS if column not in mapping_df.columns]
    assert missing_columns == []


def test_all_expected_output_files_exist():
    expected_files = [
        MAPPING_OUTPUT,
        HUMAN_REVIEW_OUTPUT,
        RAG_OUTPUT,
        AUTOMATION_OUTPUT,
        BI_OUTPUT,
        RULE_BASED_CHECK_OUTPUT,
        DX_SERVICE_OUTPUT,
        DEEP_DIVE_OUTPUT,
        DISCUSSION_REPORT_OUTPUT,
        SUMMARY_OUTPUT,
    ]

    for file_path in expected_files:
        assert file_path.exists(), f"Missing output file: {file_path}"
        assert file_path.stat().st_size > 0, f"Empty output file: {file_path}"


def test_high_risk_use_cases_require_human_review(input_df, mapping_df):
    merged_df = mapping_df.merge(
        input_df[["UseCaseId", "RiskLevel"]],
        on="UseCaseId",
        how="left",
    )

    high_risk_df = merged_df[merged_df["RiskLevel"].str.lower() == "high"]

    assert not high_risk_df.empty
    assert high_risk_df["HumanReviewRequired"].apply(normalize_bool).all()


def test_design_legal_or_construction_judgment_requires_human_review(input_df, mapping_df):
    judgment_columns = [
        "RequiresDesignJudgment",
        "RequiresLegalJudgment",
        "RequiresConstructionJudgment",
    ]

    merged_df = mapping_df.merge(
        input_df[["UseCaseId"] + judgment_columns],
        on="UseCaseId",
        how="left",
    )

    judgment_required_df = merged_df[
        merged_df[judgment_columns].applymap(normalize_bool).any(axis=1)
    ]

    assert not judgment_required_df.empty
    assert judgment_required_df["HumanReviewRequired"].apply(normalize_bool).all()


def test_expected_rag_candidates_exist(mapping_df):
    rag_df = mapping_df[mapping_df["RAGSuitable"].apply(normalize_bool)]

    expected_use_case_ids = {"UC-004", "UC-005", "UC-010"}

    assert expected_use_case_ids.issubset(set(rag_df["UseCaseId"]))


def test_expected_automation_candidates_exist(mapping_df):
    automation_df = mapping_df[mapping_df["AutomationSuitable"].apply(normalize_bool)]

    expected_use_case_ids = {"UC-006", "UC-009"}

    assert expected_use_case_ids.issubset(set(automation_df["UseCaseId"]))


def test_expected_rule_based_check_candidates_exist(mapping_df):
    rule_based_df = mapping_df[mapping_df["RuleBasedCheckSuitable"].apply(normalize_bool)]

    expected_use_case_ids = {"UC-001", "UC-002", "UC-003", "UC-009"}

    assert expected_use_case_ids.issubset(set(rule_based_df["UseCaseId"]))


def test_expected_bi_candidates_exist(mapping_df):
    bi_df = mapping_df[mapping_df["BISuitable"].apply(normalize_bool)]

    expected_use_case_ids = {"UC-001", "UC-002", "UC-007"}

    assert expected_use_case_ids.issubset(set(bi_df["UseCaseId"]))


def test_dx_service_candidate_output_has_required_columns(dx_service_df):
    missing_columns = [column for column in REQUIRED_DX_SERVICE_COLUMNS if column not in dx_service_df.columns]
    assert missing_columns == []


def test_dx_service_candidates_are_not_empty(dx_service_df):
    assert not dx_service_df.empty
    assert dx_service_df["CandidateDXService"].notna().all()
    assert dx_service_df["RecommendedApproach"].notna().all()
    assert dx_service_df["DiscussionPoint"].notna().all()


def test_deep_dive_output_has_required_columns(deep_dive_df):
    missing_columns = [column for column in REQUIRED_DEEP_DIVE_COLUMNS if column not in deep_dive_df.columns]
    assert missing_columns == []


def test_deep_dive_targets_are_not_empty(deep_dive_df):
    assert not deep_dive_df.empty
    assert deep_dive_df["DeepDiveRequired"].apply(normalize_bool).all()
    assert deep_dive_df["DeepDiveQuestion"].notna().all()


def test_discussion_report_contains_required_policy_notes():
    report_text = DISCUSSION_REPORT_OUTPUT.read_text(encoding="utf-8")

    required_phrases = [
        "AI classification results are not final decisions",
        "Human review is required",
        "Deep-dive targets require additional interviews",
        "does not use real project data",
    ]

    for phrase in required_phrases:
        assert phrase in report_text


def test_summary_report_contains_required_sections():
    summary_text = SUMMARY_OUTPUT.read_text(encoding="utf-8")

    required_sections = [
        "# AI Use Case Summary",
        "## 2. Overall Classification Summary",
        "## 3. Recommended Approach Summary",
        "## 5. Representative Use Cases",
        "## 11. Important Notes",
        "## 12. Portfolio Interpretation",
    ]

    for section in required_sections:
        assert section in summary_text


def test_reports_do_not_claim_ai_final_decision_authority():
    combined_text = (
        DISCUSSION_REPORT_OUTPUT.read_text(encoding="utf-8")
        + "\n"
        + SUMMARY_OUTPUT.read_text(encoding="utf-8")
    ).lower()

    forbidden_phrases = [
        "ai can make final decisions",
        "ai can automatically approve",
        "human review is not required",
        "ai replaces expert judgment",
        "ai guarantees safety",
        "ai determines legal compliance",
    ]

    for phrase in forbidden_phrases:
        assert phrase not in combined_text