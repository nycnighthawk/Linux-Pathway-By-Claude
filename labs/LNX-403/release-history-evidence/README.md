# Guide lab: Releases and user issues over several weeks

Ship the service publicly (a public repository and a tagged release are enough), invite real users, and keep it for several weeks while you handle what comes in. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `weeks_observed` | weeks between the first release and this summary |
| `releases` | tagged releases in the period |
| `signed_releases` | of those, how many have a signature or attestation |
| `changelog_entries` | changelog entries written |
| `issues_opened` | issues or reports from other people |
| `issues_closed` | of those, how many are closed |
| `median_first_response_hours` | median hours to your first reply |
| `regressions` | issues that were regressions of your own releases |
| `security_reports` | private security reports received (0 is fine) |
| `security_policy_published` | yes if a SECURITY file or equivalent tells people how to report |
| `docs_changes_from_issues` | documentation changes caused by user questions |
| `upgrade_path_tested` | yes if you tested upgrading from the previous release |

## Success criteria

- Release notes tell users what changed and what to do when upgrading.
- At least one issue led to a fix, a release and a note.
- You wrote a reply to every report, including the ones you declined.
- You recorded one thing you would change in the process.

## Grade it

`bin/lpc course lab LNX-403 release-history-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment O: time or human review); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-403-T06).
