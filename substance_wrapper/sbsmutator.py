
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


def edit(
		input=None,
		inputs=None,
		presets_path=None,
		alias=None,
		no_dependency=None,
		output_path=None,
		output_name=None,
		output_merge=None,
		input_graph=None,
		output_graph_name=None,
		output_graph_description=None,
		output_graph_category=None,
		output_graph_label=None,
		output_graph_author=None,
		output_graph_author_url=None,
		output_graph_tags=None,
		output_graph_physical_size=None,
		output_graph_user_data=None,
		output_graph_icon=None,
		connect_image=None,
		connect_input=None,
		remove_output=None,
		hide_parameters=None,
		hide_parameter=None,
		switch_to_constant=None,
		set_default_value=None,
		instantiate=None):

	sbsmutator_exec = get_tool_exec("sbsmutator")

	args = [sbsmutator_exec]
	
	if input:
		args.extend(["--input", str(input)])
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if presets_path:
		args.extend(["--presets-path", str(presets_path)])
	
	if alias:
		args.extend(["--alias", str(alias)])
	
	if no_dependency:
		args.extend(["--no-dependency", str(no_dependency)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_merge:
		args.extend(["--output-merge", str(output_merge)])
	
	if input_graph:
		args.extend(["--input-graph", str(input_graph)])
	
	if output_graph_name:
		args.extend(["--output-graph-name", str(output_graph_name)])
	
	if output_graph_description:
		args.extend(["--output-graph-description", str(output_graph_description)])
	
	if output_graph_category:
		args.extend(["--output-graph-category", str(output_graph_category)])
	
	if output_graph_label:
		args.extend(["--output-graph-label", str(output_graph_label)])
	
	if output_graph_author:
		args.extend(["--output-graph-author", str(output_graph_author)])
	
	if output_graph_author_url:
		args.extend(["--output-graph-author-url", str(output_graph_author_url)])
	
	if output_graph_tags:
		args.extend(["--output-graph-tags", str(output_graph_tags)])
	
	if output_graph_physical_size:
		args.extend(["--output-graph-physical-size", str(output_graph_physical_size)])
	
	if output_graph_user_data:
		args.extend(["--output-graph-user-data", str(output_graph_user_data)])
	
	if output_graph_icon:
		args.extend(["--output-graph-icon", str(output_graph_icon)])
	
	if connect_image:
		args.extend(["--connect-image", str(connect_image)])
	
	if connect_input:
		args.extend(["--connect-input", str(connect_input)])
	
	if remove_output:
		args.extend(["--remove-output", str(remove_output)])
	
	if hide_parameters:
		args.extend(["--hide-parameters", str(hide_parameters)])
	
	if hide_parameter:
		args.extend(["--hide-parameter", str(hide_parameter)])
	
	if switch_to_constant:
		args.extend(["--switch-to-constant", str(switch_to_constant)])
	
	if set_default_value:
		args.extend(["--set-default-value", str(set_default_value)])
	
	if instantiate:
		args.extend(["--instantiate", str(instantiate)])
	
	subprocess.run(args)

	return


def update(
		input=None,
		inputs=None,
		presets_path=None,
		alias=None,
		no_dependency=None,
		output_path=None,
		output_name=None):

	sbsmutator_exec = get_tool_exec("sbsmutator")

	args = [sbsmutator_exec]
	
	if input:
		args.extend(["--input", str(input)])
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if presets_path:
		args.extend(["--presets-path", str(presets_path)])
	
	if alias:
		args.extend(["--alias", str(alias)])
	
	if no_dependency:
		args.extend(["--no-dependency", str(no_dependency)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	subprocess.run(args)

	return