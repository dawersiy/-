#!/bin/bash
cd "$(dirname "$0")"

echo "╔══════════════════════════════════════╗"
echo "║   数学知识图谱构建启动器            ║"
echo "╚══════════════════════════════════════╝"
echo

# 解析参数
MODE="full"
ENRICH_FILE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --export) MODE="export"; shift ;;
        --enrich) ENRICH_FILE="$2"; shift 2 ;;
        *) shift ;;
    esac
done

if [ "$MODE" = "export" ]; then
    echo "[1/2] 正则提取原始items..."
    python build_graph.py --export output/raw_items.json || exit 1
    echo
    echo "[2/2] 请在Claude Code中运行:"
    echo '  "读取 prompts/classify.txt, 对 output/raw_items.json 分类"'
    echo "  将结果保存为 output/enriched.json"
    echo "  然后运行: ./run.sh --enrich output/enriched.json"
    exit 0
fi

# 全量构建
echo "[1/3] 解析论文 + 关键词 + 去重 + 关系 + 布局..."
if [ -n "$ENRICH_FILE" ]; then
    python build_graph.py --enrich "$ENRICH_FILE" || exit 1
else
    python build_graph.py || exit 1
fi

echo
echo "[2/3] 打开可视化..."
case "$(uname -s)" in
    Darwin*)  open output/knowledge_network.html ;;
    Linux*)   xdg-open output/knowledge_network.html 2>/dev/null || echo "请手动打开: output/knowledge_network.html" ;;
    MINGW*|MSYS*) start "" "output/knowledge_network.html" ;;
esac

echo
echo "[3/3] 完成!"
echo "  输出: output/knowledge_network.json"
echo "  输出: output/knowledge_network.html"
