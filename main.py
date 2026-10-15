from log_summary import LogSummary
from disk_check import check_disk
from config import load_config
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="系統檢查工具")
    parser.add_argument("--log", default="test.txt", help="要分析的 log 檔")
    parser.add_argument("--limit", type=int, help="磁碟上限（%%），沒給就用 config")
    return parser.parse_args()

def run_disk_check(paths, limit):
    disk_info_d ={}
    use_level="OK"
    use_warn=""
    for disk_name in paths:
        disk_info=check_disk(disk_name,limit)
        if (disk_info is None):
            print(f"[ERR]  {disk_name} 找不到路徑")
            continue
        if (not disk_info['ok'] ):
            use_level="WARN"
            use_warn=F"，超過上限 {disk_info['limit']}%"
        else:
            #沒超過
            use_level="OK"
            use_warn=""
        print(f"[{use_level}]   {disk_info['path']} 使用率 {disk_info['percent']}%{use_warn}")

        #儲存資料
        disk_info_d[disk_name]=disk_info
    return disk_info_d


def run_log_summary(log_path):
    summary = LogSummary()
    summary.add_files(log_path)
    print(summary.counts)        
    print("total line:",summary.total())       
    print("skipped line:",summary.skipped)
    summary.save("summary.json")
    return summary


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
