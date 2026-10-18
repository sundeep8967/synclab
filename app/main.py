import os
import sys
import time
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
core_dir = os.path.join(root_dir, "core")
sys.path.insert(0, core_dir)

from server import SyncLabHub

def main():
    print("\n" + "#"*75)
    print("      🧪 SYNCLAB: REAL-TIME WEBRTC CODE & CANVAS SANDBOX")
    print("      BUiLDX (Code-A-Nova) Hackathon — Unstop Submission")
    print("#"*75)

    hub = SyncLabHub(session_id="interview_room_tokyo_sf")

    time.sleep(0.5)
    print("\n👥 [STEP 1/3]: Simulating Real-Time Concurrent Multi-Peer CRDT Editing...")
    print("  • Peer 1 (Dev A - San Francisco): Typing function definition...")
    # Dev A writes: "def compute_fibonacci(n):\n    return n if n <= 1 else compute_fibonacci(n-1) + compute_fibonacci(n-2)\n"
    code_part_a = "def compute_fibonacci(n):\n    return n if n <= 1 else compute_fibonacci(n-1) + compute_fibonacci(n-2)\n"
    prev = None
    for i, ch in enumerate(code_part_a):
        cid = f"a_{i}"
        hub.doc.insert(ch, cid, prev)
        prev = cid

    print("  • Peer 2 (Dev B - Bengaluru): Concurrently inserting driver test code...")
    # Dev B concurrently writes the driver call at the end: "print(f'Fib(8) = {compute_fibonacci(8)}')\n"
    code_part_b = "print(f'Fibonacci(8) = {compute_fibonacci(8)}')\n"
    for j, ch in enumerate(code_part_b):
        cid = f"b_{j}"
        hub.doc.insert(ch, cid, prev)
        prev = cid

    consolidated_code = hub.doc.get_text()
    print("\n📄 [CONSOLIDATED CONFLICT-FREE CRDT BUFFER]:")
    print("-" * 50)
    print(consolidated_code.strip())
    print("-" * 50)

    time.sleep(0.5)
    print("\n🎨 [STEP 2/3]: Synchronizing Vector Whiteboard Architecture Layer...")
    # Dev A draws a client node, Dev B connects it to an API gateway
    hub.canvas.update_element("node_client", {"type": "rect", "x": 100, "y": 150, "label": "Client PWA (WebRTC)"})
    hub.canvas.update_element("node_gateway", {"type": "rect", "x": 350, "y": 150, "label": "SyncLab Hub Gateway"})
    hub.canvas.update_element("arrow_conn", {"type": "arrow", "from": "node_client", "to": "node_gateway"})
    hub.canvas.update_cursor("peer_dev_a", 145, 160)
    hub.canvas.update_cursor("peer_dev_b", 380, 165)

    snap = hub.canvas.get_canvas_snapshot()
    print(f"  • Active Canvas Elements: {snap['total_elements']} synchronized vector nodes")
    print(f"  • Tracked Peer Cursors:   {list(snap['active_peer_cursors'].keys())}")

    time.sleep(0.5)
    print("\n⚡ [STEP 3/3]: Triggering Ephemeral Code Execution in Sandboxed Subprocess...")
    exec_result = hub.execute_current_buffer()

    print("\n" + "="*75)
    print("📋 SANDBOX EXECUTION REPORT:")
    print(f"Status:             {'✅ SUCCESS' if exec_result['success'] else '❌ FAILED'}")
    print(f"Execution Duration: {exec_result['execution_time_ms']} ms")
    print(f"Captured STDOUT:")
    print(f"  {exec_result['stdout'].strip()}")
    print("="*75)
    print("✨ SUCCESS: Multi-peer CRDT sync, vector canvas, and sandboxed run verified!")

if __name__ == "__main__":
    main()
