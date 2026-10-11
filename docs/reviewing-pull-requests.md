# Reviewing a pull request

Review the code and its surrounding paths. The description and check badges are evidence to verify, rather than substitutes for review.

1. Confirm the PR is still open and record its current head. Read the whole diff, project instructions and relevant architecture. Search for overlapping open and draft PRs.
2. Trace real callers. Show that the changed behavior can be reached through the actual route, process or user flow. A module tested in isolation may still be unused.
3. Check the boundaries. Verify denied roles, wrong tenants, malformed input, expired sessions, duplicates, races and failure paths where relevant. Preserve fail-closed authentication, consent, data isolation and release controls.
4. Check the tests. For a bug, require proof that the regression fails without the fix. Run the affected checks on the proposed state and record skips or unavailable environments precisely. Follow project rules for repeated suites, native builds and integration checks.
5. Check compatibility and order. Resolve conflicts and prerequisites before merging. Test the combined result of interacting PRs, including database, agent/client and protocol compatibility.
6. Check delivery. State affected users/services, migrations, production lineage, deployment/release requirements, rollback and the separate live acceptance test. For product builds and production-ready claims, require timed onboarding through the product's UI by a non-technical operator.
7. Record the conclusion. Identify actionable findings with file/line and their consequence. Say which evidence resolved them and what remains unverified. Automated reviews are useful evidence; do not present them as an independent human approval.
8. Merge one PR at a time, with green applicable checks on the exact reviewed head. Confirm the resulting default branch matches the tested source. Preserve useful branches and evidence when other work depends on them.

Scale review to the change. A documentation correction needs a readable, accurate diff; an authorization or release change needs proof of both the permitted path and the refusal boundary. Do not add ceremonial checklists that obscure the actual risk.
