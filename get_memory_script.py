import subprocess
import datetime
import json

host_id = 'os-compute'
comm_file = "memory.txt"

ram = subprocess.Popen("free -m | grep Mem | tr -s ' ' | cut -d ' ' -f 2,3", shell=True, stdout=subprocess.PIPE).stdout.read()
ram = str(ram).split()

record = {}
record['meta'] = {}
record['meta']['host_id'] = host_id
record['meta']['date'] = datetime.datetime.utcnow()
record['stat'] = {}
record['stat']['stat_name'] = "hardware.memory.total"
record['stat']['value'] = ram[0]
record['stat']['unit'] = "MB"

record2 = {}
record2['meta'] = {}
record2['meta']['host_id'] = host_id
record2['meta']['date'] = datetime.datetime.utcnow()
record2['stat'] = {}
record2['stat']['stat_name'] = "hardware.memory.used"
record2['stat']['value'] = ram[1]
record2['stat']['unit'] = "MB"

print str(record)

r = []
r.append(record)
r.append(record2)

r = json.loads(r)

with open(comm_file, "a") as myfile:
    myfile.write(str(r))



