# _ChRIS_ ds Plugin Template

<!--
[![Version](https://img.shields.io/docker/v/fnndsc/pl-appname?sort=semver)](https://hub.docker.com/r/fnndsc/pl-appname)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-appname)](https://github.com/FNNDSC/pl-appname/blob/main/LICENSE)
[![Build](https://github.com/FNNDSC/pl-appname/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-appname/actions)
-->


This is a minimal template repository for _ChRIS_ _ds_ plugin applications.
For a more comprehensive boilerplate, use

https://github.com/fnndsc/cookiecutter-chrisapp

## How to Use This Template

1. Click "Use this template"
2. Clone the newly created repository
3. Replace placeholder text

```shell
function replace () {
  find . -type f -not -path '*/\.*/*' -not -path '*/\venv/*' -exec sed -i -e "s/$1/$2/g" '{}' \;
}

replace commandname my_command_name
replace pl-appname pl-my-plugin-name
replace fnndsc my_username
```

### Template Examples

Here are some good, complete examples of _ChRIS_ plugins created from this template.

- https://github.com/FNNDSC/pl-nums2mask
- https://github.com/FNNDSC/pl-nii2mnc-u8

Advanced users can `cp -rv .github/workflows` into their own repositories to enable
automatic builds.

## Abstract

PROGRAMNAME is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in ...  as input files and
creates ... as output files.

## Usage

```shell
singularity exec docker://fnndsc/pl-appname commandname [--args values...] input/ output/
```

## Examples

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
singularity exec docker://fnndsc/pl-appname:latest commandname [--args] incoming/ outgoing/
```

## Development

### Building

```shell
docker build -t localhost/fnndsc/pl-appname .
```

### Get JSON Representation

```shell
docker run --rm localhost/fnndsc/pl-appname chris_plugin_info > MyProgram.json
```

### Local Test Run

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/app.py:/usr/local/lib/python3.10/site-packages/app.py:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/fnndsc/pl-appname commandname /incoming /outgoing
```
