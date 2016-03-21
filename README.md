Openshift Multi-App Environment
===============================

This is an Openshift Python WSGI application containing a number of apps.
Requests are routed to each app based on the subdomain. For example:
mobilator.peteburgers.tk is routed to the mobilator app.

###Apps
 * [camlib](https://github.com/sneakypete81/camlib)

###Configuration

The subdomain router needs to know the domain root:
```
rhc env set DOMAIN_ROOT=peteburgers.tk -a multi
```

###Submodules
Each app is pulled in as a git submodule. Submodules are a bit tricky, so here's
an example workflow:

First pull in the latest versions of all submodules
```
# From the root repository:
git submodule update --remote
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

CamLib
------
Scrapings from Cambridgeshire Library eBooks with ratings from GoodReads.
https://github.com/sneakypete81/camlib

###Configuration

The hourly cron job needs to know where to find the scraper:
```
rhc env set CAMLIB_SCRAPER_REL_DIR=apps/camlib/tasks -a multi
```
