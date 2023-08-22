# utils.py
import uuid

def generate_tid():
    tid = uuid.uuid4()
    tid_string = str(tid).replace("-", "")
    return tid_string
