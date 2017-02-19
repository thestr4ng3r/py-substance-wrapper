
__all__ = ["sbsbaker", "sbscooker", "sbsmutator", "sbsrender"]

tools_path = None

class SubstanceBatchToolsNotFoundError(Exception):
	pass

import os.path

def get_tool_exec(tool):
	if not tools_path:
		raise SubstanceBatchToolsNotFoundError()
	return os.path.join(tools_path, tool)

from . import sbsbaker
from .sbscooker import sbscooker
from . import sbsmutator
from . import sbsrender