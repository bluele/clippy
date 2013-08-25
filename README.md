# Clippy

A Cross-platform clipboard command for Linux, MacOSX, etc...

This script use [pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/).

## Install

```sh
 $ curl https://raw.github.com/bluele/clippy/master/install.py | python
```

## Usage

```sh
 # Get the data from clipboard and writes it to the stdout.
 $ clippy

 # Take the stdout input in clipboard.
 $ echo "hello, world" | clippy
```

## Copyright

This software is licensed under the BSD License.