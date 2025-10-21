import sys
import os
import django
import json
from datetime import datetime
from pathlib import Path

# ✅ Dynamically locate the Django project root (where manage.py is)
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
django.setup()

from alerts.models import Alert

LOG_FILE = Path(__file__).resolve().parent / "sample_logs.txt"

def parse_log_line(line):
    try:
        data = json.loads(line)
        return data
    except json.JSONDecodeError:
        return None

def process_log_entry(entry):
    if not entry:
        return

    # Example detection rules
    event_type = entry.get('event_type')
    severity = 'Low'

    if event_type == 'LOGIN_FAILED':
        severity = 'Medium'
    elif event_type == 'PORT_SCAN':
        severity = 'High'
    elif event_type == 'MALWARE_DETECTED':
        severity = 'Critical'

    Alert.objects.create(
        timestamp=datetime.now(),
        source_ip=entry.get('source_ip'),
        event_type=event_type,
        severity=severity,
        description=entry.get('description', '')
    )

def main():
    if not LOG_FILE.exists():
        print(f"Log file not found: {LOG_FILE}")
        return

    with open(LOG_FILE, 'r') as f:
        for line in f:
            entry = parse_log_line(line)
            process_log_entry(entry)

    print("✅ Logs processed and alerts saved to the database.")

if __name__ == "__main__":
    main()