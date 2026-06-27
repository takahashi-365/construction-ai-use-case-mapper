# AI Use Case Mapper 方針

このドキュメントでは、PoC 2: BIM / Construction AI Use Case Mapper の全体方針を定義します。

本PoCは、建設・BIM関連業務のユースケースを、AI/DX活用パターンへ分類し、関係者との協議、追加ヒアリング、DXサービス候補検討につなげるための個人開発ポートフォリオです。

---

## 1. PoC の位置づけ

本PoCは、BIM / Construction AI Readiness Portfolio の第2弾です。

```text
PoC 1:
BIM Data Quality & AI Readiness Assessment PoC

PoC 2:
BIM / Construction AI Use Case Mapper
```

PoC 1 では、Revit / BIMデータをAI活用可能な形に整えるために、データ品質評価、AI Readiness評価、Fix Guide生成、RAG構成検討などを行いました。

PoC 2 では、対象をBIMデータそのものから、建設・BIM関連業務のユースケースへ広げます。

つまり、PoC 1 と PoC 2 の関係は以下です。

```text
PoC 1:
BIMデータをAI活用可能な形に整える

PoC 2:
建設・BIM業務をAI/DX活用候補として整理する
```

共通する考え方は、以下です。

```text
AIに渡す前に、現実の業務・データを構造化する
```

---

## 2. 目的

本PoCの目的は、建設・BIM関連業務ユースケースを、AI/DX活用の観点で整理し、以下のような活用パターンに分類することです。

```text
RAG向き
BI可視化向き
ルールベースチェック向き
自動化支援向き
人間レビュー必須
追加ヒアリング必須
AI/DX支援対象外
```

このPoCは、AIモデルそのものを作ることを目的としていません。

また、AIによる分類結果や推奨結果を、最終判断として扱うことも目的としていません。

本PoCの目的は、AI/DXサービスを検討する前段階として、業務内容、必要データ、関係者、リスク、人間判断の必要性、深掘りの必要性を構造化することです。

---

## 3. 基本思想

本PoCの基本思想は、以下です。

```text
広く浅く → 狭く深く
```

### 広く浅く

初期段階では、建設・BIM関連業務のユースケースを広く浅く整理します。

確認する内容は以下です。

```text
どのような業務か
誰が関係するか
どのフェーズの業務か
どのような入力データを使うか
どのような成果物を出すか
現在どのツールや方法で行っているか
どのような課題があるか
AI/DX活用の候補になりそうか
人間レビューが必要か
追加ヒアリングが必要か
```

この段階では、詳細な業務要件やシステム仕様は確定しません。

---

### 狭く深く

AI/DX活用候補が見えてきた業務について、次に狭く深く確認します。

確認する内容は以下です。

```text
判断基準は何か
正とする資料は何か
関係者は誰か
最終判断者は誰か
入力データ形式は安定しているか
案件ごとの例外はあるか
成果物は誰が使うか
外部提出や契約責任に関係するか
どこまでAIに任せてよいか
どこから人間判断が必要か
```

---

## 4. AI分類結果の扱い

本PoCでは、AI/DX活用分類結果を最終回答として扱いません。

分類結果は、以下のための参考資料として扱います。

```text
関係者との協議
DXサービス候補の検討
優先順位付け
人間レビューが必要な業務の把握
深掘り対象業務の抽出
追加ヒアリング項目の整理
```

重要な前提は以下です。

```text
AI分類結果は答えではない
AI分類結果は自動承認ではない
AI分類結果は専門家判断の代替ではない
AI分類結果は協議用参考資料である
```

---

## 5. 対象とする業務

本PoCでは、架空の建設・BIM関連業務ユースケースを対象とします。

例：

```text
Door schedule quality check
Room name consistency check
COBie Component.Space validation
BIM rule explanation assistant
RFI draft support
Meeting minutes summarization
Construction issue classification
Drawing revision impact review
Equipment list comparison
Facility management handover data check
```

対象領域は以下を想定します。

```text
BIM
設計レビュー
施工管理
COBie
FM
RFI
会議
引渡し
維持管理
```

---

## 6. 対象外

本PoCでは、以下は対象外とします。

```text
実案件データの使用
顧客名の使用
現職サービスの詳細再現
実際の業務カードの使用
社内ノウハウの再現
AIによる設計判断
AIによる施工判断
AIによる法規判断
AIによる契約判断
AIによる安全判断
AIによる最終承認
本番用AI診断システムの構築
機械学習モデルの作成
RAGチャットUIの本格実装
Azure実デプロイ
```

このPoCは、架空サンプルを用いた個人開発ポートフォリオです。

---

## 7. 分類カテゴリ

本PoCでは、各ユースケースを以下の観点で分類します。

| 分類名                    | 内容                          |
| ---------------------- | --------------------------- |
| RAGSuitable            | 文書参照・説明支援・ドラフト作成に向いているか     |
| BISuitable             | 集計・可視化・傾向把握に向いているか          |
| AutomationSuitable     | 繰り返し作業や整理作業の自動化支援に向いているか    |
| RuleBasedCheckSuitable | 明確なルールに基づくチェックに向いているか       |
| HumanReviewRequired    | 人間レビューが必須か                  |
| DeepDiveRequired       | 追加ヒアリングや詳細確認が必要か            |
| OutOfScope             | AI/DX支援対象外、またはAIが扱うべきでない判断か |

