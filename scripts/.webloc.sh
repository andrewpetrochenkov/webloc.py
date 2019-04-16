#!/usr/bin/env bash
{ set +x; } 2>/dev/null

usage() {
    echo "usage: $(basename $0) path [url]" 1>&2
    [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; exit
}

[[ $1 == "-h" ]] || [[ $1 == "--help" ]] && usage "$@"

[[ $# == 0 ]] || [[ $# -gt 2 ]] && usage

[[ $OSTYPE != *darwin* ]] && echo "macOS only" && exit

[[ $# == 1 ]] && { /usr/libexec/PlistBuddy -c "Print URL" "$1"; exit; }

[[ -z $2 ]] && echo "EMPTY url" 1>&2 && exit 1
rm -f "$1"
[[ $1 == */* ]] && ! [ -e "${1%/*}" ] && { mkdir -p "${1%/*}" || exit; }
[[ $1 != *.webloc ]] && set -- "$1".webloc "$2"
/usr/libexec/PlistBuddy -c "Add URL string '$2'" "$1" &> /dev/null

