# sys_check

一個用 Python 寫的系統檢查工具：檢查磁碟使用率、統計 log 檔的錯誤等級。

## 功能
- 磁碟檢查：讀 config.json 的路徑，超過上限發出警告
- log 統計：計算各等級（INFO / ERROR...）數量，存成 summary.json
- 執行紀錄寫入 sys_check.log

## 怎麼跑
​```bash
python main.py
python main.py --log app.log --limit 90
python main.py -h
​```

## 設定檔 config.json
{
  "disk_paths": [ "Z:/","C:/"],
  "disk_limit": 95
}

## 測試
​```bash
python -m pytest -v
​```
每次 push 會由 GitHub Actions 自動跑測試。

## 專案結構
（待補）