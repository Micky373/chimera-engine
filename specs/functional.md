# Project Chimera - Functional Specs

## User Stories

- As a Network Operator, I need to define a campaign goal so that agents can act to achieve measurable outcomes.
- As a Human Reviewer, I need an interface to review flagged content so that sensitive items are approved before publication.
- As a Developer, I need clear skill I/O contracts so that agents and automation can integrate reliably.

## Acceptance Criteria (examples)

- Campaign object contains: `id`, `owner_id`, `channels`, `budget`, `goals`.
- Skills accept JSON inputs and return JSON output with `status` and `artifact` metadata.
