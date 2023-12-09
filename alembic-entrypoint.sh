#!/bin/bash
set -euo pipefail

echo -e '\033[32m ==== run "alembic upgrade head" ==== \033[0m'
cd src && alembic upgrade head || { echo -e '\033[31m alembic upgrade failed \033[0m' ; exit 1; }
