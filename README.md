This is a demo of the seems like cache bug of [mypy](https://github.com/python/mypy).

The issue is that in particular configuration of packages and files and imports mypy doesn't report a type issue when it previously type-checked the file and the check was correct.

You can see the list of steps to reproduce in bin/test. Shortly it is this:
1. `mypy -p main -p src` fails because src.lib.protocols.connection.Connection contains the `not_exists` property while src.app.APIConnection does not have it.
2. We remove this property from protocol, run mypy (it will succeed), and then we return this `not_exists` property back.
3. `mypy -p main -p src` would succeed while it is expected to fail as on step 1.

Run:
```
bin/setup
bin/test
```
