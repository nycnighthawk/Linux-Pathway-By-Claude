# SPDX-License-Identifier: MIT
# Reference solution.
split_streams() {
    ./noisy > out.txt 2> err.txt
}
merge_streams() {
    ./noisy > both.txt 2>&1
}
append_log() {
    echo "run finished" >> log.txt
}
tee_copy() {
    ./noisy 2>/dev/null | tee copy.txt | wc -l
}
pipeline_status() {
    set -o pipefail
    false | true
    echo "$?"
}
make_conf() {
    cat > app.conf <<'CONF'
mode=fast
retries=3
name=lab
CONF
}
