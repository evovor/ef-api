# EF API

本仓库提供 "EF API" 的示例代码，支持外部控制 "EF数字人 软件" 以及其中运行的 "数字人"。

该 API 最初用于内部开发，目前基于 "TCP Socket" 实现。不过，我们计划迁移到 "HTTP(s)"，并在未来版本中发布完整的 API 文档。

## 环境准备

### 1. 下载 EF数字人 软件（社区版）  
最新版本适用于 **Windows 和 Linux**：  
- [Windows Build](https://github.com/evovor/ef_community/releases/download/v0.1.0-alpha/ef_community_win-v0.1.0-alpha.7z)  
- [Linux Build](https://github.com/evovor/ef_community/releases/download/v0.1.0-alpha/ef_community_linux-v0.1.0-alpha.7z)  

✅ "已测试系统："Windows 10、11 和 Ubuntu 22.04。  
⚠️ 其他支持 **DirectX 11/12** 或 **Vulkan** 的操作系统可能尝试运行。

### 2. 安装 Python 3  
请确保本机已安装 Python 3，可在以下网站下载：  
- "[Python 官网](https://www.python.org/downloads/)"  
- "[Anaconda 官网](https://www.anaconda.com/products/distribution)"  

### 3. 下载本仓库  
在终端执行以下命令克隆仓库：  
```bash
git clone https://github.com/evovor/ef-api.git
```

---

## 运行 API 示例

### "步骤 1：启动 EF"  
解压后运行 EF：  

"Windows："  
```bash
start_ef.bat
```
"Linux："  
```bash
bash start_ef.sh
```

### "步骤 2：运行示例代码"  
例如，运行 ""speak"" 示例：  
```bash
cd ef-api
python speak.py
```
如果环境配置正确，"数字人会开始说话"。

---

## 未来规划  
我们正在推进以下改进：  
✅ 将 API "从 TCP 迁移到 HTTP(s)"。  
✅ 扩展 API 功能，提供更丰富的控制方式。  
✅ 发布完整的 API 文档，优化开发体验。

如果你有任何建议或问题，欢迎提交 "[Issue](https://github.com/evovor/ef-api/issues)" 或发起 "Pull Request"！
