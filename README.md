# Python Wrapper for Substance Batchtools
**Disclaimer:** This software is not endorsed or certified by Allegorithmic.

This is an auto-generated wrapper for the **Substance Batchtools** by Allegorithmic for **Python 3**.
It exposes the functionality of the command line tools in the form of Python functions
in order to integrate them into other applications such as Blender.

It has been tested with version 6.0.0 of the tools. Please note that a valid Substance Designer license is required to use the Batchtools.

## Usage
Here is an example on how to use it:

```python
import substance_wrapper as sbs

# set path to the tools
sbs.tools_path = "/path/to/Substance_BatchTools-6"

# bake 2048x2048 ambient occlusion to test_ambient-occlusion.png
sbs.sbsbaker.ambient_occlusion("test.fbx", output_size="11,11")

# bake a normal map
sbs.sbsbaker.normal_from_mesh("test.fbx", highdef_mesh="test_hp.fbx", output_size="11,11")

# print info about sbs file
print(sbs.sbsmutator.info(inputs="test.sbs"))

# cook test.sbs into test.sbsar
sbs.sbscooker(inputs="test.sbs")

# print info about test.sbsar
print(sbs.sbsrender.info("test.sbsar"))

# generate images from sbsar
sbs.sbsrender.render("test.sbsar")
```

## Installing
The package can be installed using the provided distutils script:
```
python3 setup.py build
sudo python3 setup.py install
```

## Generating the Wrapper
As mentioned above, the wrapper is mostly auto-generated. This is done by parsing the --help output from the command line tools.
A pre-generated wrapper is already provided in this repository, so most users can just ignore this part.

To use the generator, jinja2 is required to be installed. Then, the wrapper can be generated like this:
```
python3 generate-wrapper.py /path/to/Substance_BatchTools-6
```

## About
Created by Florian Märkl: https://www.metallic-entertainment.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.