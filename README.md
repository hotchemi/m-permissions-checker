# m-permissions-checker

With this tiny script, you can check whether you have to handle your app permission or not in Android M.

## What is app permissions?

Please read [Android Developers](http://developer.android.com/preview/features/runtime-permissions.html).

## Usage

Only you have to do is just executing below command on your root app directory.

```sh
$ cd <root your app>
$ python permissions_checker.py

> Unfortunately, you have to handle these permissions in MNC.
> android.permission.READ_CALENDAR
> android.permission.WRITE_CALENDAR
> android.permission.CAMERA
```

## Support

Over Python 2.7.

## Contribute

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
