
import subprocess
import os.path

from . import get_tool_exec


def ambient_occlusion( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		normal=None,
		normal_world_space=None,
		normal_format=None,
		normal_invert=None,
		use_neighbors=None,
		quality=None,
		details=None,
		spread=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "ambient-occlusion"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if normal:
		args.extend(["--normal", str(normal)])
	
	if normal_world_space:
		args.extend(["--normal-world-space", str(normal_world_space)])
	
	if normal_format:
		args.extend(["--normal-format", str(normal_format)])
	
	if normal_invert:
		args.extend(["--normal-invert", str(normal_invert)])
	
	if use_neighbors:
		args.extend(["--use-neighbors", str(use_neighbors)])
	
	if quality:
		args.extend(["--quality", str(quality)])
	
	if details:
		args.extend(["--details", str(details)])
	
	if spread:
		args.extend(["--spread", str(spread)])
	
	subprocess.run(args)

	return


def ambient_occlusion_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		nb_second_rays=None,
		min_dist=None,
		max_dist=None,
		max_dist_relative_scale=None,
		spread_angle=None,
		ray_distrib=None,
		ignore_backface_secondary=None,
		self_occlusion=None,
		attenuation=None,
		normal=None,
		normal_world_space=None,
		normal_format=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "ambient-occlusion-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if nb_second_rays:
		args.extend(["--nb-second-rays", str(nb_second_rays)])
	
	if min_dist:
		args.extend(["--min-dist", str(min_dist)])
	
	if max_dist:
		args.extend(["--max-dist", str(max_dist)])
	
	if max_dist_relative_scale:
		args.extend(["--max-dist-relative-scale", str(max_dist_relative_scale)])
	
	if spread_angle:
		args.extend(["--spread-angle", str(spread_angle)])
	
	if ray_distrib:
		args.extend(["--ray-distrib", str(ray_distrib)])
	
	if ignore_backface_secondary:
		args.extend(["--ignore-backface-secondary", str(ignore_backface_secondary)])
	
	if self_occlusion:
		args.extend(["--self-occlusion", str(self_occlusion)])
	
	if attenuation:
		args.extend(["--attenuation", str(attenuation)])
	
	if normal:
		args.extend(["--normal", str(normal)])
	
	if normal_world_space:
		args.extend(["--normal-world-space", str(normal_world_space)])
	
	if normal_format:
		args.extend(["--normal-format", str(normal_format)])
	
	subprocess.run(args)

	return


def bent_normal_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		nb_second_rays=None,
		min_dist=None,
		max_dist=None,
		max_dist_relative_scale=None,
		spread_angle=None,
		ray_distrib=None,
		ignore_backface_secondary=None,
		self_occlusion=None,
		map_type=None,
		normal_invert=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "bent-normal-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if nb_second_rays:
		args.extend(["--nb-second-rays", str(nb_second_rays)])
	
	if min_dist:
		args.extend(["--min-dist", str(min_dist)])
	
	if max_dist:
		args.extend(["--max-dist", str(max_dist)])
	
	if max_dist_relative_scale:
		args.extend(["--max-dist-relative-scale", str(max_dist_relative_scale)])
	
	if spread_angle:
		args.extend(["--spread-angle", str(spread_angle)])
	
	if ray_distrib:
		args.extend(["--ray-distrib", str(ray_distrib)])
	
	if ignore_backface_secondary:
		args.extend(["--ignore-backface-secondary", str(ignore_backface_secondary)])
	
	if self_occlusion:
		args.extend(["--self-occlusion", str(self_occlusion)])
	
	if map_type:
		args.extend(["--map-type", str(map_type)])
	
	if normal_invert:
		args.extend(["--normal-invert", str(normal_invert)])
	
	subprocess.run(args)

	return


def color_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		color_source=None,
		color_generator=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "color-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if color_source:
		args.extend(["--color-source", str(color_source)])
	
	if color_generator:
		args.extend(["--color-generator", str(color_generator)])
	
	subprocess.run(args)

	return


def curvature( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		algorithm=None,
		normal=None,
		normal_world_space=None,
		normal_format=None,
		details=None,
		enable_seams=None,
		seams_power=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "curvature"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if algorithm:
		args.extend(["--algorithm", str(algorithm)])
	
	if normal:
		args.extend(["--normal", str(normal)])
	
	if normal_world_space:
		args.extend(["--normal-world-space", str(normal_world_space)])
	
	if normal_format:
		args.extend(["--normal-format", str(normal_format)])
	
	if details:
		args.extend(["--details", str(details)])
	
	if enable_seams:
		args.extend(["--enable-seams", str(enable_seams)])
	
	if seams_power:
		args.extend(["--seams-power", str(seams_power)])
	
	subprocess.run(args)

	return


def curvature_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		intensity=None,
		soft_saturate=None,
		maximize_range=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "curvature-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if intensity:
		args.extend(["--intensity", str(intensity)])
	
	if soft_saturate:
		args.extend(["--soft-saturate", str(soft_saturate)])
	
	if maximize_range:
		args.extend(["--maximize-range", str(maximize_range)])
	
	subprocess.run(args)

	return


def height_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		auto_normalize=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "height-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if auto_normalize:
		args.extend(["--auto-normalize", str(auto_normalize)])
	
	subprocess.run(args)

	return


def normal_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		map_type=None,
		normal_invert=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "normal-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if map_type:
		args.extend(["--map-type", str(map_type)])
	
	if normal_invert:
		args.extend(["--normal-invert", str(normal_invert)])
	
	subprocess.run(args)

	return


def normal_world_space( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		normal=None,
		normal_format=None,
		normal_type=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "normal-world-space"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if normal:
		args.extend(["--normal", str(normal)])
	
	if normal_format:
		args.extend(["--normal-format", str(normal_format)])
	
	if normal_type:
		args.extend(["--normal-type", str(normal_type)])
	
	subprocess.run(args)

	return


def opacity_mask_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "opacity-mask-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	subprocess.run(args)

	return


def position( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		mode=None,
		axis=None,
		normalization=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "position"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if mode:
		args.extend(["--mode", str(mode)])
	
	if axis:
		args.extend(["--axis", str(axis)])
	
	if normalization:
		args.extend(["--normalization", str(normalization)])
	
	subprocess.run(args)

	return


def position_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		mode=None,
		axis=None,
		normalization=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "position-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if mode:
		args.extend(["--mode", str(mode)])
	
	if axis:
		args.extend(["--axis", str(axis)])
	
	if normalization:
		args.extend(["--normalization", str(normalization)])
	
	subprocess.run(args)

	return


def texture_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		texture_file=None,
		high_poly_uv_set=None,
		filtering_mode=None,
		normal_map=None,
		map_type=None,
		normal_invert=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "texture-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if texture_file:
		args.extend(["--texture-file", str(texture_file)])
	
	if high_poly_uv_set:
		args.extend(["--high-poly-uv-set", str(high_poly_uv_set)])
	
	if filtering_mode:
		args.extend(["--filtering-mode", str(filtering_mode)])
	
	if normal_map:
		args.extend(["--normal-map", str(normal_map)])
	
	if map_type:
		args.extend(["--map-type", str(map_type)])
	
	if normal_invert:
		args.extend(["--normal-invert", str(normal_invert)])
	
	subprocess.run(args)

	return


def thickness_from_mesh( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		highdef_mesh=None,
		use_cage=None,
		cage_mesh=None,
		max_frontal=None,
		max_rear=None,
		relative_to_bbox=None,
		average_normals=None,
		ignore_backface=None,
		match=None,
		antialiasing=None,
		nb_second_rays=None,
		min_dist=None,
		max_dist=None,
		max_dist_relative_scale=None,
		spread_angle=None,
		ray_distrib=None,
		ignore_backface_secondary=None,
		self_occlusion=None,
		auto_normalize=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "thickness-from-mesh"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if highdef_mesh:
		args.extend(["--highdef-mesh", str(highdef_mesh)])
	
	if use_cage:
		args.extend(["--use-cage", str(use_cage)])
	
	if cage_mesh:
		args.extend(["--cage-mesh", str(cage_mesh)])
	
	if max_frontal:
		args.extend(["--max-frontal", str(max_frontal)])
	
	if max_rear:
		args.extend(["--max-rear", str(max_rear)])
	
	if relative_to_bbox:
		args.extend(["--relative-to-bbox", str(relative_to_bbox)])
	
	if average_normals:
		args.extend(["--average-normals", str(average_normals)])
	
	if ignore_backface:
		args.extend(["--ignore-backface", str(ignore_backface)])
	
	if match:
		args.extend(["--match", str(match)])
	
	if antialiasing:
		args.extend(["--antialiasing", str(antialiasing)])
	
	if nb_second_rays:
		args.extend(["--nb-second-rays", str(nb_second_rays)])
	
	if min_dist:
		args.extend(["--min-dist", str(min_dist)])
	
	if max_dist:
		args.extend(["--max-dist", str(max_dist)])
	
	if max_dist_relative_scale:
		args.extend(["--max-dist-relative-scale", str(max_dist_relative_scale)])
	
	if spread_angle:
		args.extend(["--spread-angle", str(spread_angle)])
	
	if ray_distrib:
		args.extend(["--ray-distrib", str(ray_distrib)])
	
	if ignore_backface_secondary:
		args.extend(["--ignore-backface-secondary", str(ignore_backface_secondary)])
	
	if self_occlusion:
		args.extend(["--self-occlusion", str(self_occlusion)])
	
	if auto_normalize:
		args.extend(["--auto-normalize", str(auto_normalize)])
	
	subprocess.run(args)

	return


def uv_map( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		padding=None,
		mode=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "uv-map"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if padding:
		args.extend(["--padding", str(padding)])
	
	if mode:
		args.extend(["--mode", str(mode)])
	
	subprocess.run(args)

	return


def world_space_direction( 
		inputs=None,
		input_selection=None,
		output_name=None,
		output_path=None,
		output_format=None,
		output_format_compression=None,
		tangent_space_plugin=None,
		per_fragment_binormal=None,
		name_suffix_low=None,
		name_suffix_high=None,
		output_size=None,
		uv_set=None,
		dilation_width=None,
		apply_diffusion=None,
		direction=None,
		normal_format=None,
		direction_x=None,
		direction_y=None,
		direction_z=None,
		direction_file=None):

	sbsbaker_exec = get_tool_exec("sbsbaker")

	args = [sbsbaker_exec, "world-space-direction"]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if input_selection:
		args.extend(["--input-selection", str(input_selection)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if output_format:
		args.extend(["--output-format", str(output_format)])
	
	if output_format_compression:
		args.extend(["--output-format-compression", str(output_format_compression)])
	
	if tangent_space_plugin:
		args.extend(["--tangent-space-plugin", str(tangent_space_plugin)])
	
	if per_fragment_binormal:
		args.extend(["--per-fragment-binormal", str(per_fragment_binormal)])
	
	if name_suffix_low:
		args.extend(["--name-suffix-low", str(name_suffix_low)])
	
	if name_suffix_high:
		args.extend(["--name-suffix-high", str(name_suffix_high)])
	
	if output_size:
		args.extend(["--output-size", str(output_size)])
	
	if uv_set:
		args.extend(["--uv-set", str(uv_set)])
	
	if dilation_width:
		args.extend(["--dilation-width", str(dilation_width)])
	
	if apply_diffusion:
		args.extend(["--apply-diffusion", str(apply_diffusion)])
	
	if direction:
		args.extend(["--direction", str(direction)])
	
	if normal_format:
		args.extend(["--normal-format", str(normal_format)])
	
	if direction_x:
		args.extend(["--direction-x", str(direction_x)])
	
	if direction_y:
		args.extend(["--direction-y", str(direction_y)])
	
	if direction_z:
		args.extend(["--direction-z", str(direction_z)])
	
	if direction_file:
		args.extend(["--direction-file", str(direction_file)])
	
	subprocess.run(args)

	return

