[English](README.md) | [中文](README_zh.md)

# HelloMyGene (个人基因图谱分析系统)

HelloMyGene 是一个基于 FastAPI 的个人基因图谱分析系统。它允许用户上传基因型数据文件（.txt 格式），并利用 AI 生成详细的基因健康报告，包括疾病风险、药物反应、遗传特征等。

## ✨ 主要功能

- **基因数据上传**: 支持上传常见的基因型原始数据文件（.txt）。
- **智能分析**: 解析基因位点，结合内置知识库进行健康风险评估。
- **可视化报告**: 提供直观的 HTML 交互式报告。
- **PDF 导出**: 支持将基因报告导出为 PDF 格式，方便保存和分享。
- **本地化支持**: 完美支持中文报告生成。

## 🛠️ 技术栈

- **后端框架**: [FastAPI](https://fastapi.tiangolo.com/) - 高性能 Python Web 框架
- **数据库**: SQLite (通过 SQLAlchemy 和 aiosqlite 访问)
- **模板引擎**: Jinja2
- **PDF 生成**: xhtml2pdf & reportlab
- **数据处理**: pandas

## 🚀 快速开始

### 环境要求

- Python 3.12 或更高版本
- [uv](https://github.com/astral-sh/uv) (推荐) 或 pip

### 安装依赖

如果使用 `uv` (推荐):

```bash
uv sync
```

或者使用 `pip`:

```bash
pip install .
```

### 运行应用

开发模式启动（支持热重载）：

```bash
uv run uvicorn src.app:app --reload
```

或者直接运行入口脚本：

```bash
python main.py
```

服务启动后，访问: http://127.0.0.1:8000

## 📖 使用指南

1.  打开浏览器访问首页。
2.  点击上传区域，选择您的基因型数据文件（.txt 格式）。
3.  等待系统解析和分析（通常只需几秒钟）。
4.  查看生成的详细基因报告。
5.  如需保存，点击页面右上角的 "下载 PDF" 按钮。

## 📂 项目结构

```
HelloMyGene/
├── data/               # 数据存储
│   └── raw/            # 原始上传文件
├── src/                # 源代码
│   ├── analysis/       # 分析逻辑 (解析器, 报告生成)
│   ├── database/       # 数据库模型与初始化
│   ├── models/         # Pydantic 数据模型
│   ├── static/         # 静态资源 (CSS, 字体)
│   ├── web/            # Web 前端 (模板)
│   └── app.py          # FastAPI 主应用
├── main.py             # 启动入口
├── pyproject.toml      # 项目配置与依赖
└── README.md           # 项目文档
```

## 📝 许可证

[MIT License](LICENSE)
