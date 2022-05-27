ADDR1=172.17.20.237:12345
ADDR2=172.17.20.259:12345
INDEX?=0

run:
	TF_CONFIG='{"cluster": {"worker": ["${ADDR1}", "${ADDR2}"]}, "task": {"type": "worker", "index": ${INDEX}} }' python3 main.py