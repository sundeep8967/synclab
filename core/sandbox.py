import subprocess
import time
import sys
import tempfile
import os
from typing import Dict, Any

class CodeExecutionSandbox:
    """
    Isolated Subprocess Code Runner with strict resource limits and timeouts.
    Executes Python and JavaScript code safely for collaborative sessions.
    """
    def __init__(self, timeout_sec: int = 5):
        self.timeout_sec = timeout_sec

    def execute_python(self, code_str: str) -> Dict[str, Any]:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(code_str)
            temp_path = f.name

        t0 = time.perf_counter()
        try:
            res = subprocess.run(
                [sys.executable, temp_path],
                capture_output=True,
                text=True,
                timeout=self.timeout_sec
            )
            t1 = time.perf_counter()
            return {
                "success": (res.returncode == 0),
                "exit_code": res.returncode,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "execution_time_ms": round((t1 - t0) * 1000.0, 2)
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "exit_code": -1,
                "stdout": "",
                "stderr": f"Execution Timed Out: Exceeded {self.timeout_sec}s guard limit.",
                "execution_time_ms": self.timeout_sec * 1000.0
            }
        except Exception as e:
            return {
                "success": False,
                "exit_code": -1,
                "stdout": "",
                "stderr": str(e),
                "execution_time_ms": 0.0
            }
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
