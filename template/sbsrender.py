
import subprocess
import os.path

from . import get_tool_exec


encoding = "utf-8"


def info(input):
	sbsrender_exec = get_tool_exec("sbsrender")

	info = subprocess.run([sbsrender_exec, "info", "--input", input], stdout=subprocess.PIPE).stdout.decode(encoding)

	return info


def render({% for arg in sbsrender_args %}
		{{ arg["py_name"] }}=None{% if not loop.last %},{% endif %}{% endfor %}):

	sbsrender_exec = get_tool_exec("sbsrender")

	args = [sbsrender_exec, "render"]
	{% for arg in sbsrender_args %}
	if {{arg["py_name"]}}:
		args.extend(["--{{ arg["name"] }}", str({{arg["py_name"]}})])
	{% endfor %}
	subprocess.run(args)

	return

