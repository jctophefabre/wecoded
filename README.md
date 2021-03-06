# WeCoded

WeCoded is a Python tool for counting contributed lines by authors on multiple git repositories.


## Installation


WeCoded requires Python 3.6 (or higher) and can be installed using the pip/pip3 tool

```sh
pip3 install wecoded
```

## Usage

WeCoded is run as a command line program with arguments. 
It performs the cloning of the repositories then it computes and agregates the lines count statistics as a CSV file.


### Prerequisites

WeCoded needs the following external tools:

* the `git` command line
* the [git-extras](https://github.com/tj/git-extras) extension

_Currently, WeCoded has only be tested on Linux system_


### Configuration file 

WeCoded requires a configuration file defining 

* git repositories to clone and explore
* authors aliases (optional)

Each repository is defined by a name with an associated URL and an optional revision to checkout. 
The revision can be a branch name, a tag or even a commit SHA1.
If no revision is provided, the default repository branch is checked out.  
Aliases for authors can be defined to avoid separate counting of the same author 
who has commited under various forms of his name (e.g. 'John Doe', 'jdoe', 'J. Doe').

```yaml
repositories:
  - name: a-repos
    url: https://organization.org/gitrepos/arepos
    revision: v3.2.0
  - name: another-repos
    url: https://organization.org/gitrepos/anotherrepos
  - name: extrarepos
    url: https://company.com/git/extra
    revision: develop

authors:
  - name: 'John Doe'
    aliases: 
      - 'J. Doe'
      - 'jdoe'
  - name: 'Erika Mustermann'
    aliases: 
      - 'emustermann'
```

Examples of real configuration files are provided in the [examples](https://github.com/jctophefabre/wecoded/tree/master/examples) directory.


### Command line

To execute the WeCoded tool in a given work directory, run the following command:
```sh
wecoded /path/to/work/dir
```
in this case, WeCoded will try to use a `wecoded-config.yaml` file in the current directory.  


To specify a configuration file path, use the `-f` / `--config-file` option
```sh
wecoded /path/to/work/dir -f /path/to/wecoded-myconfig.yaml
```

The complete help on command line arguments can be obtained in a terminal using the `wecoded --help` command:
```txt
usage: wecoded [-h] [-f CONFIG_FILE] [-c] [-s] workpath

A tool for contributions stats by authors on multiple git repositories

positional arguments:
  workpath              the work path

optional arguments:
  -h, --help            show this help message and exit
  -f CONFIG_FILE, --config-file CONFIG_FILE
                        the path to the YAML configuration file (default: /path/to/wecoded-config.yaml)
  -c, --no-clone        disable the cloning of remote repositories
  -s, --no-stats        disable the computation of stats
```


## Author and License

The WeCoded package is developped by [Jean-Christophe Fabre](https://github.com/jctophefabre).  
it is distributed under the terms of the [MIT license](https://github.com/jctophefabre/wecoded/blob/master/LICENSE)