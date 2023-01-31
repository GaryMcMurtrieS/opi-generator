import os
import toml


def get_attr_conf():
    """ Return a dict of the attribute map from BOY to BOB.

    Read default config from '/etc/opigen/attr.toml', if failed,
    read from '<package-directory>/config/attr.toml'.

    If 'attr.toml' exists in current working directory, read it
    to override the default config, otherwise, override with
    '~/.opigen/attr.toml' if available.
    """
    if os.path.isfile("/etc/opigen/attr.toml"):
        deployed_conf = toml.load("/etc/opigen/attr.toml")
    else:
        basedir = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(basedir, "attr.toml")
        deployed_conf = toml.load(path)
    # check if user-defined config exists
    _cwd_confpath = os.path.abspath("./attr.toml")
    if os.path.isfile(_cwd_confpath):
        _confpath = _cwd_confpath
    else:
        _user_confpath = os.path.expanduser("~/.opigen/attr.toml")
        if os.path.isfile(_user_confpath):
            _confpath = _user_confpath
        else:
            return deployed_conf
    # override
    _user_conf = toml.load(_confpath)
    for k, v in _user_conf.items():
        _d = deployed_conf.setdefault(k, {})
        for _k, _v in v.items():
            _d[_k] = _v
    return deployed_conf


def get_font_def_path():
    """ Get the absolute path of the font definition file, search and use any one of:
    - <current-working-directory>/font.def
    - ~/.opigen/font.def
    - <package-directory>/config/font.def
    
    Returns
    -------
    r : str
        The absolute path of the font definition file.
    """
    print(f"Found font def file: {_get_def_path('font.def')}")
    return _get_def_path('font.def')


def get_color_def_path():
    """ Get the absolute path of the color definition file, search and use any one of:
    - <current-working-directory>/color.def
    - ~/.opigen/color.def
    - <package-directory>/config/color.def
    
    Returns
    -------
    r : str
        The absolute path of the color definition file.
    """
    print(f"Found color def file: {_get_def_path('color.def')}")
    return _get_def_path('color.def')
 
    
def _get_def_path(filename):
    # current working directory
    _cwd_confpath = os.path.abspath(f"./{filename}")
    if os.path.isfile(_cwd_confpath):
        return _cwd_confpath
    # user home directory
    _user_confpath = os.path.expanduser(f"~/.opigen/{filename}")
    if os.path.isfile(_user_confpath):
        return _user_confpath
    # package deployed
    basedir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(basedir, filename)