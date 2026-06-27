# 入力CSV 列定義

このドキュメントでは、`input/construction_ai_use_cases_v001.csv` の入力列を定義します。

このCSVは、建設・BIM関連業務の架空ユースケースを整理し、AI/DX活用パターンへ分類するための入力データです。

分類対象には、RAG、BI可視化、ルールベースチェック、自動化支援、人間レビュー前提のAI支援、追加ヒアリング必須などを含みます。

本PoCでは、実案件データ、顧客データ、社内サービスの詳細情報は使用しません。
あくまで、ポートフォリオ用の架空サンプルデータとして作成します。

---

## 1. 入力CSVファイル

```text
input/construction_ai_use_cases_v001.csv
```

---

## 2. 列一覧

| 列名                           | 内容                                                  |
| ---------------------------- | --------------------------------------------------- |
| UseCaseId                    | ユースケースID。例：UC-001                                   |
| Domain                       | 対象領域。例：BIM、施工管理、COBie、FM、会議                         |
| WorkPhase                    | 業務フェーズ。例：設計、施工、引渡し、維持管理、社内管理                        |
| Role                         | 主な担当者・関係者。例：BIM担当、施工管理者、設計者、FM担当                    |
| UseCaseName                  | ユースケース名                                             |
| CurrentTask                  | 現在行っている業務内容                                         |
| InputData                    | 業務に使用する入力データ・資料                                     |
| OutputData                   | 業務の成果物・出力結果                                         |
| CurrentTool                  | 現在使用しているツール・方法                                      |
| PainPoint                    | 現状の課題・非効率・困りごと                                      |
| DecisionType                 | 判断・支援の種類                                            |
| RiskLevel                    | 業務リスク。Low / Medium / High                           |
| RequiresDomainKnowledge      | 建設・BIMの専門知識が必要か。TRUE / FALSE                        |
| RequiresDesignJudgment       | 設計判断が必要か。TRUE / FALSE                               |
| RequiresLegalJudgment        | 法規・契約・責任判断が必要か。TRUE / FALSE                         |
| RequiresConstructionJudgment | 施工判断・現場判断が必要か。TRUE / FALSE                          |
| DataStructuredness           | データの構造化度。Structured / SemiStructured / Unstructured |
| Frequency                    | 業務頻度。Daily / Weekly / Monthly / ProjectBased        |
| CandidateAIUse               | 想定されるAI活用案                                          |
| CandidateDXService           | 候補となるAI/DX支援パターン                                    |
| Stakeholders                 | 深掘り時に確認すべき関係者                                       |
| DeepDiveRequired             | 追加ヒアリングや詳細確認が必要か。TRUE / FALSE                       |
| DeepDiveReason               | 深掘りが必要な理由                                           |
| DeepDiveQuestion             | 深掘り時に確認すべき質問                                        |

---

## 3. 各列の定義

### UseCaseId

各ユースケースを識別するためのIDです。

例：

```text
UC-001
UC-002
UC-003
```

入力ルール：

```text
UC-XXX の形式にする
IDは重複させない
```

---

### Domain

対象となる業務領域を記入します。

例：

```text
BIM
設計レビュー
施工管理
COBie
FM
会議
RFI
引渡し
```

---

### WorkPhase

ユースケースが発生する業務フェーズを記入します。

例：

```text
設計
施工
引渡し
維持管理
社内管理
```

---

### Role

主に関係する担当者や役割を記入します。

例：

```text
BIM担当
設計者
施工管理者
FM担当
プロジェクトマネージャー
```

---

### UseCaseName

ユースケースの短い名称を記入します。

例：

```text
Door schedule quality check
Room name consistency check
RFI draft support
```

ユースケース名は、GitHub上で見せることも考慮し、英語名で統一してもよいです。

---

### CurrentTask

現在行っている業務内容を記入します。

AI/DX支援を導入する前に、人がどのような作業をしているのかが分かるように記述します。

---

### InputData

業務で使用する入力データ、資料、ファイルを記入します。

例：

```text
Revit Schedule
Excel checklist
Meeting transcript
RFI history
Drawing revision list
COBie spreadsheet
```

---

### OutputData

業務の成果物や出力結果を記入します。

例：

```text
Quality check result
Issue list
Draft response
Summary report
Validation result
```

---

### CurrentTool

現在使用しているツールや方法を記入します。

例：

```text
Revit
Excel
PDF
Email
Teams
Manual review
```

---

### PainPoint

現状の課題、非効率、困りごとを記入します。

例：

```text
手作業の確認に時間がかかる
確認基準が担当者によってばらつく
情報が複数の資料に分散している
引渡し前に不備を見つけにくい
```

