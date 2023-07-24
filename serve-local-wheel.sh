#!/bin/sh
set -ex

TMP_REPO=`mktemp -d`

mkdir -p $TMP_REPO/setuptools-ocrd
pip wheel --wheel-dir $TMP_REPO/setuptools-ocrd .

cd $TMP_REPO
python3 -m http.server 28486
