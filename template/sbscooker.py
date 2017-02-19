
import subprocess
import os.path

from . import get_tool_exec


def sbscooker({% for arg in sbscooker_args %}
		{{ arg["py_name"] }}=None{% if not loop.last %},{% endif %}{% endfor %}):

	sbscooker_exec = get_tool_exec("sbscooker")

	args = [sbscooker_exec]
	{% for arg in sbscooker_args %}
	if {{arg["py_name"]}}:
		args.extend(["--{{ arg["name"] }}", str({{arg["py_name"]}})])
	{% endfor %}
	subprocess.run(args)

	return

