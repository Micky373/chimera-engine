# Project Chimera — Scaffold

Project Chimera is a spec-first scaffold for an Autonomous Influencer Network. This repository provides a starter architecture and developer workflow so you can focus on implementing agent skills, MCP adapters, and governance.

Repository layout

- [specs/](specs/): project specifications and Mermaid diagrams (`_meta.md`, `functional.md`, `technical.md`)
- [skills/](skills/): runtime skill stubs and I/O contracts (e.g., `skill_download_video`, `skill_publish_post`)
- [tests/](tests/): failing test placeholders (TDD-first — tests define the agent's goals)
- [chimera_core/](chimera_core/): core helpers (includes `agent_persona.py`)
- `SOUL.md`: agent persona template (frontmatter + backstory)
- `Dockerfile`, `Makefile`, `.github/workflows/main.yml`: CI and container helpers
- `.cursor/rules`: IDE agent rules and prime directive

Quick start

1. Create a virtual environment and activate it.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the test suite (expected to contain intentional failing/stubbed tests):

```bash
make test
```

3. Install git hooks (optional — runs tests on push):

```bash
make install-hooks
```

CI

- GitHub Actions will run on pushes and PRs to `main/master` and upload a JUnit XML report artifact.
- The `Makefile` exposes `make ci` and `make build-image` to mirror CI steps locally.

Development notes

- Follow spec-first development: update files in `specs/` before implementing code.
- Skills must expose clear JSON I/O contracts; use `skills/README.md` as the source of truth for each skill.
- Use `SOUL.md` (versioned) as the canonical persona source and hydrate it via `chimera_core.agent_persona.AgentPersona`.

Next recommended milestones

- Implement a mock `mcp-server` adapter for `weaviate` and `twitter` to enable offline integration tests.
- Implement 1–2 core skills and convert tests from errors→failing→passing (TDD flow).
- Add telemetry integration with Tenx MCP Sense when available.

---
Updated scaffold and developer workflow files: `Makefile`, `.github/workflows/main.yml`, `.pre-commit-config.yaml`, `pytest.ini`.

## Author

- GitHub: [@Micky](https://github.com/Micky373)
- Twitter: [@twitterhandle](https://twitter.com/twitterhandle)
- LinkedIn: [LinkedIn](https://linkedin.com/in/michaeltamirie)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/Micky373/chimera-engine/issues).

## 📝 License

This project is [MIT](./MIT.md) licensed.
