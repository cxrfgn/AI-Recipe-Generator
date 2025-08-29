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
