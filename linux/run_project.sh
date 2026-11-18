#!/usr/bin/env bash
echo "run_project.sh started"
source ../.venv/bin/activate || exit 1
type -a python #  or use command -v python
export APP_MODE=development
python env_variable.py
status=$?

if [ "$status" -eq 0 ]; then
	printf "Status: %s => Program ran successfully.\n" "$status"
else
	printf "Status: %s => Program did not execute.\n" "$status"
fi

exit "$status" 
