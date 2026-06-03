"""
AI 服务运营助手作品集 — 统一展示门户
"""

import streamlit as st

st.set_page_config(
    page_title="AI 服务运营助手作品集",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SYSTEMS = [
    {
        "name": "VOC 智能分类与优先级评估",
        "short": "分类",
        "version": "v3.2",
        "value": "将客诉文本转化为类别、情绪、优先级和处理建议，帮助一线快速分流。",
        "evidence": "对应携程 AI 智能化投诉系统与投诉业务分类经验。",
        "features": ["规则/AI 双引擎", "优先级评估", "批量异常检测", "可视化看板"],
        "scenario": "一线接到大量客诉后，需要快速判断问题类型、紧急程度和处理方向。",
        "analysis": "把非结构化文本拆成分类标签、情绪、优先级和建议动作。",
        "output": "分类结果、优先级、处理建议、异常聚集提示。",
        "tooling": "规则引擎负责稳定分类兜底，AI 模型负责语义理解和复杂表达判断，人工负责低置信度复核。",
        "url": "https://complaint-classifier-crxmkw4rzhybwb5ksusx2d.streamlit.app",
    },
    {
        "name": "批量异常识别与服务风险预警",
        "short": "预警",
        "version": "v3.2",
        "value": "识别 VOC 聚集、敏感风险和时间异常，把潜在舆情从事后复盘前移到事中预警。",
        "evidence": "对应携程智慧预警平台与拼多多批量异常客诉处理经验。",
        "features": ["统计聚类", "敏感词识别", "时间异常检测", "风险报告"],
        "scenario": "运营需要从大量用户声音中发现正在聚集的问题，而不是逐条人工阅读。",
        "analysis": "把 VOC 拆成事件类型、聚集程度、时间异常、升级风险和影响范围。",
        "output": "异常主题、风险等级、趋势判断、响应建议和 Markdown 报告。",
        "tooling": "统计聚类发现聚集，敏感词规则识别确定性风险，AI 引擎补充语义聚类和根因总结。",
        "url": "https://voc-risk-detector-mgneov7ezrugngxdwoynzf.streamlit.app",
    },
    {
        "name": "客服对话质量评估",
        "short": "质检",
        "version": "v3.2",
        "value": "围绕识别需求、有效共情、达成一致、承诺回复四个维度评估服务质量。",
        "evidence": "对应携程 AI 质检平台的业务侧评估标准设计。",
        "features": ["四维评分", "规则/AI 评估", "雷达图", "问题定位"],
        "scenario": "质检团队需要把主观的服务好不好拆成可复核、可训练的评价标准。",
        "analysis": "把对话质量拆成需求识别、共情、方案一致和承诺回复四个维度。",
        "output": "维度评分、问题定位、改进话术和 badcase 清单。",
        "tooling": "规则标准保证评分口径稳定，AI 负责理解对话语义，人工质检负责争议样本复核。",
        "url": "https://cs-quality-evaluator-kwkg6qntv2gwruquwijmgp.streamlit.app",
    },
    {
        "name": "服务事件智能摘要",
        "short": "摘要",
        "version": "v2.0",
        "value": "把对话、日志和备注压缩为结构化摘要，降低工单录入和复盘分析成本。",
        "evidence": "对应携程 AI 自动总结项目，复现 Prompt 约束和格式化输出思路。",
        "features": ["多源输入", "实体提取", "结构化摘要", "人工评分反馈"],
        "scenario": "客服处理后需要把分散对话和操作记录整理成后续角色可读的信息。",
        "analysis": "把长文本拆成事件类型、关键事实、用户诉求、处理动作和待跟进事项。",
        "output": "结构化摘要、风险等级、关键词保留率和人工评分反馈。",
        "tooling": "Prompt 约束输出结构，规则提取关键字段，人工评分反馈用于判断摘要是否可用。",
        "url": "https://summary-system-4.streamlit.app",
    },
    {
        "name": "客服 SOP 知识库问答",
        "short": "RAG",
        "version": "v1.0",
        "value": "把服务 SOP、质检标准和风险规则转为可检索知识库，输出带引用依据的处理建议。",
        "evidence": "用于补齐 RAG / 知识库应用证据，展示从规则文档到问答原型的产品转译能力。",
        "features": ["文档切分", "TF-IDF 检索", "引用依据", "结构化回答"],
        "scenario": "一线或主管需要快速找到 SOP、风险规则和质检标准中的依据。",
        "analysis": "把知识文档拆成可检索片段，并将问题匹配到相关规则和历史口径。",
        "output": "引用依据、判断逻辑、建议动作和人工确认边界。",
        "tooling": "检索负责找依据，生成负责组织回答，人工负责确认规则适用性和高风险边界。",
        "url": "https://service-rag-demo.streamlit.app",
    },
]

WORKFLOW = [
    ("1", "识别问题", "VOC 分类与优先级评估"),
    ("2", "判断风险", "批量异常与舆情预警"),
    ("3", "评估质量", "客服对话质检"),
    ("4", "检索知识", "SOP 知识库问答"),
    ("5", "沉淀信息", "服务事件智能摘要"),
    ("6", "统一入口", "降低工具切换成本"),
]


def inject_css():
    st.markdown(
        """
        <style>
        .block-container { padding-top: 2.2rem; padding-bottom: 2.5rem; }
        .hero {
            border: 1px solid #d9e2ec;
            border-radius: 8px;
            padding: 28px 30px;
            background: #f8fafc;
        }
        .hero h1 {
            margin: 0 0 10px 0;
            font-size: 34px;
            letter-spacing: 0;
            color: #102a43;
        }
        .hero p {
            margin: 0;
            color: #52606d;
            font-size: 16px;
            line-height: 1.7;
        }
        .section-title {
            font-size: 22px;
            font-weight: 700;
            color: #102a43;
            margin: 18px 0 10px 0;
        }
        .workflow-step {
            border: 1px solid #d9e2ec;
            border-radius: 8px;
            padding: 14px;
            min-height: 124px;
            background: white;
        }
        .workflow-index {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: #0f766e;
            color: white;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 8px;
        }
        .system-card {
            border: 1px solid #d9e2ec;
            border-radius: 8px;
            padding: 20px;
            background: white;
            min-height: 290px;
        }
        .system-card h3 {
            margin-top: 0;
            color: #102a43;
            font-size: 20px;
        }
        .muted { color: #627d98; font-size: 14px; line-height: 1.65; }
        .tag {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 6px;
            background: #e6fffa;
            color: #0f766e;
            font-size: 13px;
            margin: 0 6px 6px 0;
            border: 1px solid #b2f5ea;
        }
        .demo-button {
            display: block;
            text-align: center;
            padding: 10px 12px;
            border-radius: 8px;
            background: #0f766e;
            color: white !important;
            text-decoration: none;
            font-weight: 700;
            margin-top: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero():
    st.markdown(
        """
        <div class="hero">
            <h1>AI 服务运营助手作品集</h1>
            <p>
            这是一组基于真实服务运营经验拆解出的 Streamlit Demo，覆盖 VOC 分类、风险预警、
            对话质检、RAG 知识库问答、事件摘要和统一入口。它展示的不是单点工具，而是一条从"分类 → 风险识别 → 质量评估 → 知识检索 → 摘要沉淀 → 统一入口"
            的服务 AI 工作流。
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metrics():
    cols = st.columns(4)
    cols[0].metric("业务 Demo", "5 个", "VOC/预警/质检/RAG/摘要")
    cols[1].metric("统一门户", "1 个", "AI 助手门户")
    cols[2].metric("默认演示", "无需 Key", "规则/统计引擎")
    cols[3].metric("作品定位", "AI 服务运营", "服务治理场景")


def render_workflow():
    st.markdown('<div class="section-title">服务 AI 工作流</div>', unsafe_allow_html=True)
    cols = st.columns(6)
    for col, (index, title, desc) in zip(cols, WORKFLOW):
        with col:
            st.markdown(
                f"""
                <div class="workflow-step">
                    <div class="workflow-index">{index}</div>
                    <div><strong>{title}</strong></div>
                    <div class="muted">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_system_card(system):
    tags = "".join(f'<span class="tag">{feature}</span>' for feature in system["features"])
    st.markdown(
        f"""
        <div class="system-card">
            <h3>{system["short"]} · {system["name"]}</h3>
            <div class="muted"><strong>{system["version"]}</strong> | Streamlit Cloud | 点击后如休眠会自动唤醒</div>
            <p>{system["value"]}</p>
            <div class="muted"><strong>使用场景：</strong>{system["scenario"]}</div>
            <div class="muted"><strong>分析需求：</strong>{system["analysis"]}</div>
            <div class="muted"><strong>功能输出：</strong>{system["output"]}</div>
            <div class="muted"><strong>AI/工具调配：</strong>{system["tooling"]}</div>
            <div class="muted">{system["evidence"]}</div>
            <div style="margin-top:14px;">{tags}</div>
            <a class="demo-button" href="{system["url"]}" target="_blank">体验 Demo</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_systems():
    st.markdown('<div class="section-title">Demo 入口</div>', unsafe_allow_html=True)
    for row_start in range(0, len(SYSTEMS), 2):
        cols = st.columns(2)
        for offset, col in enumerate(cols):
            index = row_start + offset
            if index < len(SYSTEMS):
                with col:
                    render_system_card(SYSTEMS[index])


def render_notes():
    st.markdown('<div class="section-title">产品思维拆解方式</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(
            """
            | 产品拆解层 | 展示重点 |
            |---|---|
            | 业务场景 | 谁在什么业务节点遇到什么问题 |
            | 功能需求 | 需要系统判断、提取、监控或沉淀什么 |
            | AI/工具调配 | 哪些交给规则，哪些交给 AI，哪些保留人工复核 |
            | 输出设计 | 给一线、主管或运营什么结果，是否可导出、可复盘 |
            | 验证指标 | 用准确性、误伤/漏报、处理时长、人工修改原因或保留比例验证 |
            """
        )

    st.markdown('<div class="section-title">面试展示提示</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(
            """
            - 默认规则/统计引擎无需 API Key，可直接展示完整流程。
            - 接入 DeepSeek、Gemini、Groq 或本地 Ollama 后，可切换为 AI 增强模式。
            - 样例数据为模拟/脱敏数据，不包含真实用户隐私。
            - 这组 Demo 主要展示业务使用场景和分析需求如何拆解为功能模块，而不是个人能力展示板。
            """
        )

    with st.expander("5 分钟面试演示脚本", expanded=False):
        st.markdown(
            """
            **开场 30 秒**

            这组 Demo 是我把过往服务 AI 项目拆成的 6 个模块：先识别用户问题，再判断风险，再评估服务质量，再检索知识依据，再把复杂记录沉淀成结构化摘要，最后统一入口。门户页的价值是把这些能力统一到一个入口，避免一线员工在多个工具之间切换。

            **第 1 分钟：VOC 分类**

            打开"VOC 智能分类与优先级评估"，加载模拟数据，展示类别、情绪、优先级和处理建议。这里对应我在携程做 AI 自动总结之前，对一线 SOP 和问题类型的拆解能力。

            **第 2 分钟：风险预警**

            打开"批量异常识别与服务风险预警"，加载 200 条模拟 VOC，展示聚类、时间异常和预警面板。这里重点讲：预警不是收集更多信息，而是把正确的信息在正确时间推给正确的人。

            **第 3 分钟：对话质检**

            打开"客服对话质量评估"，填入示例对话，展示四维评分。这里对应 AI 质检项目：把主观的"服务好不好"拆成可评估、可复核的标准。

            **第 4 分钟：RAG 知识库问答**

            打开"客服 SOP 知识库问答"，输入示例问题，展示检索召回、引用依据和结构化回答。这里展示知识治理的能力：把分散的 SOP、质检标准和风险规则转化为可检索、可引用的知识依据。

            **第 5 分钟：智能摘要**

            打开"服务事件智能摘要"，加载示例数据，展示结构化摘要和风险等级。这里对应携程 AI 智能化投诉系统：把多系统信息压缩成后续处理可用的事实摘要。

            **第 6 分钟：门户收束**

            回到门户页，说明这 6 个模块构成一条完整链路：分类 → 风险识别 → 质量评估 → 知识检索 → 摘要沉淀 → 统一入口。

            **收尾 30 秒**

            这组作品不是为了证明我会写 Streamlit，而是证明我能把业务规则、评估标准和 AI 能力翻译成可运行的系统。这也是我想做 AI 产品运营 / AI 服务运营的核心原因。
            """
        )

    with st.expander("可复制到简历的项目表述", expanded=False):
        st.code(
            """AI 服务系统作品集（2026.03 - 至今）
使用 Claude Code + Streamlit 独立构建 AI 服务系统作品集，包含 5 个业务能力 Demo + 1 个统一门户，覆盖 VOC 智能分类、批量异常预警、客服对话质检、RAG 知识库问答、服务事件摘要和 AI 助手门户。项目以"分类 → 风险识别 → 质量评估 → 知识检索 → 摘要沉淀 → 统一入口"为递进逻辑，展示将业务规则、评估标准、知识依据和 Prompt 约束转化为可运行系统的能力。""",
            language="markdown",
        )


def main():
    inject_css()
    render_hero()
    st.write("")
    render_metrics()
    render_workflow()
    render_systems()
    render_notes()
    st.caption("Streamlit Cloud 免费版应用闲置后会休眠，首次打开通常需要等待约 30 秒。")


if __name__ == "__main__":
    main()
