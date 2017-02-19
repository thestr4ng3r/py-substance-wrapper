
import subprocess
import os.path

from . import get_tool_exec

{% for cmd in sbsbaker_commands %}
def {{ cmd["py_name"] }}( {% for arg in cmd["args"] %}
		{{ arg["py_name"] }}=None{% if not loop.last %},{% endif %}{% endfor %}):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "{{ cmd["name"] }}"]
	{% for arg in cmd["args"] %}
	if {{ arg["py_name"] }}:
		args.extend(["--{{ arg["name"] }}", str({{ arg["py_name"] }})])
	{% endfor %}
	subprocess.run(args)

	return

{% endfor %}