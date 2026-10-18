from typing import Dict, Any, List

class ArchitectureCanvasSync:
    """
    Real-Time Vector Whiteboard State Manager.
    Synchronizes diagram nodes, arrows, and cursor presence across collaborators.
    """
    def __init__(self, room_id: str = "room_01"):
        self.room_id = room_id
        self.elements: Dict[str, Dict[str, Any]] = {}
        self.peer_cursors: Dict[str, Dict[str, int]] = {}

    def update_element(self, element_id: str, element_data: Dict[str, Any]) -> None:
        self.elements[element_id] = element_data

    def update_cursor(self, peer_id: str, x: int, y: int) -> None:
        self.peer_cursors[peer_id] = {"x": x, "y": y}

    def get_canvas_snapshot(self) -> Dict[str, Any]:
        return {
            "room_id": self.room_id,
            "total_elements": len(self.elements),
            "elements": self.elements,
            "active_peer_cursors": self.peer_cursors
        }
