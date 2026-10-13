import shutil

def by_to_gb (usage_type):
   return usage_type / (1024 ** 3)
  
def check_disk(path, limit):
    disk_d={}
    try:
        usage = shutil.disk_usage(path)  
    except FileNotFoundError:
        return None
    disk_d["path"]=path
    disk_d["total"]=round(by_to_gb(usage.total),1)
    disk_d["used"]=round(by_to_gb(usage.used),1)
    disk_d["free"]=round(by_to_gb(usage.free),1)
    disk_d["percent"]=round(usage.used / usage.total * 100,1)
    disk_d["ok"]=(disk_d["percent"]<limit)
    disk_d["limit"]=limit
    return disk_d 