---

### DecisionType

その業務で必要となる判断や支援の種類を記入します。

例：

```text
DataCheck
Explanation
DraftSupport
RiskReview
DecisionMaking
Summarization
Classification
Comparison
```

---

### RiskLevel

ユースケースのリスクレベルを記入します。

使用する値：

```text
Low
Medium
High
```

判断目安：

```text
Low：
事務作業、単純作業、繰り返し作業が中心で、リスクが低い業務

Medium：
建設・BIMの専門知識が必要、または成果物の品質に影響する業務

High：
設計判断、施工判断、法規判断、安全判断、コスト判断、契約判断に関わる業務
```

---

### RequiresDomainKnowledge

建設・BIMの専門知識が必要かを記入します。

使用する値：

```text
TRUE
FALSE
```

---

### RequiresDesignJudgment

設計判断が必要かを記入します。

使用する値：

```text
TRUE
FALSE
```

`TRUE` の場合、原則として人間レビュー必須の対象になります。

---

### RequiresLegalJudgment

法規、契約、責任判断が必要かを記入します。

使用する値：

```text
TRUE
FALSE
```

`TRUE` の場合、原則として人間レビュー必須の対象になります。

---

### RequiresConstructionJudgment

施工判断、現場判断、安全判断が必要かを記入します。

使用する値：

```text
TRUE
FALSE
```

`TRUE` の場合、原則として人間レビュー必須の対象になります。

---

### DataStructuredness

入力データの構造化度を記入します。

使用する値：

```text
Structured
SemiStructured
Unstructured
```

定義：

```text
Structured：
CSV、Excel、Revit Schedule、COBieなど、表形式で整理されたデータ

SemiStructured：
RFIログ、議事録、チェックリスト、報告書など、一定の形式はあるが自由記述も含むデータ

Unstructured：
メール、会話、録音文字起こし、図面、写真、自由記述メモなど、構造化されていないデータ
```

---

### Frequency

業務頻度を記入します。

使用する値：

```text
Daily
Weekly
Monthly
ProjectBased
```

---

### CandidateAIUse

想定されるAI活用案を記入します。

例：

```text
未入力項目を検出する
会議内容を要約する
RFI回答案を作成する
施工課題を分類する
BIMルールを参照して説明文を生成する
```

この項目は、あくまで初期案です。
最終判断として扱わないようにします。

---

### CandidateDXService

候補となるAI/DX支援パターンを記入します。

例：

```text
Rule-based quality checker
RAG assistant
BI dashboard
Automation support tool
Human-reviewed AI drafting support
```

この項目も、あくまで候補です。
関係者との協議を通じて、採用可否や優先度を判断します。

---

### Stakeholders

深掘り時に確認すべき関係者を記入します。

例：

```text
BIM担当
設計責任者
施工管理者
FM担当
プロジェクトマネージャー
発注者担当者
```

---

### DeepDiveRequired

追加ヒアリング、追加資料確認、詳細情報共有が必要かを記入します。

使用する値：

```text
TRUE
FALSE
```

初期情報だけではAI/DXサービスのアウトラインを作れない場合は、`TRUE` とします。

---

### DeepDiveReason

深掘りが必要な理由を記入します。

例：

```text
判断基準が明文化されていない
関係者が複数いる
入力データの形式が案件ごとに異なる
人間の責任範囲を確認する必要がある
例外処理が多い
```

---

### DeepDiveQuestion

深掘り時に確認すべき質問を記入します。

例：

```text
最終承認の基準は何か
最終判断者は誰か
正とする資料はどれか
実案件で発生する例外は何か
どこまでAIに任せてよいか
```

---

## 4. 入力データ作成方針

入力CSVは、以下の方針で作成します。

```text
架空のユースケースのみを使用する
実案件名は使用しない
顧客名は使用しない
社内サービスの詳細情報は使用しない
分類できる程度に業務内容を具体化する
初期整理として広く浅い粒度にする
AIの推奨結果を最終判断として扱わない
人間レビューや深掘りが必要な場合は明示する
```

---

## 5. この入力CSVから生成する成果物

この入力CSVをもとに、以下を生成します。

```text
AI/DX活用分類結果CSV
RAG候補ユースケースCSV
自動化候補ユースケースCSV
人間レビュー必須ユースケースCSV
DXサービス候補CSV
深掘り対象CSV
協議用Markdownレポート
Summary Markdown
```

この入力CSVは、AI/DXサービスの詳細要件を決める前段階として、業務ユースケースを整理し、協議・優先順位付け・深掘り対象選定に使うためのものです。
