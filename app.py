"""
售后AI智能助手 — 统一导航门户
"""

import streamlit as st

st.set_page_config(page_title="售后AI智能助手", page_icon="🤖", layout="wide")

SYSTEMS = [
    {
        "id": "p1", "name": "客诉智能分类系统", "icon": "🔍", "ver": "v3.2",
        "desc": "双引擎对比 + 优先级评估 + 批量异常检测", "color": "#2196F3",
        "url": "https://complaint-classifier-crxmkw4rzhybwb5ksusx2d.streamlit.app",
    },
    {
        "id": "p2", "name": "VOC批量异常风险识别与预警系统", "icon": "🚨", "ver": "v3.2",
        "desc": "统计聚类 + AI语义聚类 + 趋势预测 + 一键报告", "color": "#FF5722",
        "url": "https://voc-risk-detector-mgneov7ezrugngxdwoynzf.streamlit.app",
    },
    {
        "id": "p3", "name": "AI客服对话质检系统", "icon": "🎧", "ver": "v3.2",
        "desc": "4维评分 + 雷达图 + 对话高亮 + 客服对比", "color": "#4CAF50",
        "url": "https://cs-quality-evaluator-kwkg6qntv2gwruquwijmgp.streamlit.app",
    },
    {
        "id": "p4", "name": "智能总结概要系统", "icon": "📝", "ver": "v2.0",
        "desc": "多源输入 + AI摘要 + 双引擎对比 + 人工评分", "color": "#9C27B0",
        "url": "https://summary-system-4.streamlit.app",
    },
]

# Header
st.markdown("<h1 style='text-align:center'>🤖 售后AI智能助手</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#888'>四系统聚合平台 | Ollama · DeepSeek · Gemini · Groq</p>", unsafe_allow_html=True)
st.divider()

# Status bar
cols = st.columns(4)
for i, s in enumerate(SYSTEMS):
    cols[i].metric(f"{s['icon']} {s['name'][:8]}...", s["ver"], delta="☁️ 在线")

st.divider()

# Cards
for i in range(0, 4, 2):
    c1, c2 = st.columns(2)
    for col, sys in [(c1, SYSTEMS[i]), (c2, SYSTEMS[i+1])]:
        with col:
            with st.container(border=True):
                st.markdown(f"### {sys['icon']} {sys['name']}")
                st.caption(f"{sys['ver']} | Streamlit Cloud | 点击即唤醒")
                st.markdown(sys["desc"])
                # 点击直接跳转 Streamlit Cloud，自动唤醒休眠应用
                st.markdown(
                    f'<a href="{sys["url"]}" target="_blank">'
                    f'<button style="background:{sys["color"]};color:white;border:none;'
                    f'padding:10px 24px;border-radius:8px;cursor:pointer;width:100%;'
                    f'font-size:16px;font-weight:bold;">🚀 打开系统（自动唤醒）</button></a>',
                    unsafe_allow_html=True,
                )

st.divider()
st.caption("💡 Streamlit Cloud 免费版应用闲置后会休眠，点击按钮即可自动唤醒（约30秒）")
