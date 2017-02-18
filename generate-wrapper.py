import os
import subprocess
import jinja2
import sys

sbsbaker_exec = None

encoding = "utf-8"


def sbsbaker_get_command_args(cmd):
	help = subprocess.run([sbsbaker_exec, cmd, "--help"], stdout=subprocess.PIPE).stdout.decode(encoding)
	lines = help.splitlines()
	arg_lines = [l.strip().split() for l in lines if l.startswith("  --")]

	args = []
	for arg_line in arg_lines:
		cmd_arg_name = arg_line[0][2:]
		py_arg_name = cmd_arg_name.replace("-", "_")

		args.append({"py_name": py_arg_name, "name": cmd_arg_name})

	return args

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
		args = sbsbaker_get_command_args(cmd_name)
		py_cmd_name = cmd_name.replace("-", "_")
		cmds.append({"py_name": py_cmd_name, "name": cmd_name, "args": args})

	return cmds


def main():
	if len(sys.argv) != 2:
		print("Usage: " + sys.argv[0] + " [path to batch tools]")
		return 1

	global sbsbaker_exec

	tools_path = sys.argv[1]
	sbsbaker_exec = os.path.join(tools_path, "sbsbaker")

	print("sbsbaker:")
	sbsbaker_commands = sbsbaker_get_commands()

	jinja_env = jinja2.Environment(
		loader=jinja2.PackageLoader(__name__, "template"),
		autoescape=(["py"]))

	out_mod_dir = "substance_wrapper"
	os.makedirs(out_mod_dir, exist_ok=True)

	init_template = jinja_env.get_template("__init__.py")
	init_py = init_template.render()

	file = open(os.path.join(out_mod_dir, "__init__.py"), "w")
	file.write(init_py)
	file.close()

	sbsbaker_template = jinja_env.get_template("sbsbaker.py")
	sbsbaker_py = sbsbaker_template.render(sbsbaker_commands=sbsbaker_commands)

	file = open(os.path.join(out_mod_dir, "sbsbaker.py"), "w")
	file.write(sbsbaker_py)
	file.close()

	return 0


if __name__ == "__main__":
	r = main()
	sys.exit(r)
