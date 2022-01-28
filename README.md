# _ChRIS_ ds Plugin Template

This is a minimal template repository for _ChRIS_ _ds_ plugin applications.
For a more comprehensive boilerplate, use

https://github.com/fnndsc/cookiecutter-chrisapp

## Abstract

PROGRAMNAME is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in ...  as input files and
creates ... as output files.

## Building

```shell
docker build -t localhost/fnndsc/pl-programname .
```

### Get JSON Representation

```shell
docker run --rm localhost/fnndsc/pl-programname chris_plugin_info > MyProgram.json
```


## Usage

```shell
singularity exec fnndsc/pl-programname commandname [--args values...] input/ output/
```

## Examples

```shell

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
singularity exec docker://fndsc/pl-programname:latest programname [--args] incoming/ outgoing/
```
```
