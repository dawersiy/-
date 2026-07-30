@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo ╔══════════════════════════════════════╗
echo ║   数学知识图谱构建启动器            ║
echo ╚══════════════════════════════════════╝
echo.

:: 检查Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未找到Python，请先安装Python 3
    pause
    exit /b 1
)

:: 解析参数
set MODE=full
set ENRICH_FILE=

:parse
if "%~1"=="" goto run
if "%~1"=="--export" (
    set MODE=export
    shift
    goto parse
)
if "%~1"=="--enrich" (
    set ENRICH_FILE=%~2
    shift
    shift
    goto parse
)
shift
goto parse

:run
if "%MODE%"=="export" (
    echo [1/2] 正则提取原始items...
    python build_graph.py --export output/raw_items.json
    if %errorlevel% neq 0 (
        echo [错误] 提取失败
        pause
        exit /b 1
    )
    echo.
    echo [2/2] 请在Claude Code中运行:
    echo   "读取 prompts/classify.txt, 对 output/raw_items.json 分类"
    echo   将结果保存为 output/enriched.json
    echo   然后运行: run.bat --enrich output/enriched.json
    pause
    exit /b 0
)

:: 全量构建
echo [1/3] 解析论文 + 关键词 + 去重 + 关系 + 布局...
if "%ENRICH_FILE%"=="" (
    python build_graph.py
) else (
    python build_graph.py --enrich "%ENRICH_FILE%"
)
if %errorlevel% neq 0 (
    echo [错误] 构建失败
    pause
    exit /b 1
)

echo.
echo [2/3] 打开可视化...
start "" "output\knowledge_network.html"

echo.
echo [3/3] 完成!
echo.
echo ┌──────────────────────────────────────┐
echo │ 输出文件:                            │
echo │   output/knowledge_network.json      │
echo │   output/knowledge_network.html      │
echo │                                      │
echo │ 下一步 (Claude Code增强):             │
echo │   run.bat --export                   │
echo │   run.bat --enrich output/enriched.json │
echo └──────────────────────────────────────┘
echo.
pause
