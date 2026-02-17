#!/bin/bash
set -euo pipefail

# Find the default IPv4 gateway from inside the container
GW="$(ip -4 route show default 2>/dev/null | awk '/default/ {print $3; exit}')"

if [ -z "${GW:-}" ]; then
  echo "Could not determine default gateway (ip route show default returned nothing)." >&2
  exit 0
fi

# Prepare the hosts line
LINE="$GW host.docker.internal"

# /etc/hosts is managed by Docker. You can update it at runtime as root.
# Replace an existing line or append if missing (idempotent).
if grep -qE '^[0-9.]+\s+host\.docker\.internal$' /etc/hosts; then
  # Replace existing mapping
  sed -i "s|^[0-9.]\+\s\+host\.docker\.internal$|$LINE|" /etc/hosts
else
  echo "$LINE" >> /etc/hosts
fi

echo "Mapped host.docker.internal -> $GW"
