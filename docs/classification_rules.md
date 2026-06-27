# 分類ルール

このドキュメントでは、`input/construction_ai_use_cases_v001.csv` に記載された建設・BIM関連業務ユースケースを、AI/DX活用パターンに分類するためのルールを定義します。

本PoCでは、AIによる分類結果を最終判断とは扱いません。
分類結果は、関係者との協議、優先順位付け、追加ヒアリング、DXサービス候補検討のための参考資料として扱います。

---

## 1. 分類カテゴリ

本PoCでは、各ユースケースに対して以下の分類を行います。

| 分類名                    | 内容                          |
| ---------------------- | --------------------------- |
| RAGSuitable            | RAGによる文書参照・説明支援に向いているか      |
| BISuitable             | BIダッシュボードや集計可視化に向いているか      |
| AutomationSuitable     | 自動化支援に向いているか                |
| RuleBasedCheckSuitable | ルールベースチェックに向いているか           |
| HumanReviewRequired    | 人間レビューが必須か                  |
| DeepDiveRequired       | 追加ヒアリング・深掘りが必要か             |
| OutOfScope             | AI/DX支援対象外、またはAIが扱うべきでない判断か |

各分類は、TRUE / FALSE で判定します。

---

## 2. 基本方針

本PoCの分類方針は以下です。

```text
AIに任せきるための分類ではない
AI/DX活用の候補を整理するための分類である
人間判断が必要な業務は明示する
初期情報だけで判断できない業務はDeepDiveRequired=Trueにする
AIの出力は、協議用参考資料として扱う
設計・施工・法規・契約・安全・責任に関わる判断は、人間レビューを必須にする
```

---

## 3. RAGSuitable の判定ルール

### 3.1 概要

`RAGSuitable` は、RAGを使って文書や過去情報を参照しながら回答・説明・草案作成を支援するのに向いているユースケースを示します。

RAGは、以下のような業務に向いています。

```text
業務マニュアルを参照する
BIM標準やルールを参照する
仕様書、図面、引渡し資料などを根拠にする
過去のFix Guideや品質チェック結果を参照する
質問に対して根拠文書を示しながら説明する
RFIや説明文のドラフトを作る
```

---

### 3.2 TRUEにする条件

以下のいずれかに該当する場合、`RAGSuitable=True` とします。

```text
DecisionType が Explanation
DecisionType が DraftSupport
InputData に documents, specifications, manuals, standards, emails, RFI, drawings などが含まれる
CandidateAIUse が reference information を使う説明や草案作成である
CandidateDXService が RAG assistant を含む
```

---

### 3.3 代表例

```text
UC-004 BIM rule explanation assistant
UC-005 RFI draft support
UC-010 Facility management handover data check
```

---

### 3.4 注意点

RAG向きであっても、AIの回答を最終判断として扱ってはいけません。

特に以下を含む場合は、人間レビューが必要です。

```text
設計判断
施工判断
法規判断
契約判断
安全判断
コスト影響
責任判断
```

---

## 4. BISuitable の判定ルール

### 4.1 概要

`BISuitable` は、件数、傾向、割合、進捗、品質状態などを集計・可視化するのに向いているユースケースを示します。

BIは、以下のような業務に向いています。

```text
品質チェック結果を一覧化する
不備件数を集計する
担当者別、案件別、カテゴリ別に比較する
進捗や傾向を可視化する
問題の多い領域を把握する
```

---

### 4.2 TRUEにする条件

以下のいずれかに該当する場合、`BISuitable=True` とします。

```text
DecisionType が DataCheck
DecisionType が Classification
InputData が Structured または SemiStructured
OutputData が issue list, check result, report, classified list などである
CandidateDXService が BI dashboard を含む
PainPoint に compare, trend, inconsistent, difficult to compare などの集計・比較に関係する内容がある
```

---

### 4.3 代表例

```text
UC-001 Door schedule quality check
UC-002 Room name consistency check
UC-007 Construction issue classification
```

---

### 4.4 注意点

BIは、状況把握や判断材料の可視化に向いています。
ただし、BIの結果だけで設計・施工・法規・契約上の最終判断をしてはいけません。

---

## 5. AutomationSuitable の判定ルール

### 5.1 概要

`AutomationSuitable` は、繰り返し作業、転記、比較、要約、データ整形、一覧出力など、自動化支援に向いているユースケースを示します。

自動化支援は、以下のような業務に向いています。

```text
繰り返し発生する
作業手順が比較的明確である
データ変換や整形が中心である
一覧比較や差分抽出が中心である
議事録要約やアクションアイテム抽出が中心である
人間の最終判断前の下準備である
```

---

### 5.2 TRUEにする条件

以下のいずれかに該当する場合、`AutomationSuitable=True` とします。

