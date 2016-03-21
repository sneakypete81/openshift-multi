Openshift Multi-App Environment
===============================

This is an Openshift Python WSGI application containing a number of apps.
Each app is pulled in as a git submodule.

Requests are routed to each app based on the subdomain. For example:
mobilator.peteburgers.tk is routed to the mobilator app.

###Configuration

The subdomain router needs to know the domain root:
```
rhc env set DOMAIN_ROOT=peteburgers.tk -a multi
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
