/**
 * 数学知识图谱 — Node.js Web 服务器
 * 读取 Python pipeline 生成的 knowledge_network.json 并通过 Web 提供服务
 *
 * 用法:
 *   1. python build_graph.py        (生成 output/knowledge_network.json)
 *   2. npm install && npm start     (启动服务器)
 *   3. 浏览器打开 http://localhost:3000
 */

const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

const OUTPUT_DIR = path.join(__dirname, 'output');
const JSON_PATH = path.join(OUTPUT_DIR, 'knowledge_network.json');

// ── 静态文件服务 ──────────────────────────────────────────────
// public/ 目录: HTML, CSS, JS 前端资源
app.use(express.static(path.join(__dirname, 'public')));

// output/ 目录: Python pipeline 生成的 JSON 数据文件
app.use('/data', express.static(OUTPUT_DIR));

// ── API ───────────────────────────────────────────────────────

// GET /api/graph — 返回完整知识图谱数据
app.get('/api/graph', (req, res) => {
    try {
        if (!fs.existsSync(JSON_PATH)) {
            return res.status(404).json({
                error: '数据文件未找到',
                message: `请先运行 python build_graph.py 生成 ${JSON_PATH}`,
                path: JSON_PATH
            });
        }
        const raw = fs.readFileSync(JSON_PATH, 'utf-8');
        const data = JSON.parse(raw);
        res.json(data);
    } catch (err) {
        console.error('读取图谱数据失败:', err.message);
        res.status(500).json({ error: '数据读取失败', detail: err.message });
    }
});

// GET /api/status — 检查数据文件状态
app.get('/api/status', (req, res) => {
    const exists = fs.existsSync(JSON_PATH);
    let stats = null;
    if (exists) {
        const s = fs.statSync(JSON_PATH);
        stats = { size_kb: (s.size / 1024).toFixed(1), modified: s.mtime.toISOString() };
    }
    res.json({ data_file_exists: exists, stats, json_path: JSON_PATH });
});

// ── 主页 ──────────────────────────────────────────────────────
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// ── 启动 ──────────────────────────────────────────────────────
app.listen(PORT, () => {
    console.log('');
    console.log('╔══════════════════════════════════════════╗');
    console.log('║   Mathematical Knowledge Graph Server   ║');
    console.log('╚══════════════════════════════════════════╝');
    console.log('');
    console.log(`  Server:     http://localhost:${PORT}`);
    console.log(`  Graph API:  http://localhost:${PORT}/api/graph`);
    console.log(`  Status:     http://localhost:${PORT}/api/status`);
    console.log('');

    if (fs.existsSync(JSON_PATH)) {
        const s = fs.statSync(JSON_PATH);
        console.log(`  ✓ 数据文件已就绪 (${(s.size / 1024).toFixed(1)} KB, ${s.mtime.toLocaleString()})`);
    } else {
        console.log('  ⚠ 数据文件未找到 — 请先运行: python build_graph.py');
    }
    console.log('');
});
