# AI 服务运营助手作品集

这是一个基于真实服务运营经验构建的 AI Demo 作品集门户，聚合 4 个 Streamlit 应用：VOC 智能分类、批量异常预警、客服对话质检、服务事件摘要。

作品集的核心不是展示单点工具，而是展示一条服务 AI 工作流：

```text
识别问题 → 判断风险 → 评估质量 → 沉淀信息 → 统一入口
```

## 在线演示

https://ai-assistant-app-msydemo.streamlit.app

## 模块清单

| 模块 | 业务价值 | Demo |
|---|---|---|
| VOC 智能分类与优先级评估 | 将客诉文本转化为类别、情绪、优先级和处理建议 | https://complaint-classifier-crxmkw4rzhybwb5ksusx2d.streamlit.app |
| 批量异常识别与服务风险预警 | 识别 VOC 聚集、敏感风险和时间异常 | https://voc-risk-detector-mgneov7ezrugngxdwoynzf.streamlit.app |
| 客服对话质量评估 | 从四个维度评估客服对话质量 | https://cs-quality-evaluator-kwkg6qntv2gwruquwijmgp.streamlit.app |
| 服务事件智能摘要 | 将对话、日志和备注压缩为结构化摘要 | https://summary-system-4.streamlit.app |

## 项目定位

这组 Demo 对应过往经历中的四类真实业务能力：

- AI 智能客服落地：将服务 SOP、评估标准和 Prompt 约束转为系统能力。
- 智慧预警平台：把潜在舆情和批量问题前置识别。
- AI 质检：把服务质量从主观判断拆成可评估维度。
- 自动总结：降低工单录入、复盘分析和交接协同成本。

## 设计原则

- 默认可演示：规则/统计引擎无需 API Key。
- AI 可增强：接入 DeepSeek、Gemini、Groq 或本地 Ollama 后可切换 LLM 模式。
- 数据可脱敏：样例数据均为模拟数据，不包含真实用户隐私。
- 结果可解释：每个系统都尽量输出规则依据、风险证据或评分理由。

## 技术栈

- Python
- Streamlit
- pandas
- Plotly
- scikit-learn
- Multi-LLM API

## 本地运行

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 面试展示话术

这 5 个 Demo 不是随机练手项目，而是我把过去做过的服务 AI 系统重新拆成五个能力模块：先识别问题是什么，再判断风险有多高，再评估服务质量，再生成结构化摘要，最后统一入口降低工具切换成本。这对应我在携程做 AI 项目时的核心理解：AI 不应该成为新的工具负担，而应该嵌入工作流。

