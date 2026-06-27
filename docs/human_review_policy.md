# 人間レビュー方針

このドキュメントでは、PoC 2: BIM / Construction AI Use Case Mapper における `HumanReviewRequired` の考え方を定義します。

本PoCでは、AI/DX活用候補を整理しますが、AIの出力を最終判断として扱いません。
特に、設計判断、施工判断、法規判断、契約判断、安全判断、責任判断に関わる業務では、人間レビューを必須とします。

---

## 1. 目的

この方針の目的は、建設・BIM関連業務において、AIに支援させてよい範囲と、人間が最終確認すべき範囲を明確にすることです。

AIは、以下のような作業を支援できます。

```text
情報整理
要約
分類
候補提示
チェック結果の一覧化
確認項目の抽出
説明文のドラフト作成
回答案のドラフト作成
```

一方で、AIは最終判断者にはなりません。

本PoCでは、AIの出力は以下として扱います。

```text
最終回答ではない
自動承認ではない
専門家判断の代替ではない
関係者協議のための参考資料である
```

---

## 2. HumanReviewRequired の基本方針

`HumanReviewRequired=True` は、AIや自動化の出力を人間が確認し、最終判断する必要があるユースケースを示します。

以下のいずれかに該当する場合は、原則として `HumanReviewRequired=True` とします。

```text
RiskLevel が High
RequiresDesignJudgment が TRUE
RequiresLegalJudgment が TRUE
RequiresConstructionJudgment が TRUE
DecisionType が RiskReview
DecisionType が DecisionMaking
RFI、設計変更、施工判断、法規確認、契約責任、安全判断に関係する
CandidateDXService に Human-reviewed が含まれる
```

---

## 3. 人間レビューが必要な判断領域

以下の判断は、AIが最終判断してはいけません。

```text
設計判断
施工判断
法規判断
安全判断
契約判断
コスト影響判断
責任範囲の判断
発注者・施工者・設計者間の合意判断
外部提出物の最終承認
```

これらの領域では、AIはあくまで支援役です。

---

## 4. AIに任せてよい範囲

AIに任せてよい範囲は、主に人間判断の前段階です。

例：

```text
入力データの整理
不足情報の検出
類似項目の抽出
不整合の候補抽出
議事録の要約
アクションアイテムの抽出
RFI回答案のドラフト作成
BIMルール説明文のドラフト作成
チェック結果の集計
深掘り質問の候補作成
```

AIの役割は、判断そのものではなく、判断に必要な情報を整理することです。

---

## 5. AIに任せてはいけない範囲

以下は、AIに任せてはいけない範囲です。

```text
設計内容が正しいと断定する
施工可否を断定する
法規適合を断定する
安全上問題ないと断定する
契約責任を判断する
コスト影響を最終判断する
RFI回答を自動送信する
設計変更を自動承認する
施工方法を自動決定する
発注者への最終回答を自動生成してそのまま送付する
```

このような処理を含む場合は、`OutOfScope=True` または `HumanReviewRequired=True` として扱います。

---

## 6. リスクレベル別の扱い

### Low

`RiskLevel=Low` のユースケースは、主に事務作業、要約、整理、単純な自動化が中心です。

例：

```text
Meeting minutes summarization
Action item extraction
Simple list formatting
```

扱い：

```text
HumanReviewRequired=False でもよい
ただし外部提出する場合は人間確認を行う
```

---

### Medium

`RiskLevel=Medium` のユースケースは、建設・BIMの専門知識や品質に関係する業務です。

例：

```text
Door schedule quality check
Room name consistency check
COBie Component.Space validation
Equipment list comparison
```

扱い：

```text
AIやルールベースチェックで支援可能
ただしチェックルールや正とする資料は人間が確認する
必要に応じて HumanReviewRequired=True にする
```

---

### High

`RiskLevel=High` のユースケースは、設計、施工、法規、契約、安全、責任に関わる可能性がある業務です。

例：

```text
RFI draft support
Drawing revision impact review
Facility management handover data check
```

扱い：

```text
HumanReviewRequired=True とする
AIは情報整理やドラフト作成に限定する
最終判断は専門家または責任者が行う
```

---

## 7. ユースケース別の考え方

### UC-001 Door schedule quality check

想定：

```text
ドアスケジュールの未入力や命名不整合を確認する
```

扱い：

```text
ルールが明確であれば HumanReviewRequired=False でもよい
ただしチェックルールの確定はBIM担当者が行う
```

