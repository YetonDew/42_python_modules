import sys


print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
sys.stdout.write("Input Stream active. Enter archivist ID: ")
sys.stdout.flush()
archivist_id = sys.stdin.readline().rstrip("\n")
# stdin for receiving messages
sys.stdout.write("Input Stream active. Enter status report: ")
sys.stdout.flush()
status_report = sys.stdin.readline().rstrip("\n")

standard_prefix = f"[STANDARD] Archive status from {archivist_id}: "
standard_msg = f"{standard_prefix}{status_report}\n"
alert_msg = "[ALERT] System diagnostic: Communication channels verified\n"

# stdout for normal broadcasts
sys.stdout.write(standard_msg)
# stderr for emergency alerts
sys.stderr.write(alert_msg)
sys.stdout.write("[STANDARD] Data transmission complete\n")
print("Three-channel communication test successful.")
