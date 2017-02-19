
import subprocess
import os.path

from . import get_tool_exec


encoding = "utf-8"


def info(input):
	sbsrender_exec = get_tool_exec("sbsrender")

	info = subprocess.run([sbsrender_exec, "info", "--input", input], stdout=subprocess.PIPE).stdout.decode(encoding)

	return info


def render(
		inputs=None,
		input_graph=None,
		input_graph_output=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		set_value=None,
		set_entry=None,
		use_preset=None,
		engine=None,
		memory_budget=None):

	sbsrender_exec = get_tool_exec("sbsrender")

	args = [sbsrender_exec, "render"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_graph:
		args.extend(["--input-graph", str(input_graph)])
	
	if input_graph_output:
		args.extend(["--input-graph-output", str(input_graph_output)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if set_value:
		args.extend(["--set-value", str(set_value)])
	
	if set_entry:
		args.extend(["--set-entry", str(set_entry)])
	
	if use_preset:
		args.extend(["--use-preset", str(use_preset)])
	
	if engine:
		args.extend(["--engine", str(engine)])
	
	if memory_budget:
		args.extend(["--memory-budget", str(memory_budget)])
	
	subprocess.run(args)

	return
