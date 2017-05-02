import subprocess
import datetime
import json

host_id = 'oscompute-x'
comm_file = "memory.txt"

ram = subprocess.Popen("free -m | grep Mem | tr -s ' ' | cut -d ' ' -f 2,3", shell=True, stdout=subprocess.PIPE).stdout.read()
ram = str(ram).split()

record = {}
record['meta'] = {}
record['meta']['host_id'] = host_id
record['meta']['date'] = datetime.datetime.utcnow()
record['stat'] = {}
record['stat']['stat_name'] = "hardware.memory.total"
record['stat']['value'] = str(ram[0])
record['stat']['unit'] = "MB"

record2 = {}
record2['meta'] = {}
record2['meta']['host_id'] = host_id
record2['meta']['date'] = datetime.datetime.utcnow()
record2['stat'] = {}
record2['stat']['stat_name'] = "hardware.memory.used"
record2['stat']['value'] = str(ram[1])
record2['stat']['unit'] = "MB"


r = []
r.append(record)
r.append(record2)


ram2 = subprocess.Popen("sudo iotop -bok --iter=5 -d 5 | grep '|' | tr ':' ' ' | tr -s ' ' | cut -d ' ' -f 10", shell=True, stdout=subprocess.PIPE).stdout.read()


ram2 = str(ram2).split()

i = 0
for j in ram2:
    record = {}
    record['meta'] = {}
    record['meta']['host_id'] = host_id
    record['meta']['date'] = datetime.datetime.utcnow()
    record['stat'] = {}
    record['stat']['value'] = str(j)
    record['stat']['unit'] = "KB/s"
    if int(i) % 2 == 0:
        record['stat']['stat_name'] = "hardware.system_stats.io.total"
    else:
        record['stat']['stat_name'] = "hardware.system_stats.io.used"
    r.append(record)
    i += 1




with open(comm_file) as myfile:
    d = myfile.read()
    if d:
        d = eval(d)
        r += d

if d:
    with open(comm_file, "w") as f:
        f.truncate()


with open(comm_file, "a") as myfile:
    myfile.write(str(r))





