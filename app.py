"""
售后AI智能助手 — 统一导航门户
"""

import streamlit as st
import socket

st.set_page_config(page_title="售后AI智能助手", page_icon="🤖", layout="wide")

SYSTEMS = [
    {"id": "p1", "name": "客诉智能分类系统", "icon": "🔍", "ver": "v3.2", "port": 8501,
     "desc": "双引擎对比 + 优先级评估 + 批量异常检测", "color": "#2196F3"},
    {"id": "p2", "name": "VOC批量异常风险识别与预警系统", "icon": "🚨", "ver": "v3.2", "port": 8502,
     "desc": "统计聚类 + AI语义聚类 + 趋势预测 + 一键报告", "color": "#FF5722"},
    {"id": "p3", "name": "AI客服对话质检系统", "icon": "🎧", "ver": "v3.2", "port": 8503,
     "desc": "4维评分 + 雷达图 + 对话高亮 + 客服对比", "color": "#4CAF50"},
    {"id": "p4", "name": "智能总结概要系统", "icon": "📝", "ver": "v1.2", "port": 8504,
     "desc": "多源输入 + AI摘要 + 事件分类 + 准确度评估", "color": "#9C27B0"},
]

def check(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        r = s.connect_ex(("127.0.0.1", port)) == 0
        s.close()
        return r
    except:
        return False

# Header
st.markdown("<h1 style='text-align:center'>🤖 售后AI智能助手</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#888'>四系统聚合平台 | Ollama · DeepSeek · Gemini · Groq</p>", unsafe_allow_html=True)
st.divider()

# Status bar
cols = st.columns(4)
for i, s in enumerate(SYSTEMS):
    up = check(s["port"])
    cols[i].metric(f"{s['icon']} {s['name'][:8]}...", s["ver"], delta="🟢 运行中" if up else "🔴 离线")

st.divider()

# Cards
for i in range(0, 4, 2):
    c1, c2 = st.columns(2)
    for col, sys in [(c1, SYSTEMS[i]), (c2, SYSTEMS[i+1])]:
        with col:
            up = check(sys["port"])
            with st.container(border=True):
                st.markdown(f"### {sys['icon']} {sys['name']}")
                st.caption(f"{sys['ver']} | 端口 {sys['port']} | {'🟢 在线' if up else '🔴 离线'}")
                st.markdown(sys["desc"])
                if up:
                    st.markdown(f'<a href="http://localhost:{sys["port"]}" target="_blank"><button style="background:{sys["color"]};color:white;border:none;padding:10px 24px;border-radius:8px;cursor:pointer;width:100%;font-size:16px;font-weight:bold;">🚀 打开系统</button></a>', unsafe_allow_html=True)
                else:
                    st.warning("系统未启动")