```text
DecisionType が Summarization
DecisionType が Comparison
Frequency が Daily または Weekly
CandidateDXService が Automation support tool を含む
CurrentTask が compare, summarize, extract, generate list などの作業支援である
RiskLevel が Low または Medium
RequiresDesignJudgment, RequiresLegalJudgment, RequiresConstructionJudgment がすべて FALSE
```

---

### 5.3 代表例

```text
UC-006 Meeting minutes summarization
UC-009 Equipment list comparison
UC-003 COBie Component.Space validation
```

---

### 5.4 注意点

自動化に向いていても、以下の場合は完全自動化ではなく、人間確認を残します。

```text
成果物が外部提出される
引渡しデータに関係する
責任範囲が不明確である
確認基準が案件ごとに異なる
```

---

## 6. RuleBasedCheckSuitable の判定ルール

### 6.1 概要

`RuleBasedCheckSuitable` は、明確なルールに基づいて機械的にチェックできるユースケースを示します。

ルールベースチェックは、以下のような業務に向いています。

```text
未入力チェック
命名規則チェック
必須項目チェック
分類コードチェック
一覧間の突合チェック
入力値の形式チェック
```

---

### 6.2 TRUEにする条件

以下のいずれかに該当する場合、`RuleBasedCheckSuitable=True` とします。

```text
DecisionType が DataCheck
DecisionType が Comparison
DataStructuredness が Structured
InputData が schedule, spreadsheet, Excel, COBie などの表形式データである
CandidateAIUse が detect missing values, compare lists, validate values などである
CandidateDXService が Rule-based quality checker を含む
```

---

### 6.3 代表例

```text
UC-001 Door schedule quality check
UC-002 Room name consistency check
UC-003 COBie Component.Space validation
UC-009 Equipment list comparison
```

---

### 6.4 注意点

ルールベースチェックは、明確な基準がある場合に有効です。

以下の場合は、ルール確定前に深掘りが必要です。

```text
案件ごとにルールが変わる
正とする資料が決まっていない
命名規則が明文化されていない
例外処理が多い
```

---

## 7. HumanReviewRequired の判定ルール

### 7.1 概要

`HumanReviewRequired` は、AIや自動化の出力を人間が確認し、最終判断すべきユースケースを示します。

---

### 7.2 TRUEにする条件

以下のいずれかに該当する場合、`HumanReviewRequired=True` とします。

```text
RiskLevel が High
RequiresDesignJudgment が TRUE
RequiresLegalJudgment が TRUE
RequiresConstructionJudgment が TRUE
DecisionType が RiskReview
DecisionType が DecisionMaking
RFI、設計変更、施工判断、法規確認、契約責任、安全判断に関係する
CandidateDXService が Human-reviewed を含む
```

---

### 7.3 代表例

```text
UC-005 RFI draft support
UC-007 Construction issue classification
UC-008 Drawing revision impact review
UC-010 Facility management handover data check
```

---

### 7.4 注意点

人間レビュー必須のユースケースでは、AIの役割は以下に限定します。

```text
情報整理
要約
候補提示
論点整理
確認項目の抽出
ドラフト作成
```

AIが最終判断してはいけません。

---

## 8. DeepDiveRequired の判定ルール

### 8.1 概要

`DeepDiveRequired` は、初期ユースケース情報だけではAI/DXサービスの具体的なアウトラインを作れないため、追加ヒアリングや詳細資料確認が必要なユースケースを示します。

---

### 8.2 TRUEにする条件

以下のいずれかに該当する場合、`DeepDiveRequired=True` とします。

```text
入力CSVの DeepDiveRequired が TRUE
RiskLevel が High
Stakeholders が複数いる
DeepDiveReason が空欄ではない
RequiresDesignJudgment が TRUE
RequiresLegalJudgment が TRUE
RequiresConstructionJudgment が TRUE
業務ルール、責任範囲、正とする資料、例外処理が不明確である
```

---

### 8.3 代表例

```text
UC-002 Room name consistency check
UC-003 COBie Component.Space validation
UC-004 BIM rule explanation assistant
UC-005 RFI draft support
UC-007 Construction issue classification
UC-008 Drawing revision impact review
UC-009 Equipment list comparison
UC-010 Facility management handover data check
```

---

### 8.4 注意点

DeepDiveRequired は、PoC 2 の重要な出力です。

初期整理は「広く浅く」行い、DXサービス候補が見えてきた業務について、次に「狭く深く」確認する対象を抽出するために使います。

---

## 9. OutOfScope の判定ルール

### 9.1 概要

`OutOfScope` は、AI/DX支援の対象外、またはAIが扱うべきでない判断を示します。

---

### 9.2 TRUEにする条件

以下のような場合、`OutOfScope=True` とします。

