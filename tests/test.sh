#!/bin/bash

set -ex

CURDIR=$(dirname "$0")
CHECKER=check-pipfile-lock

check_cwd() {
	(cd "$CURDIR/good" && $CHECKER)
}

check_good() {
	$CHECKER "$CURDIR/good/Pipfile.lock"
}

check_bad() {
	if $CHECKER "$CURDIR/bad/Pipfile.lock"; then
		echo "Got false negative on a bad file"
		exit 1
	fi
}

check_both() {
	if $CHECKER "$CURDIR/bad/Pipfile.lock" "$CURDIR/good/Pipfile.lock"; then
		echo "Got false negative on one of the bad files"
		exit 1
	fi
	if ! $CHECKER "$CURDIR/bad/Pipfile.lock" "$CURDIR/good/Pipfile.lock" 2>&1 | \
			grep -q "bad/Pipfile.lock is out of date. Consider running 'pipenv lock'"; then
		echo "Error signature missing/changed"
		exit 1
	fi
}

check_cwd
check_good
check_bad
check_both
