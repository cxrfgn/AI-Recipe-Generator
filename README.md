# AI 个性化食谱生成器

简体中文说明（项目根仓库）。本项目是一个教学/演示级的全栈示例：前端表单收集用户口味/忌口/健康目标，后端使用 Flask + SQLAlchemy 存储与筛选食谱，并返回推荐结果。

## 功能简介
- 接收用户偏好（口味 taste、忌口 exclusions、健康目标 health_goal）并返回推荐食谱列表
- 后端使用规则化的匹配与打分逻辑（考虑标签、菜系、名称、食材、减脂优先低卡等）
- 忌口严格排除匹配到的配方
- 自动在空数据库时插入少量示例数据，方便开发和手动调试
- 支持跨域（已使用 flask-cors）以便前端在 Live Server 上调试

## 技术栈
- Python 3.8+（项目使用虚拟环境 `venv` 管理）
- Flask（后端 HTTP API）
- Flask-SQLAlchemy / SQLite（ORM 与持久化）
- flask-cors（允许前端跨域请求）
- JavaScript（前端，Vanilla JS，使用 fetch 调用 API）

## 项目结构（关键文件）
- `backend/app.py` - Flask 后端主程序（包含模型、/generate 路由、数据库自动种子逻辑）
- `app.py` - 仓库根的另一个 Flask 实现（可用作备用或在不使用 `backend` 时运行）
- `frontend/index.html` - 前端页面（可用 Live Server 打开）
- `frontend/script.js` - 前端逻辑（收集表单并 POST 到后端）
- `static/` - Flask 静态文件目录（若通过 Flask 提供前端）
- `database/recipe_db.db` - SQLite 数据库文件（由应用自动创建）
- `populate_db.py` / `check_db.py` / `diagnose_backend.py` - 辅助脚本（插入样例、检查 DB、诊断请求）
- `requirements.txt` - Python 依赖（如有）

## 先决条件
- Windows（本文档以 PowerShell 为例）
- 已安装 Python（建议 3.8+），并能通过 `python` 命令运行
- VS Code（可选，用于 Live Server 插件）

## 在 Windows PowerShell 中的快速启动（推荐）
下面的命令假设你的仓库位于 `D:\工程实践作业\AI-Recipe-Generator`。

1. 打开 PowerShell，切换到项目根：
```powershell
cd "D:\工程实践作业\AI-Recipe-Generator"
```

2. 激活后端虚拟环境（可选但推荐）：
```powershell
.\backend\venv\Scripts\Activate.ps1
# 若提示执行策略错误，可在管理员权限下临时允许：
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

3. 安装依赖（若尚未安装）：
```powershell
python -m pip install -r requirements.txt
```

4. 启动后端（在该窗口不要按 Ctrl+C，保持运行）：
```powershell
python .\backend\app.py
```
启动成功后你应看到类似：
```
* Running on http://127.0.0.1:5000
```

5. 打开前端进行调试：
- 方案 A（推荐用于快速调试）：使用 Live Server（VS Code 插件）打开 `frontend/index.html`，地址通常是 `http://127.0.0.1:5500/frontend/index.html`。
- 方案 B：由 Flask 提供静态文件，直接访问 `http://127.0.0.1:5000/`（仓库根或 `backend` 的 `app.py` 中的路由可能不同）。

6. 在前端选择偏好并点击“生成我的食谱”，页面会向 `http://127.0.0.1:5000/generate` 发送 POST 请求并显示结果。

## 诊断命令（PowerShell）
如果前端显示 `未获取到食谱数据，请重试` 或浏览器 DevTools 报 `Failed to fetch`，按顺序运行下面命令并保存输出用于排查：

1) 在另一个 PowerShell 窗口里（后端在运行的情况下）直接发起 POST：
```powershell
cd "D:\工程实践作业\AI-Recipe-Generator"
$body = @{ taste = '辣'; exclusions = '牛奶'; health_goal = '减脂' } | ConvertTo-Json
Invoke-RestMethod -Uri 'http://127.0.0.1:5000/generate' -Method Post -Body $body -ContentType 'application/json'
```
这将返回 JSON（食谱数组）或显示错误。注意：不能直接在浏览器地址栏打开 `/generate`，那会以 GET 请求发送并返回 `Method Not Allowed`。

