from typing import Dict, Any, List
from crdt_doc import CRDTTextDoc
from sandbox import CodeExecutionSandbox
from canvas_sync import ArchitectureCanvasSync

class SyncLabHub:
    """
    Central Coordination Hub managing CRDT Documents,
    Infinite Canvas State, and Ephemeral Sandbox Execution.
    """
    def __init__(self, session_id: str = "session_hackathon"):
        self.session_id = session_id
        self.doc = CRDTTextDoc(doc_id=session_id)
        self.canvas = ArchitectureCanvasSync(room_id=session_id)
        self.sandbox = CodeExecutionSandbox(timeout_sec=5)

    def execute_current_buffer(self) -> Dict[str, Any]:
        """Runs the consolidated code currently in the CRDT document."""
        source_code = self.doc.get_text()
        return self.sandbox.execute_python(source_code)
