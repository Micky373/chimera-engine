# Project Chimera - Specs Meta

## Vision
Project Chimera: an Autonomous Influencer Network driven by spec-first development, traceability (MCP), and hierarchical swarm agents.

## High-level diagram (Mermaid)

```mermaid
flowchart LR
  subgraph Hub
    Orchestrator[Central Orchestrator]
  end
  subgraph Spokes
    AgentSwarm[Agent Swarm\n(Planner -> Worker -> Judge)]
  end
  Orchestrator -->|manages| AgentSwarm
  AgentSwarm -->|uses| MCP[MCP Servers & Tools]
  MCP -->|connects to| External[Social APIs, Weaviate, Wallets]
```

## Notes
- Use `specs/functional.md` for user stories.
- Use `specs/technical.md` for API contracts and ERD.
