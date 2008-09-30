from distutils.core import setup
import py2exe

opts = {
    "py2exe": {
        "dist_dir": "..\\bin",
        "dist_dir": "..\\build",
    }
}

setup(
        name = "VeohProxy",
        version = "1.5",
        url = r'http://code.google.com/p/veohproxy',
        author = "Torben Gerkensmeyer",
        options = opts,
        console=[
                    {
                        "script":'default.py',
                        "icon_resources": [(1, r'..\res\VeohProxy.ico')]
                    }
                ]
)
