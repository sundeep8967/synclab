from typing import List, Dict, Any, Optional

class CharNode:
    def __init__(self, char: str, char_id: str, prev_id: Optional[str] = None):
        self.char = char
        self.char_id = char_id      # e.g., "1@clientA"
        self.prev_id = prev_id      # Points to preceding character ID
        self.is_deleted = False

class CRDTTextDoc:
    """
    Sequence Conflict-Free Replicated Data Type (CRDT).
    Ensures mathematical convergence of concurrent peer edits without locks or merge conflicts.
    """
    def __init__(self, doc_id: str = "doc_collab_default"):
        self.doc_id = doc_id
        self.nodes: List[CharNode] = []
        self.node_map: Dict[str, CharNode] = {}

    def insert(self, char: str, char_id: str, after_id: Optional[str] = None) -> None:
        """Inserts character using deterministic tie-breaking on char_id."""
        node = CharNode(char, char_id, after_id)
        if char_id in self.node_map:
            return  # Idempotent re-application

        if after_id is None:
            # Insert at beginning
            insert_pos = 0
            while insert_pos < len(self.nodes) and self.nodes[insert_pos].prev_id is None:
                if self.nodes[insert_pos].char_id > char_id:
                    break
                insert_pos += 1
            self.nodes.insert(insert_pos, node)
        else:
            # Find after_id position
            idx = next((i for i, n in enumerate(self.nodes) if n.char_id == after_id), -1)
            if idx != -1:
                insert_pos = idx + 1
                while insert_pos < len(self.nodes) and self.nodes[insert_pos].prev_id == after_id:
                    if self.nodes[insert_pos].char_id > char_id:
                        break
                    insert_pos += 1
                self.nodes.insert(insert_pos, node)
            else:
                self.nodes.append(node)

        self.node_map[char_id] = node

    def delete(self, char_id: str) -> None:
        """Tombstone deletion."""
        if char_id in self.node_map:
            self.node_map[char_id].is_deleted = True

    def get_text(self) -> str:
        """Renders consolidated text state."""
        return "".join(n.char for n in self.nodes if not n.is_deleted)
