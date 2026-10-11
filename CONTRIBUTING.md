# Proposing a change

Read the repository's README, contribution guide and agent instructions first. Follow its stricter requirements when they differ from this baseline.

## Start with the problem

Search issues and all open pull requests, including drafts. Reuse an existing issue when it describes the same problem. Record a new issue before changing behavior, authentication, data, infrastructure, CI or release machinery. Include the affected people or services and a clear acceptance condition.

Keep one logical change in a PR. Start from a freshly fetched default branch. Preserve other contributors' work. Once a PR has been published, merge new base changes into it rather than rebasing or force-pushing reviewed commits.

## Make the result reviewable

Explain the observed problem, the resulting behavior and why the approach works. Link the issue. Use conventional commit titles such as `fix(component): prevent the observed failure`; include an issue reference in the commit or PR.

Document behavior changes in the same PR. New routes, fields, protocols, settings or operational steps need their corresponding project documentation. Record a decision when undoing it would reopen a security, tenancy or reliability problem.

For a bug, reproduce the failure and show that the regression test fails without the fix. Check real callers and refusal paths, including missing permissions and wrong tenants. Run the repository's required checks on the exact state proposed for merge. Repeat order-sensitive or race-sensitive suites as its rules require. Never describe skipped or unavailable checks as passed.

Provide visual evidence for meaningful UI changes. When building a product, or describing it as production-ready, verify that a non-technical operator can onboard a test customer through the product UI alone, including discovery or grants, plain-language checks, a test step and visible pending status. Record the timing and any remaining manual work.

Keep incomplete work in draft. Say exactly what remains unverified and why. Do not include real customer data, credentials, session values or private operational details in public examples, screenshots, logs or issue forms. Use synthetic test fixtures.

## Merge and deliver deliberately

Check for overlapping open PRs, including drafts, and state prerequisites and merge order. Test the combined result when several changes interact. Review the current GitHub head before every push or merge; preserve concurrent changes and pin the merge to the reviewed commit.

Use the repository's required checks and review process. Record review findings and their resolution even where the small-team review model does not require a separate GitHub approval. Never weaken a safeguard to make a change mergeable.

Describe deployment, migrations, platform builds, rollback and acceptance separately. A merged PR is source accepted; a successful build is an artifact prepared; a healthy endpoint alone does not prove the new behavior. Verify the deployed version and the intended user workflow before calling delivery complete.

See the [reviewer guide](https://github.com/geeksblock/.github/blob/main/docs/reviewing-pull-requests.md) and [settings baseline](https://github.com/geeksblock/.github/blob/main/docs/github-settings-baseline.md).
