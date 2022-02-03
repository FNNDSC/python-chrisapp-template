# _ChRIS_ ds Plugin Template

<!--
[![Version](https://img.shields.io/docker/v/fnndsc/pl-appname?sort=semver)](https://hub.docker.com/r/fnndsc/pl-appname)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-appname)](https://github.com/FNNDSC/pl-appname/blob/main/LICENSE)
[![Build](https://github.com/FNNDSC/pl-appname/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-appname/actions)
-->


This is a minimal template repository for _ChRIS_ _ds_ plugin applications.
For a more comprehensive boilerplate, use

https://github.com/fnndsc/cookiecutter-chrisapp

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
singularity exec docker://fndsc/pl-appname:latest commandname [--args] incoming/ outgoing/
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
