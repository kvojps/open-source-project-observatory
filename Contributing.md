# Contributing to Open source project observatory

Welcome! Here is a community project that aims to work towards a broad
range of users with the aim of building a platform that centralizes open source projects. If you are trying to contribute to an open source project, your experience and what you can contribute are
important for the success of the project.

## Code of Conduct

Everyone who participates in our community, and in particular in our
issue tracker, pull requests, and chat are expected to resolve
other people with respect and, more generally, follow the guidelines
articulated in the [Open source project observatory Code of Conduct](https://github.com/kvojps/open-source-project-observatory#coc-ov-file).

## Getting started with development

### Setup

#### (1) Fork the mypy repository

Within Github, navigate to <https://github.com/kvojps/open-source-project-observatory> and fork the repository.

#### (2) Clone the repository and enter into it

```bash
git clone git@github.com:<your_username>/open-source-project-observatory.git
cd open-source-project-observatory
```

#### (3) Follow the manual for running the frontend and backend environments

- [Backend manual](https://github.com/kvojps/open-source-project-observatory/blob/main/backend/README.md)
- [Frontend manual](https://github.com/kvojps/open-source-project-observatory/blob/main/frontend/README.md)

## First time contributors

If you're looking for things to help with, browse our [issue tracker](https://github.com/kvojps/open-source-project-observatory/issues)!

In particular, look for:

- [good first issues](https://github.com/kvojps/open-source-project-observatory/labels/good-first-issue)
- [good second issues](https://github.com/kvojps/open-source-project-observatory/labels/good-second-issue)
- [documentation issues](https://github.com/kvojps/open-source-project-observatory/labels/documentation)

You do not need to ask for permission to work on any of these issues.
Just fix the issue yourself, [open a pull request](#submitting-changes).

To get help fixing a specific issue, it's often best to comment on the issue
itself. You're much more likely to get help if you provide details about what
you've tried and where you've looked (maintainers tend to help those who help
themselves).

## Submitting changes

Even more excellent than a good bug report is a fix for a bug, or the
implementation of a much-needed new feature. We'd love to have
your contributions.

We use the usual GitHub pull-request flow, which may be familiar to
you if you've contributed to other projects on GitHub.  For the mechanics,
see [GitHub's own documentation](https://help.github.com/articles/using-pull-requests/).

Anyone interested in this project may review your code.  One of the core
developers will merge your pull request when they think it's ready.

If your change will be a significant amount of work
to write, we highly recommend starting by opening an issue laying out
what you want to do.  That lets a conversation happen early in case
other contributors disagree with what you'd like to do or have ideas
that will help you do it.

The best pull requests are focused, clearly describe what they're for
and why they're correct, and contain tests for whatever changes they
make to the code's behavior.  As a bonus these are easiest for someone
to review, which helps your pull request get merged quickly!  Standard
advice about good pull requests for open-source projects applies; we
have [our own writeup]() of this advice.

Also, do not squash your commits after you have submitted a pull request, as this
erases context during review. We will squash commits when the pull request is merged.

You may also find other pages in the [developer guide]() helpful in developing your change.

## Core developer guidelines

Core developers should follow these rules when processing pull requests:

- Always wait for tests to pass before merging PRs.
- Use "[Squash and merge](https://github.com/blog/2141-squash-your-commits)"
  to merge PRs.
- Delete branches for merged PRs (by core devs pushing to the main repo).
- Edit the final commit message before merging to conform to the following
  style (we wish to have a clean `git log` output):
  - When merging a multi-commit PR make sure that the commit message doesn't
    contain the local history from the committer and the review history from
    the PR. Edit the message to only describe the end state of the PR.
  - Make sure there is a *single* newline at the end of the commit message.
    This way there is a single empty line between commits in `git log`
    output.
  - Split lines as needed so that the maximum line length of the commit
    message is under 80 characters, including the subject line.
  - Capitalize the subject and each paragraph.
  - Make sure that the subject of the commit message has no trailing dot.
  - Use the imperative mood in the subject line (e.g. "Fix typo in README").
  - If the PR fixes an issue, make sure something like "Fixes #xxx." occurs
    in the body of the message (not in the subject).
  - Use Markdown for formatting.
