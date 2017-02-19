
import subprocess
import os.path

from . import get_tool_exec


def sbscooker(
		inputs=None,
		includes=None,
		alias=None,
		output_name=None,
		output_path=None,
		merge=None,
		no_archive=None,
		no_optimization=None,
		size_limit=None,
		expose_output_size=None,
		expose_random_seed=None,
		expose_pixel_size=None,
		compression_mode=None):

	sbscooker_exec = get_tool_exec("sbscooker")

	args = [sbscooker_exec]
	
	if inputs:
		args.extend(["--inputs", str(inputs)])
	
	if includes:
		args.extend(["--includes", str(includes)])
	
	if alias:
		args.extend(["--alias", str(alias)])
	
	if output_name:
		args.extend(["--output-name", str(output_name)])
	
	if output_path:
		args.extend(["--output-path", str(output_path)])
	
	if merge:
		args.extend(["--merge", str(merge)])
	
	if no_archive:
		args.extend(["--no-archive", str(no_archive)])
	
	if no_optimization:
		args.extend(["--no-optimization", str(no_optimization)])
	
	if size_limit:
		args.extend(["--size-limit", str(size_limit)])
	
	if expose_output_size:
		args.extend(["--expose-output-size", str(expose_output_size)])
	
	if expose_random_seed:
		args.extend(["--expose-random-seed", str(expose_random_seed)])
	
	if expose_pixel_size:
		args.extend(["--expose-pixel-size", str(expose_pixel_size)])
	
	if compression_mode:
		args.extend(["--compression-mode", str(compression_mode)])
	
	subprocess.run(args)

	return
