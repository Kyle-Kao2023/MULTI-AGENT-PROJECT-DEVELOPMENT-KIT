#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path
import json

# --- Configuration ---
# Allowlist of acceptable licenses (use SPDX identifiers)
ALLOWED_LICENSES = {
    "MIT", "Apache-2.0", "BSD-3-Clause", "ISC", "Python-2.0"
}

# Blocklist of sensitive words to scan for in the codebase
SENSITIVE_WORDS = {
    "TODO", "FIXME", "XXX", "HACK",
    "password", "secret", "apikey", "private_key"
}

# Directories to scan
SCAN_DIRECTORIES = ["src", "cli", "graph", "scripts", "templates"]

def check_licenses():
    """Checks installed packages against an allowed license list."""
    print("\n--- Running License Compliance Scan ---")
    try:
        # Run pip-licenses to get a report
        result = subprocess.run(
            [sys.executable, "-m", "piplicenses", "--format=json", "--with-urls"],
            capture_output=True, text=True, check=True
        )
        packages = json.loads(result.stdout)
        
        non_compliant_packages = []
        for pkg in packages:
            if pkg["License"] not in ALLOWED_LICENSES:
                non_compliant_packages.append(pkg)
                
        if non_compliant_packages:
            print("❌ Found non-compliant package licenses:")
            for pkg in non_compliant_packages:
                print(f"  - {pkg['Name']} ({pkg['Version']}): {pkg['License']}")
            return False
        else:
            print("✅ All package licenses are compliant.")
            return True
            
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error running pip-licenses: {e}")
        return False

def check_sensitive_words():
    """Scans the codebase for sensitive words."""
    print("\n--- Running Sensitive Word Scan ---")
    found_words = []
    
    for directory in SCAN_DIRECTORIES:
        for filepath in Path(directory).rglob("*.py"):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, 1):
                        for word in SENSITIVE_WORDS:
                            if word.lower() in line.lower():
                                found_words.append((word, filepath, i))
            except (IOError, UnicodeDecodeError):
                continue # Skip unreadable files

    if found_words:
        print("❌ Found potentially sensitive words in the codebase:")
        for word, filepath, line_num in found_words:
            print(f"  - Found '{word}' in {filepath} on line {line_num}")
        return False
    else:
        print("✅ No sensitive words found in the codebase.")
        return True

def main():
    print("--- VibeCoder Compliance Scan ---")
    license_ok = check_licenses()
    words_ok = check_sensitive_words()
    
    if license_ok and words_ok:
        print("\n[RESULT] ✅ Compliance Scan PASSED")
        sys.exit(0)
    else:
        print("\n[RESULT] ❌ Compliance Scan FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()
