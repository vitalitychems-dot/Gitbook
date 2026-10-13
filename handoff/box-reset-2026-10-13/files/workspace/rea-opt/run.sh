export PATH=/workspace/tools/node22/bin:$PATH
cd /workspace/rea-opt
for r in stanfordnlp/dspy microsoft/agent-lightning huggingface/smolagents apache/airflow PrefectHQ/prefect temporalio/temporal openai/tiktoken zilliztech/GPTCache a2aproject/A2A langchain-ai/langgraph; do
 n=${r//\//__}; [ -d $n ] || git clone -q --depth 1 --filter=blob:limit=2m https://github.com/$r $n
 git -C $n ls-files > out/$n.files; h=$(git -C $n rev-parse --short HEAD)
 timeout 600 npx -y rea-agents@6.4.0 analyze-javascript-application $n --json > out/$n.json 2> out/$n.err; echo "$n exit=$? size=$(stat -c%s out/$n.json) files=$(wc -l <out/$n.files) head=$h"
 du -sm $n | cut -f1 > out/$n.mb
done; echo ALLDONE
