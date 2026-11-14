# SPDX-License-Identifier: MIT
# Reference solution.
visible_txt() {
    printf '%s\n' *.txt
}
count_short_reports() {
    local n=0 f
    for f in report\ ?.log; do [ -e "$f" ] && n=$((n + 1)); done
    echo "$n"
}
literal_text() {
    echo '$HOME is "home"'
}
show_notes() {
    cat -- 'my notes.txt'
}
remove_dash_file() {
    rm -- -rf.txt
}
