"""
HelloMyGene FastAPI 应用
基因图谱分析 Web 服务
"""
import os
import uuid
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.database.init_db import init_database
from src.analysis.reporter import ReportGenerator
from src.models.report import GeneReport


# 初始化应用
app = FastAPI(
    title="HelloMyGene",
    description="个人基因图谱分析系统",
    version="1.0.0"
)

# 配置路径
BASE_DIR = Path(__file__).parent.parent
UPLOAD_DIR = BASE_DIR / "data" / "raw"
TEMPLATES_DIR = BASE_DIR / "src" / "web" / "templates"
STATIC_DIR = BASE_DIR / "src" / "static"

# 确保目录存在
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
STATIC_DIR.mkdir(parents=True, exist_ok=True)

# 配置模板和静态文件
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# 报告缓存
reports_cache: dict[str, GeneReport] = {}


@app.on_event("startup")
async def startup():
    """应用启动时初始化数据库"""
    init_database()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """首页"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    """上传基因型文件"""
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="仅支持 .txt 格式文件")
    
    # 保存文件
    file_id = str(uuid.uuid4())[:8]
    filename = f"{file_id}_{file.filename}"
    filepath = UPLOAD_DIR / filename
    
    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)
    
    # 生成报告
    try:
        generator = ReportGenerator(str(filepath))
        report = generator.generate()
        reports_cache[report.report_id] = report
        
        return {
            "status": "success",
            "report_id": report.report_id,
            "message": f"成功解析 {report.total_variants} 个变异位点",
            "redirect_url": f"/report/{report.report_id}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"分析失败: {str(e)}")


@app.get("/api/report/{report_id}")
async def get_report_json(report_id: str):
    """获取报告 JSON 数据"""
    if report_id not in reports_cache:
        raise HTTPException(status_code=404, detail="报告不存在")
    
    report = reports_cache[report_id]
    return JSONResponse(content=report.model_dump(mode="json"))


@app.get("/report/{report_id}", response_class=HTMLResponse)
async def view_report(request: Request, report_id: str):
    """查看 HTML 报告"""
    if report_id not in reports_cache:
        raise HTTPException(status_code=404, detail="报告不存在")
    
    report = reports_cache[report_id]
    return templates.TemplateResponse("report.html", {
        "request": request,
        "report": report,
    })


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.get("/report/{report_id}/pdf")
async def download_pdf(request: Request, report_id: str):
    """下载 PDF 报告"""
    from fastapi.responses import StreamingResponse
    from xhtml2pdf import pisa
    from reportlab.pdfbase import pdfmetrics
    import io
    
    # 注册中文字体 - 使用 macOS 系统自带的宋体
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    try:
        pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
    except:
        pass  # 字体已注册
    
    if report_id not in reports_cache:
        raise HTTPException(status_code=404, detail="报告不存在")
    
    report = reports_cache[report_id]
    
    # 渲染 HTML
    html_content = templates.TemplateResponse("report_pdf.html", {
        "request": request,
        "report": report,
    }).body.decode("utf-8")
    
    # 生成 PDF
    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(
        io.StringIO(html_content),
        dest=pdf_buffer,
        encoding='utf-8'
    )
    
    if pisa_status.err:
        raise HTTPException(status_code=500, detail="PDF 生成失败")
    
    pdf_buffer.seek(0)
    
    filename = f"GeneReport_{report.sample_id}_{report.report_id}.pdf"
    
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


