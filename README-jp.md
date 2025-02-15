# EF API

このリポジトリでは、"EF API" を使用して "EF ソフトウェア" および "デジタルヒューマン" を制御するサンプルコードを提供します。

元々は内部向けに設計された API であり、現在は "TCP ソケット" によって実装されています。ただし、今後のリリースで "HTTP(s) ベースへの移行" および "詳細な API ドキュメントの公開" を予定しています。

## 前提条件

### 1. EFデジタルヒューマンソフトウェア（コミュニティ版）をダウンロード  
最新バージョンは **Windows および Linux** に対応：  
- [Windows Build](https://github.com/evovor/ef_community/releases/download/v0.1.0-alpha/ef_community_win-v0.1.0-alpha.7z)  
- [Linux Build](https://github.com/evovor/ef_community/releases/download/v0.1.0-alpha/ef_community_linux-v0.1.0-alpha.7z)  

✅ "動作確認済み OS": Windows 10, 11 および Ubuntu 22.04  
⚠️ **DirectX 11/12** または **Vulkan** に対応している他のオペレーティングシステムでも動作する可能性があります。


### 2. Python 3 のインストール  
Python 3 がインストールされていることを確認してください：  
- [Python.org](https://www.python.org/downloads/)  
- [Anaconda](https://www.anaconda.com/products/distribution) 

### 3. リポジトリをクローン  
以下のコマンドを実行してリポジトリをクローンしてください：  
```bash
git clone https://github.com/evovor/ef-api.git
```

---

## API サンプルの実行

### ステップ 1：EF ソフトウェアの起動  
EF ソフトウェアを解凍し、起動してください：

**Windows:**  
```bash
start_ef.bat
```
**Linux:**  
```bash
bash start_ef.sh

```

### ステップ 2：サンプルコードの実行  
例えば、"「speak」" デモを実行する場合：  
```bash
cd ef-api
python speak.py
```
正しく設定されていれば、"デジタルヒューマンが話し始めるはずです"。

---

## 今後の改善予定  
現在、以下のアップデートを予定しています：  
✅ API を "TCP から HTTP(s) へ移行"  
✅ API 機能の拡張  
✅ 詳細な API ドキュメントの公開  

バグ報告、フィードバック、または貢献を希望される方は、[issue](https://github.com/evovor/ef-api/issues) を作成するか、"pull request" をお送りください。