2) 快速诊断脚本（仓库已提供），它会输出 GET /、POST /generate 结果并检查 `flask-cors`：
```powershell
& "D:\工程实践作业\AI-Recipe-Generator\backend\venv\Scripts\python.exe" "D:\工程实践作业\AI-Recipe-Generator\diagnose_backend.py"
```

3) 检查 `flask-cors` 是否已安装（若浏览器提示 CORS 错误时执行）：
```powershell
& "D:\工程实践作业\AI-Recipe-Generator\backend\venv\Scripts\python.exe" -m pip show flask-cors
# 若未安装：
& "D:\工程实践作业\AI-Recipe-Generator\backend\venv\Scripts\python.exe" -m pip install flask-cors
```

## 数据库与示例数据
- 项目会在 `database/recipe_db.db` 下创建 SQLite 文件。
- 后端包含“若数据库为空则自动插入少量示例配方”的逻辑，首次启动应用时会自动填充，便于前端开发与演示。
- 如需手动插入或查看数据，可使用仓库中的 `populate_db.py` / `check_db.py`，或使用任何 SQLite 客户端查看 `database/recipe_db.db`。

## 常见问题与排查
- 问：浏览器地址栏打开 `/generate` 显示 `Method Not Allowed`。
   答：该接口只支持 POST，请用前端表单或上面的 PowerShell POST 命令调用。
- 问：点击前端按钮看到 `未获取到食谱数据，请重试`。
   答：可能后端返回了空数组（筛选逻辑排除了所有配方），或后端未运行，或前端 fetch 出错。请按“诊断命令”执行 POST 并把输出粘来排查。
- 问：浏览器报 `Failed to fetch` 或 CORS 错误。
   答：确认 `flask-cors` 已安装且后端启用了 CORS（`backend/app.py` 已包含）。如报 CORS，请把浏览器 DevTools 的 Console 与 Network → `/generate` → Response 的错误原文粘来。

## 运行测试（若提供）
- 项目可包含 pytest 单元测试（若存在 `test_*.py`），在 venv 下运行：
```powershell
& "D:\工程实践作业\AI-Recipe-Generator\backend\venv\Scripts\python.exe" -m pytest
```

## 变更记录（关键）
- 在 `backend/app.py` 中添加了：
   - `/generate` 路由的实现（支持 JSON POST）；
   - 数据库空时自动插入示例配方的种子逻辑；
   - 使用 `flask-cors` 启用跨域，方便前端在 Live Server 调试。

## 帮助与下一步
如果你在某一步遇到困难，请按顺序把下面这些内容原样粘回给我：
1. 后端启动时的完整启动日志（包含 `Running on http://127.0.0.1:5000`）
2. 在 PowerShell 里执行 POST `/generate` 的输出（或诊断脚本输出）
3. 若浏览器仍失败：DevTools → Console 的红色错误文本与 Network → /generate → Response 的文本

我会根据你贴回的输出，直接修改代码或给出具体可复制的命令来修复问题。

---
谢谢你使用这个项目，若你希望我把前端改成内嵌到 Flask（避免跨域和 Live Server），或希望我添加更多示例配方／更复杂的匹配策略，我可以继续实现。
# AI-Recipe-Generator

## 项目简介
AI-Recipe-Generator 是一个基于人工智能的个性化食谱生成器，旨在为用户提供定制化的生活类食谱推荐。

## 技术栈
- 后端：Flask
- 前端：纯 JavaScript
- 数据库：SQLite

## 安装步骤
1. 克隆或下载本项目到本地。
2. 进入项目根目录下的 backend 文件夹：
   ```powershell
   cd backend
   ```
3. 创建并激活 Python 虚拟环境：
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. 安装后端依赖：
   ```powershell
   pip install -r requirements.txt
   ```

## 运行说明
1. 启动 Flask 服务器：
   ```powershell
   python app.py
   ```
2. 默认服务运行在 http://localhost:5000 ，可在浏览器访问。

## 目录结构
- backend/    后端服务代码
- frontend/   前端页面代码
- database/   数据库相关文件
