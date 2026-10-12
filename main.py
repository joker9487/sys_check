-vfrom log_summary import LogSummary

summary = LogSummary()
summary.add_files("test.txt")
print(summary.counts)        
print("total line:",summary.total())       
print("skipped line:",summary.skipped)
summary.save("summary.json")