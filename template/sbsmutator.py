
import subprocess
import os.path

from . import get_tool_exec


encoding = "utf-8"


def info(inputs):
	sbsmutator_exec = get_tool_exec("sbsmutator")

	args = [sbsmutator_exec, "info", "--inputs"]

	if inputs is list:
		args.extend(inputs)
	else:
		args.append(inputs)

	info = subprocess.run(args, stdout=subprocess.PIPE).stdout.decode(encoding)

	return info


def edit({% for arg in edit_args %}
		{{ arg["py_name"] }}=None{% if not loop.last %},{% endif %}{% endfor %}):

	sbsmutator_exec = get_tool_exec("sbsmutator")

	args = [sbsmutator_exec]
	{% for arg in edit_args %}
	if {{arg["py_name"]}}:
		args.extend(["--{{ arg["name"] }}", str({{arg["py_name"]}})])
	{% endfor %}
	subprocess.run(args)

	return


def update({% for arg in update_args %}
		{{ arg["py_name"] }}=None{% if not loop.last %},{% endif %}{% endfor %}):

	sbsmutator_exec = get_tool_exec("sbsmutator")

	args = [sbsmutator_exec]
	{% for arg in update_args %}
	if {{arg["py_name"]}}:
		args.extend(["--{{ arg["name"] }}", str({{arg["py_name"]}})])
	{% endfor %}
	subprocess.run(args)

	return