# 🧪 SyncLab: Real-Time Collaborative WebRTC Code & Architecture Canvas Sandbox

> **Submission for "BUiLDX (Code-A-Nova)" on Unstop**  
> **Category:** General Software Development, Real-Time Systems, Cloud Collaboration  
> **Participant:** sundeep8967

---

## 🌟 The Problem

Remote technical hiring, pair-programming, and live lab education suffer from friction:
* Traditional screen-sharing over Zoom or Google Meet is passive, laggy, and restricts editing to a single user.
* Generic web pads have no native code execution environments, and force engineers to juggle a separate whiteboard tool (Excalidraw, Miro) to explain systems architecture.

---

## 🚀 The Solution: SyncLab

**SyncLab** is an integrated collaborative engineering workspace:
1. **Conflict-Free Code Editor:** Powered by a sequence **Conflict-Free Replicated Data Type (CRDT)** allowing multiple distributed peers to type simultaneously with zero merge conflicts or locked lines.
2. **Infinite Vector Whiteboard Layer:** Synchronizes architectural diagram nodes, directional arrows, and peer $(x, y)$ cursor presence in real time.
3. **Isolated Ephemeral Sandbox:** Runs code in secure subprocesses with strict timeout boundaries (5s) and streams `stdout`, `stderr`, and execution durations back to all participants simultaneously.

---

## ⚡ Quickstart Demo

### 1. Requirements
- Python 3.10+

### 2. Run the SyncLab Simulation Demo
```bash
cd synclab
python3 app/main.py
```

### 3. Output
The tool demonstrates:
* Two distributed peers concurrently typing a recursive Fibonacci algorithm without conflicts.
* Synchronizing vector architecture nodes and peer cursor coordinates on the whiteboard.
* Executing the consolidated buffer inside an isolated sandbox, returning `Fibonacci(8) = 21` in ~14ms.

---

## 📚 Machine-Readable Documentation
- [`LLMS.txt`](./LLMS.txt): Concise system specification for LLMs and autonomous agents.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md): Formal topology, sequence flows, and data schemas.
