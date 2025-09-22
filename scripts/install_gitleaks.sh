#!/bin/bash
# Helper script to download and install gitleaks for CI/CD

set -e

VERSION="v8.18.4"
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)
if [ "$ARCH" == "x86_64" ]; then
    ARCH="x64"
elif [ "$ARCH" == "aarch64" ]; then
    ARCH="arm64"
fi

DOWNLOAD_URL="https://github.com/gitleaks/gitleaks/releases/download/${VERSION}/gitleaks_${VERSION:1}_${OS}_${ARCH}.tar.gz"
INSTALL_DIR="/usr/local/bin"

echo "Downloading gitleaks from ${DOWNLOAD_URL}..."
curl -sSL ${DOWNLOAD_URL} -o gitleaks.tar.gz

echo "Extracting gitleaks..."
tar -xzf gitleaks.tar.gz gitleaks

echo "Installing gitleaks to ${INSTALL_DIR}..."
sudo mv gitleaks ${INSTALL_DIR}/gitleaks

rm gitleaks.tar.gz

echo "gitleaks installed successfully:"
gitleaks version
