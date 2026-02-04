# Skills

This folder contains skill stubs and I/O contracts for runtime capabilities used by Chimera agents.

Three starter skills:

- `skill_download_video` — Input: `{ "url": string }` → Output: `{ "status": "ok"|"error", "artifact": {"path": string} }`
- `skill_transcribe_audio` — Input: `{ "path": string }` → Output: `{ "text": string, "segments": [] }`
- `skill_publish_post` — Input: `{ "channel": string, "content": string, "metadata": {} }` → Output: `{ "id": string, "status": string }

Implementations should follow the I/O contract and raise `NotImplementedError` until implemented.
