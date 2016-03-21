OpenShift Multi-App Environment
===============================

This is an OpenShift Python WSGI application containing a number of apps.
Requests are routed to each app based on the subdomain. For example:
http://mobilator.peteburgers.tk is routed to the mobilator app.

### Apps

 * [camlib](https://github.com/sneakypete81/camlib)
 * [mobilator](https://github.com/sneakypete81/mobilator)

### Configuration

The subdomain router needs to know the domain root:
```
rhc env set DOMAIN_ROOT=peteburgers.tk -a multi
```

### Dependencies

The master list of Python dependencies is in `requirements.txt`. This needs to be
manually updated as each app's dependencies change.

The initial OpenShift virtualenv setup takes a long time, and git push hangs up
before it completes. You'll need to ssh in and run the setup process manually:
```
ssh xxxxxx@multi-sneakypete81.rhcloud.com
pip install -r app-root/repo/requirements.txt
```

### Submodules

Each app is pulled in as a git submodule. Submodules are a bit tricky, so here's
an example workflow:

First pull in the latest versions of all submodules:
```
# From the root repository:
git submodule update --remote
# or:
git submodule update --remote --merge
```

Make sure the URL of each submodule is changed use SSH rather than HTTPS:
```
cd apps/camlib
git remote set-url origin git@github.com:sneakypete81/camlib.git
```

Now make sure we're working on the master branch of the submodule
(not a detached head):
```
cd apps/camlib
git checkout master
```

Make changes, committing as necessary. Then when you're ready to publish, push
everything (including updated submodules):
```
# From the root repository:
git push --recurse-submodules=on-demand
```

### Multiple Origins

To push to both GitHub and OpenShift simultaneously, configure as follows:
```
git remote set-url origin --push --add git@github.com:sneakypete81/openshift-multi.git
git remote set-url origin --push --add ssh://xxxxxx@multi-sneakypete81.rhcloud.com/~/git/multi.git/
git push
```

App Details
-----------

### CamLib

Scrapings from Cambridgeshire Library eBooks with ratings from GoodReads.
https://github.com/sneakypete81/camlib

#### Configuration

The hourly cron job needs to know where to find the scraper:
```
rhc env set CAMLIB_SCRAPER_REL_DIR=apps/camlib/tasks -a multi
```

### Mobilator

Converts links inside RSS/Atom feeds to point to a mobile-friendly version of the target site.
