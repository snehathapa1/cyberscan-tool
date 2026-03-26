import subprocess

url = input("Enter website URL: ")

print("Starting vulnerability scan...\n")

result = subprocess.getoutput(f"nikto -h {url}")

print(result)

with open("scan_report.txt", "w") as file:
    file.write(result)

print("\nScan finished. Report saved as scan_report.txt")