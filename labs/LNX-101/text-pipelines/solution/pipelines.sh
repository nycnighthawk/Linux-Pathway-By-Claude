# SPDX-License-Identifier: MIT
# Reference solution.
top_ips() {
    awk '{ print $1 }' access.log | sort | uniq -c | sort -rn | head -3
}
server_errors() {
    awk '$9 >= 500 { n++ } END { print n + 0 }' access.log
}
real_users() {
    awk -F: '$3 >= 1000 && $3 < 65534 { print $1 }' users.txt | sort
}
redact() {
    sed -E 's/[A-Za-z0-9._-]+@/***@/g' mail.txt
}
total_lines() {
    find files -type f -print0 | xargs -0 cat | wc -l
}