```text
AIが設計可否を最終判断する
AIが施工可否を最終判断する
AIが法規適合を断定する
AIが契約責任を判断する
AIが安全上の最終判断をする
AIがコスト・契約・責任範囲を単独で決める
実案件データや顧客機密情報を前提にしている
社内サービスの詳細再現に該当する
```

---

### 9.3 本MVPでの扱い

本MVPのサンプル10件は、すべて架空ユースケースであり、AIの最終判断を前提としていません。

そのため、基本的には以下とします。

```text
OutOfScope=False
```

ただし、将来的にAIが最終判断する内容を含むユースケースが追加された場合は、`OutOfScope=True` とします。

---

## 10. RecommendedApproach の決定方針

Python処理では、各分類結果をもとに `RecommendedApproach` を決定します。

候補は以下です。

```text
Rule-based Check + Human Review
RAG Assistant + Human Review
BI Dashboard
Automation Support
Data Structuring First
DX Service Candidate Review
Deep Dive Required
Out of Scope
```

---

### 10.1 優先順位

`RecommendedApproach` は、以下の優先順位で決定します。

```text
1. OutOfScope=True
   → Out of Scope

2. HumanReviewRequired=True かつ RAGSuitable=True
   → RAG Assistant + Human Review

3. HumanReviewRequired=True かつ RuleBasedCheckSuitable=True
   → Rule-based Check + Human Review

4. HumanReviewRequired=True
   → DX Service Candidate Review

5. RuleBasedCheckSuitable=True
   → Rule-based Check + Human Review

6. RAGSuitable=True
   → RAG Assistant + Human Review

7. BISuitable=True
   → BI Dashboard

8. AutomationSuitable=True
   → Automation Support

9. DeepDiveRequired=True
   → Deep Dive Required

10. 上記に該当しない
   → Data Structuring First
```

---

### 10.2 注意点

`RecommendedApproach` は、最終的なサービス方針ではありません。
あくまで、関係者との協議や追加ヒアリングに進むための初期分類結果です。

---

## 11. Reason の生成方針

Python処理では、分類結果に応じて `Reason` を生成します。

Reason には、以下のような内容を含めます。

```text
なぜその分類になったか
どの入力項目を根拠にしたか
なぜ人間レビューが必要か
なぜ深掘りが必要か
どのAI/DX支援パターンが候補になるか
```

例：

```text
This use case is suitable for rule-based checking because it uses structured BIM schedule data and focuses on missing value detection.
```

```text
Human review is required because this use case may affect design, construction, legal, or responsibility-related decisions.
```

---

## 12. 本PoCにおける重要な前提

本PoCでは、以下を前提とします。

```text
AI分類結果は最終判断ではない
AI/DX活用候補を整理するための初期分類である
判断が必要な業務では人間レビューを必須にする
初期情報だけでは不十分な業務は深掘り対象にする
実案件データ、顧客名、社内サービス詳細は使用しない
```

---

## 13. MVPで想定する分類結果の例

| UseCaseId | UseCaseName                             | 主な分類イメージ                                                       |
| --------- | --------------------------------------- | -------------------------------------------------------------- |
| UC-001    | Door schedule quality check             | RuleBasedCheckSuitable / BISuitable                            |
| UC-002    | Room name consistency check             | RuleBasedCheckSuitable / BISuitable / DeepDiveRequired         |
| UC-003    | COBie Component.Space validation        | RuleBasedCheckSuitable / AutomationSuitable / DeepDiveRequired |
| UC-004    | BIM rule explanation assistant          | RAGSuitable / DeepDiveRequired                                 |
| UC-005    | RFI draft support                       | RAGSuitable / HumanReviewRequired / DeepDiveRequired           |
| UC-006    | Meeting minutes summarization           | AutomationSuitable                                             |
| UC-007    | Construction issue classification       | BISuitable / HumanReviewRequired / DeepDiveRequired            |
| UC-008    | Drawing revision impact review          | HumanReviewRequired / DeepDiveRequired                         |
| UC-009    | Equipment list comparison               | RuleBasedCheckSuitable / AutomationSuitable / DeepDiveRequired |
| UC-010    | Facility management handover data check | RAGSuitable / HumanReviewRequired / DeepDiveRequired           |

---

## 14. 次工程との関係

この分類ルールは、次工程で作成する以下のPythonスクリプトに反映します。

```text
src/classify_ai_use_cases.py
```

このスクリプトでは、入力CSVを読み込み、各ユースケースに対して分類ルールを適用し、以下の出力を生成します。

```text
output/ai_use_case_mapping_v001.csv
output/human_review_required_use_cases_v001.csv
output/rag_candidate_use_cases_v001.csv
output/automation_candidate_use_cases_v001.csv
```
