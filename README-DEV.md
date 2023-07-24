To test, build a local wheel and serve it over HTTP, to pip can install it:

```
sh serve-local-wheel.sh
```

In another terminal, try to install your package using `setuptools_ocrd` (in the build requires):

```
cd ~/devel/another_project
pip install --extra-index-url http://127.0.0.1:28486/ .
```
