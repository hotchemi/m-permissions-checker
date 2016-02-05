# m-permissions-checker

[![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-m--permissions--checker-green.svg?style=flat)](https://android-arsenal.com/details/1/2074)

With this tiny script, you can check whether you have to handle your app's permission or not in [Android M](http://developer.android.com/preview/index.html).

## What is Runtime Permissions?

For the detail, please dive into [Android Developers](http://developer.android.com/preview/features/runtime-permissions.html).

## Install

Just clone this repository or download the python file.

## Usage

Only you have to do is just executing below command on your root app directory.

```sh
$ cd <root your app>
$ python permissions_checker.py

> Searching file: /Users/hoge/test/data/AndroidManifest.xml
> Unfortunately, you have to handle these permissions in MNC.
> android.permission.READ_CALENDAR
> android.permission.WRITE_CALENDAR
> android.permission.CAMERA
```

> Of course this script excludes build output directory like `build`.

## Caution

This script doesn't check custom permission's dangerousness. So please check them by your hand.

## Support

Python 2.7.

## Contribute

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
