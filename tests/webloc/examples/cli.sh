#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set -- "/tmp/name.webloc" "https://github.com"

( set -x; python -m webloc "$@" ) || exit
url="$( set -x; python -m webloc "$1" )"
echo $url
[[ $url == "$2" ]]
