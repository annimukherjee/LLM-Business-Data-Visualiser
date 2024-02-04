# App Screenshot

experimental project that leverages Large Language Models (LLMs) to achieve Text-to-SQL parsing for Business Analysts.



<p style="width:20%; margin:auto;">
  <img src="https://github.com/annimukherjee/corridor/assets/85307430/97ea6aca-c49a-4de9-afcd-592d737b8d2d" />
</p>


## Dataset Used
[WikiSQL](https://github.com/salesforce/WikiSQL): A large semantic parsing dataset consisting of 80,654 natural statement expressions and sql annotations of 24,241 tables. Each query in WikiSQL is limited to the same table and does not contain complex operations such as sorting, grouping The queries in WikiSQL are limited to the same table and do not include complex operations such as sorting, grouping, subqueries, etc.

| Dataset 	| Split 	| # samples 	|
|:---:	|:---:	|:---:	|
| wikisql 	| train 	| 56355 	|
| wikisql 	| valid 	| 14436 	|

## Model Used

🤗: `mrm8488/t5-base-finetuned-wikiSQL`
