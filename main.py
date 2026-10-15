from log_summary import LogSummary
from disk_check import check_disk
from config import load_config
import argparse
import logging

def parse_args():
    parser = argparse.ArgumentParser(description="系統檢查工具")
    parser.add_argument("--log", default="test.txt", help="要分析的 log 檔")
    parser.add_argument("--limit", type=int, help="磁碟上限（%%），沒給就用 config")
    return parser.parse_args()

def run_disk_check(paths, limit):
    results = {}
    for path in paths:
        info = check_disk(path, limit)
        if info is None:
            logging.error(f"  {path} 找不到路徑")
            continue
        if info["ok"]:
            logging.info(f"   {path} 使用率 {info['percent']}%")
        else:
            logging.warning(f" {path} 使用率 {info['percent']}%，超過上限 {limit}%")
        results[path] = info
    return results


def run_log_summary(log_path):
    summary = LogSummary()
    summary.add_files(log_path)
    logging.info(f"log 統計：{summary.counts}")
    logging.info(f"總行數：{summary.total()}")
    if summary.skipped > 0:
        logging.warning(f"有 {summary.skipped} 行格式不符，已略過")
        
    summary.save("summary.json")
    return summary

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("sys_check.log", encoding="utf-8"),  # 存檔
            logging.StreamHandler(),                                 # 印畫面
        ],
    )

def main():
    args = parse_args()
    config = load_config("config.json")
    if config is None:
        print("讀取設定失敗")
        return

    if args.limit is not None:
        limit = args.limit
    else:
        limit = config["disk_limit"]

    run_disk_check(config["disk_paths"], limit)
    run_log_summary(args.log)


    




if __name__ == "__main__":
    main()
