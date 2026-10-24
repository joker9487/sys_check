# sys_check

一個用 Python 寫的系統檢查工具：檢查磁碟使用率、統計 log 檔的錯誤等級。

## 功能
- 磁碟檢查：讀 config.json 的路徑，超過上限發出警告
- log 統計：計算各等級（INFO / ERROR...）數量，存成 `output/summary.json`
- 執行紀錄寫入 `output/sys_check.log`（同時印在畫面上）

## 怎麼跑
```bash
python main.py
python main.py --log app.log --limit 90
python main.py -h
```

| 參數 | 說明 | 預設 |
| --- | --- | --- |
| `--log` | 要分析的 log 檔 | `test.txt` |
| `--limit` | 磁碟上限（%） | 沒給就用 config 的 `disk_limit` |
| `--output` | summary的存檔路徑 | 沒給就用 output/summary.json |

## 設定檔 config.json
```json
{
  "disk_paths": ["Z:/", "C:/"],
  "disk_limit": 95
}
```
- `config.json`：本機（Windows）用
- `config.docker.json`：Docker（Linux）用，路徑是 `/`

## Docker
```bash
# 建 image
docker build -t sys_check .

# 執行（掛上 Linux 用的設定檔）
docker run --rm -v "$PWD/config.docker.json:/app/config.json" sys_check

# 執行並把 output/ 帶回本機
docker run --rm \
  -v "$PWD/config.docker.json:/app/config.json" \
  -v "$PWD/output:/app/output" \
  sys_check

# 帶參數執行（覆蓋 CMD）
docker run --rm -v "$PWD/config.docker.json:/app/config.json" sys_check python main.py --limit 90
```

Windows PowerShell 把 `$PWD` 改成 `${PWD}`，例如：
```powershell
docker run --rm -v "${PWD}/config.docker.json:/app/config.json" -v "${PWD}/output:/app/output" sys_check
```

> image 內的 `config.json` 是 Windows 路徑（`Z:/`、`C:/`），在容器裡會找不到，所以執行時要用 `-v` 掛上 `config.docker.json`。

## 測試
```bash
python -m pytest -v
```
每次 push / PR 會由 GitHub Actions 平行跑兩個 job：`test`（pytest）與 `docker`（build 並執行 image）。

## 專案結構
```
sys_check/
├── main.py                 # 進入點：解析參數、設定 logging、執行檢查
├── config.py               # load_config()：讀 JSON 設定檔
├── disk_check.py           # check_disk()：取得磁碟用量並判斷是否超過上限
├── log_summary.py          # LogSummary：統計 log 各等級數量並存成 JSON
├── config.json             # 本機設定
├── config.docker.json      # Docker 用設定
├── test.txt                # 預設的範例 log
├── test/
│   ├── test_disk_check.py
│   └── test_log_summary.py
├── output/                 # 執行時產生：summary.json、sys_check.log
├── Dockerfile
├── .dockerignore
└── .github/workflows/test.yml   # CI：test（pytest）與 docker（build/run）兩個 job
```
