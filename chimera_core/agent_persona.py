from __future__ import annotations
from typing import List
from pydantic import BaseModel
import yaml
from pathlib import Path


class AgentPersona(BaseModel):
    name: str
    id: str
    voice_traits: List[str]
    directives: List[str]
    backstory: str = ""

    @classmethod
    def from_soul_file(cls, path: str) -> "AgentPersona":
        p = Path(path)
        text = p.read_text(encoding="utf-8")
        # Simple frontmatter parse: look for YAML between --- markers
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                _, yaml_part, rest = parts
                meta = yaml.safe_load(yaml_part)
                backstory = rest.strip()
                return cls(
                    name=meta.get("name", ""),
                    id=meta.get("id", ""),
                    voice_traits=meta.get("voice_traits", []),
                    directives=meta.get("directives", []),
                    backstory=backstory,
                )
        raise ValueError("Invalid SOUL.md format")


async def assemble_context(agent_id: str, input_query: str, mcp_client) -> str:
    """Assemble runtime context string for an agent.

    This function attempts to load the agent's SOUL.md, query the mcp_client
    for relevant memories (if available), and return a formatted system prompt.
    """
    # Load persona file by convention
    soul_path = f"SOUL.md"
    persona = AgentPersona.from_soul_file(soul_path)

    memories = []
    if mcp_client is not None and hasattr(mcp_client, "search_memory"):
        try:
            mems = await mcp_client.search_memory(agent_id, input_query, limit=5)
            memories = mems
        except Exception:
            memories = []

    lines = [
        "Context:\n",
        "Who You Are:\n",
        f"Name: {persona.name}\n",
        f"Voice Traits: {', '.join(persona.voice_traits)}\n",
        f"Directives: {', '.join(persona.directives)}\n",
        "What You Remember:\n",
    ]
    for m in memories:
        lines.append(f"- {m}\n")

    lines.append("\nUser Query:\n")
    lines.append(input_query)
    return "".join(lines)
