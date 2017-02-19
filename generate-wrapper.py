import os
import subprocess
import jinja2
import sys

encoding = "utf-8"


def get_args(lines):
	arg_lines = [l.strip().split() for l in lines if l.startswith("  --")]

	args = []
	for arg_line in arg_lines:
		cmd_arg_name = arg_line[0][2:]
		py_arg_name = cmd_arg_name.replace("-", "_")

		args.append({"py_name": py_arg_name, "name": cmd_arg_name})

	return args


def get_command_args(exec, cmd):
	help = subprocess.run([exec, cmd, "--help"], stdout=subprocess.PIPE).stdout.decode(encoding)
	lines = help.splitlines()
	return get_args(lines)


def sbsbaker_get_commands():
	help = subprocess.run([sbsbaker_exec, "--help"], stdout=subprocess.PIPE).stdout.decode(encoding)
	lines = help.splitlines()

	cmds_line = lines.index("Available commands are: ") + 1
	cmds = []
	for line in lines[cmds_line:]:
		cmd_name = line.strip()
		if cmd_name == "":
			break
		print("  " + cmd_name)
		args = get_command_args(sbsbaker_exec, cmd_name)
		py_cmd_name = cmd_name.replace("-", "_")
		cmds.append({"py_name": py_cmd_name, "name": cmd_name, "args": args})

	return cmds


def sbscooker_get_args():
	help = subprocess.run([sbscooker_exec, "--help"], stdout=subprocess.PIPE).stdout.decode(encoding)
	lines = help.splitlines()
	args = get_args(lines)
	args = [arg for arg in args if arg["name"] not in ["help", "help-advanced", "version", "version-cooker", "version-linker", "verbose"]]
	return args


def sbsrender_get_args():
	help = subprocess.run([sbsrender_exec, "render", "--help"], stdout=subprocess.PIPE).stdout.decode(encoding)
	lines = help.splitlines()
	args = get_args(lines)
	return args


def generate_python_source(jinja_env, code_file, out_dir, *args, **kwargs):
	template = jinja_env.get_template(code_file)
	code = template.render(*args, **kwargs)

	file = open(os.path.join(out_dir, code_file), "w")
	file.write(code)
	file.close()


def main():
	if len(sys.argv) != 2:
		print("Usage: " + sys.argv[0] + " [path to batch tools]")
		return 1

	global sbsbaker_exec
	global sbscooker_exec
	global sbsmutator_exec
	global sbsrender_exec

	# find tools
	tools_path = sys.argv[1]
	sbsbaker_exec = os.path.join(tools_path, "sbsbaker")
	sbscooker_exec = os.path.join(tools_path, "sbscooker")
	sbsmutator_exec = os.path.join(tools_path, "sbsmutator")
	sbsrender_exec = os.path.join(tools_path, "sbsrender")

	# get commands and arguments
	print("sbsbaker:")
	sbsbaker_commands = sbsbaker_get_commands()

	print("sbscooker")
	sbscooker_args = sbscooker_get_args()

	print("sbsmutator")
	sbsmutator_edit_args = get_command_args(sbsmutator_exec, "edit")
	sbsmutator_update_args = get_command_args(sbsmutator_exec, "update")

	print("sbsrender")
	sbsrender_args = sbsrender_get_args()

	# generate code
	jinja_env = jinja2.Environment(
		loader=jinja2.PackageLoader(__name__, "template"),
		autoescape=(["py"]))

	out_mod_dir = "substance_wrapper"
	os.makedirs(out_mod_dir, exist_ok=True)

	generate_python_source(jinja_env, "__init__.py", out_mod_dir)
	generate_python_source(jinja_env, "sbsbaker.py", out_mod_dir, sbsbaker_commands=sbsbaker_commands)
	generate_python_source(jinja_env, "sbscooker.py", out_mod_dir, sbscooker_args=sbscooker_args)
	generate_python_source(jinja_env, "sbsmutator.py", out_mod_dir, edit_args=sbsmutator_edit_args, update_args=sbsmutator_update_args)
	generate_python_source(jinja_env, "sbsrender.py", out_mod_dir, sbsrender_args=sbsrender_args)

	return 0


if __name__ == "__main__":
	r = main()
	sys.exit(r)