---

### UC-002 Room name consistency check

想定：

```text
部屋名や部屋番号の整合性を確認する
```

扱い：

```text
命名ルールが案件ごとに異なる可能性があるため、人間確認が必要
初期MVPでは DeepDiveRequired=True とする
```

---

### UC-003 COBie Component.Space validation

想定：

```text
COBieのComponent.Spaceと部屋・スペース情報を突合する
```

扱い：

```text
チェック自体はルールベース化しやすい
ただし引渡し要件や正とするスペース一覧の確認が必要
人間確認を残す
```

---

### UC-004 BIM rule explanation assistant

想定：

```text
BIMルールや品質チェック結果を説明する
```

扱い：

```text
RAGによる説明支援に向いている
ただしルール解釈や修正方針はBIM担当者が確認する
```

---

### UC-005 RFI draft support

想定：

```text
RFIに対する回答案や要約を作成する
```

扱い：

```text
HumanReviewRequired=True
RFIは設計、施工、コスト、責任に影響する可能性がある
AIはドラフト作成までに限定する
最終回答は責任者が確認する
```

---

### UC-006 Meeting minutes summarization

想定：

```text
会議文字起こしから議事録やアクションアイテムを作成する
```

扱い：

```text
HumanReviewRequired=False でもよい
ただし重要な決定事項や外部共有資料として使う場合は人間確認を行う
```

---

### UC-007 Construction issue classification

想定：

```text
施工課題を分類し、優先度や傾向を整理する
```

扱い：

```text
HumanReviewRequired=True
施工判断や現場判断を含む可能性がある
AIは分類や傾向整理に限定する
```

---

### UC-008 Drawing revision impact review

想定：

```text
図面改訂がBIMモデルや関連業務へ与える影響を確認する
```

扱い：

```text
HumanReviewRequired=True
設計判断を含む可能性がある
AIは影響候補の抽出までに限定する
最終的な影響判断は設計者またはBIM担当者が行う
```

---

### UC-009 Equipment list comparison

想定：

```text
BIM、COBie、引渡し資料の設備リストを比較する
```

扱い：

```text
比較作業は自動化しやすい
ただし正とするマスターリストや名称ルールは人間が確認する
```

---

### UC-010 Facility management handover data check

想定：

```text
維持管理に必要な引渡し情報が揃っているか確認する
```

扱い：

```text
HumanReviewRequired=True
FM要件、契約、発注者要件、法的責任に関係する可能性がある
AIは不足情報の整理や確認項目の提示に限定する
```

---

## 8. HumanReviewRequired と RecommendedApproach の関係

`HumanReviewRequired=True` の場合でも、AI/DX支援の対象外になるわけではありません。

むしろ、以下のような人間レビュー前提のAI支援として扱います。

```text
RAG Assistant + Human Review
Rule-based Check + Human Review
Human-reviewed AI drafting support
Human-reviewed risk review support
DX Service Candidate Review
```

重要なのは、AI支援と人間判断を分離することです。

```text
AI：
整理、抽出、分類、候補提示、ドラフト作成

人間：
確認、判断、承認、責任を伴う意思決定
```

---

## 9. 出力上の注意

Python処理で `HumanReviewRequired=True` と判定されたユースケースは、以下の出力に含めます。

```text
output/human_review_required_use_cases_v001.csv
output/ai_use_case_mapping_v001.csv
output/discussion_reference_report_v001.md
```

レポート上では、以下を明記します。

```text
AI出力は最終判断ではない
人間レビューが必要な理由
最終確認すべき関係者
追加で確認すべき論点
```

---

## 10. 本PoCにおける重要な前提

本PoCでは、以下を前提とします。

```text
AIは判断者ではなく、支援者である
AI分類結果は協議用参考資料である
人間レビューは安全なAI/DX活用の前提である
建設・BIM業務では、専門家判断と責任範囲を明確にする必要がある
設計・施工・法規・契約・安全・責任に関わる判断はAIに任せない
```

---

## 11. まとめ

このPoCにおける `HumanReviewRequired` は、AI活用を否定するための項目ではありません。

むしろ、AI/DX支援を安全に使うために、人間が確認すべき領域を明確にするための項目です。

```text
AIに任せる部分：
整理、分類、要約、候補提示、ドラフト作成

人間が担う部分：
確認、判断、承認、責任を伴う意思決定
```

この分離により、建設・BIM業務において、AIを安全かつ現実的に活用する前提を整理します。
