from log_summary import LogSummary,read_lines
from disk_check import by_to_gb,check_disk
from config import load_config



print("=== 磁碟檢查 ===")
#讀檔
disk_log = load_config("config.json")

disk_info_d ={}
use_level="OK"
use_warn=""
if( disk_log ):
    for disk_name in disk_log["disk_paths"]:
        disk_info=check_disk(disk_name,disk_log["disk_limit"])
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
else:
    print("設定讀取失敗，結束")

#print("\n=== Log 統計 ===")
# summary = LogSummary()
# summary.add_files("test.txt")
# print(summary.counts)        
# print("total line:",summary.total())       
# print("skipped line:",summary.skipped)
# summary.save("summary.json")