---

## 8. 人間レビューの考え方

建設・BIM業務では、AIの出力をそのまま最終判断に使うことは危険です。

以下に関わる業務は、人間レビューを必須とします。

```text
設計判断
施工判断
法規判断
安全判断
契約判断
コスト影響判断
責任範囲の判断
外部提出物の最終承認
```

AIに任せてよい範囲は、主に以下です。

```text
情報整理
要約
分類
候補提示
不整合候補の抽出
ドラフト作成
確認項目の抽出
```

AIが担う部分と、人間が担う部分は明確に分けます。

```text
AI：
整理、抽出、分類、候補提示、ドラフト作成

人間：
確認、判断、承認、責任を伴う意思決定
```

---

## 9. 深掘りの考え方

本PoCでは、初期ユースケース整理だけでAI/DXサービスの具体的なアウトラインを確定しません。

以下のような場合は、`DeepDiveRequired=True` とします。

```text
判断基準が明文化されていない
正とする資料が決まっていない
関係者が複数いる
責任範囲が不明確である
入力データ形式が案件ごとに異なる
例外処理が多い
外部提出物や契約責任に関係する
設計判断、施工判断、法規判断を含む
```

深掘りでは、以下を確認します。

```text
関係者
正とする資料
判断基準
承認フロー
入力データ形式
成果物の利用目的
例外処理
AIに任せてよい範囲
人間レビューが必要な範囲
```

---

## 10. 出力ファイル

本PoCでは、入力CSVをもとに以下の出力を生成します。

```text
output/ai_use_case_mapping_v001.csv
output/human_review_required_use_cases_v001.csv
output/rag_candidate_use_cases_v001.csv
output/automation_candidate_use_cases_v001.csv
output/dx_service_candidates_v001.csv
output/deep_dive_targets_v001.csv
output/discussion_reference_report_v001.md
output/ai_use_case_summary_v001.md
```

それぞれの役割は以下です。

| 出力ファイル                                   | 役割                |
| ---------------------------------------- | ----------------- |
| ai_use_case_mapping_v001.csv             | 全ユースケースのAI/DX分類結果 |
| human_review_required_use_cases_v001.csv | 人間レビュー必須のユースケース一覧 |
| rag_candidate_use_cases_v001.csv         | RAG向きユースケース一覧     |
| automation_candidate_use_cases_v001.csv  | 自動化支援向きユースケース一覧   |
| dx_service_candidates_v001.csv           | DXサービス候補一覧        |
| deep_dive_targets_v001.csv               | 深掘り対象ユースケース一覧     |
| discussion_reference_report_v001.md      | 関係者協議用レポート        |
| ai_use_case_summary_v001.md              | 分類結果のサマリー         |

---

## 11. 実装方針

本PoCのMVPでは、以下の実装にとどめます。

```text
CSV入力
pandasによる分類処理
分類結果CSVの出力
派生CSVの出力
Markdownレポートの生成
pytestによる主要ロジック確認
```

本MVPでは、以下は行いません。

```text
Webアプリ化
Streamlit実装
Neo4j実装
Azure実デプロイ
RAGチャットUI実装
機械学習モデル作成
実案件データ連携
```

将来的な拡張としては、以下を検討できます。

```text
Streamlitによるユースケースマップ表示
RAG候補だけをJSONL化
BI向きユースケースのダッシュボード設計
Neo4j向けノード・リレーションCSV出力
PoC 1のBIM品質チェック結果との連携
英語README整備
Portfolio PDF化
```

---

## 12. 職務経歴との接続

本PoCは、現職での建設業向けAI/DX支援経験を、直接再現するものではありません。

実案件データ、顧客名、社内サービス詳細は使用せず、個人開発ポートフォリオとして抽象化しています。

職務経歴上は、以下の能力を示すための成果物です。

```text
建設・BIM業務を理解する力
業務をAI/DX活用候補として整理する力
RAG、BI、自動化、ルールベースチェックの使い分けを設計する力
人間レビューが必要な業務を切り分ける力
AI解析結果を最終判断ではなく協議材料として扱う力
クライアント業務を技術者に渡せる構造化データへ変換する力
業務側と技術側をつなぐブリッジ力
```

一言で表すと、以下です。

```text
AIに渡す前に、現実の建設・BIM業務を構造化するPoC
```

---

## 13. 本PoCで重視すること

本PoCでは、単にPythonでCSVを処理することだけを重視しません。

重視するのは以下です。

```text
業務理解
分類方針
人間レビュー設計
深掘り設計
協議用参考資料化
実案件データを使わない安全なポートフォリオ化
PoC 1との連続性
転職・職務経歴で説明しやすい構成
```

---

## 14. まとめ

PoC 2: BIM / Construction AI Use Case Mapper は、建設・BIM関連業務をAI/DX活用候補として分類・構造化するための個人開発PoCです。

このPoCでは、AIの出力を最終判断として扱わず、関係者協議のための参考資料として扱います。

また、初期整理では「広く浅く」業務を把握し、AI/DX活用候補が見えた段階で「狭く深く」関係者・判断基準・必要データ・責任範囲を確認する流れを重視します。

本PoCにより、BIMデータだけでなく、建設・BIM業務そのものをAI活用可能な形に整理する力を示します。
