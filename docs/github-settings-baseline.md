# GitHub settings baseline

This is the adoption policy, not a claim that every repository already has every setting. Verify live settings and the project's actual default and production branches before making changes. Keep the inventory and exceptions in private operational records.

## Branches and review

- Preserve default and production branches against force pushes and deletion.
- Require pull requests and resolved review conversations for maintained source branches. Include administrators. Avoid a permanent broad bypass; document any narrowly authorized emergency action and its follow-up review.
- Use real reviewers with write access. Where only one person is available, use a documented review with zero separate approval requirements rather than an impossible or fictional independent approval. Require an independent human reviewer when one becomes available.
- Configure stable, applicable required checks per project. A global check name would block repositories that do not emit it. Required checks must run on every relevant PR, including when changed-file filters would otherwise skip them.
- Preserve stricter repository rules, CODEOWNERS and acceptance requirements. Validate owner accounts and teams rather than inheriting unknown upstream owners.

## Automation

- Default `GITHUB_TOKEN` to read access and disable automated PR creation/approval unless a specific workflow needs it and has been reviewed. Grant necessary write scopes explicitly to the relevant job; do not rely on broad repository defaults.
- Audit default-branch workflow source and reusable workflows before changing permissions. Check release upload, package publish, PR creation and source writes separately. After changing settings, verify normal safe checks; do not trigger deployments merely to test a policy.
- Pin third-party actions to full commit SHAs and maintain those pins with Dependabot or a reviewed update process. Introduce an action allowlist or organization-wide pin requirement only after adapting and testing affected workflows.
- Restrict self-hosted runner groups to intended repositories and workflows. Separate untrusted PR execution from signing and production access. Confirm labels, jobs and isolation before changing routing.
- Keep publishing, signing, production environments and deployment approvals narrower than ordinary PR CI. Use the project's version/commit lineage, concurrency and artifact-verification guards.

## Accounts and data

Require organization 2FA after checking current member, outside-collaborator and billing-account access. Confirm recovery ownership; a settings checkbox does not establish recovery readiness. Verify access after the change. Stronger 2FA-method enforcement needs its own compatibility check.

Review app installations and collaborator access periodically. Grant repository access explicitly. Store machine secrets in the approved secret service with a separate identity per application/environment; use the human vault for the human copy. Never copy secrets into repository files, PRs or logs. Removing a committed secret from current source does not revoke it or erase history.

## Staged adoption

Start with shared guidance and a small pilot. Verify template inheritance and local overrides through GitHub's actual PR/issue UI. Snapshot settings before edits, make reversible changes, read them back and keep rollback instructions. Expand enforcement after the workflow and deployment paths are understood. Track exceptions as issues with an owner and acceptance condition; do not quietly label an incomplete baseline as complete.

References: [default files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file), [organization rulesets](https://docs.github.com/en/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization), [workflow permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [organization 2FA](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization).
