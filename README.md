py-i2phosts
===========

Description
-----------
**py-i2phosts** is a hostnames registration engine for I2P.

It consists of django app and python scripts. All base features are implemented. Project is ready for production use.
You can see working instances of py-i2phosts here : http://inr.i2p/ and http://no.i2p/

Features
--------
* Web interface is made using django (a set of templates included)
    * Hosts submission page with local policy and form with fields Hostname, Destination and Description
    * Page for verification of upper-level domain when addind a subdomain
    * Index page
    * Navigation menu
    * Language switcher, multi-language interface (currently available in english and russian)
    * Browsing alive and recently added hosts (URLs are provided with addresshelpers)
    * RSS feeds for all active hosts and freshly added hosts
    * Searching by hostname
* Admin interface (via django admin) features:
    * browsing all hosts with various filtering and ordering options
    * manual hosts editing and approving recently added hosts
    * preview b32 links for all hosts
    * managing external sources from which hosts.txt should be fetched
* Validation of hostname and destination as described in I2P naming rules both in web interface and in admin interface. Also some additional validation (see http://zzz.i2p/topics/739 for details) is present in web interface.
* Injector program: it parses hosts.txt files and adds hosts from them into database
* hosts.txt fetcher: it fetches hosts.txt from another services and runs injector on them. Fetcher uses Last-Modified and ETag http headers for safe bandwith.
* Hosts checker: it does availability check of each host using SAM python interface and updates "last seen" timestamp in database
* hosts.txt builder: it queries database and builds a hosts.txt file
* Hosts maintainer: it implements logic for all host-maintainance operations (activating, deactivating, deleting, setting expiration date)
* Master daemon: it runs as unix daemon and periodically launches all other py-i2phosts programs.
* All scripts (except injector and builder) can write all activity to log files. Web interface can log all submission attempts and all validation errors.
* All scripts are supports command-line options and config files
* Built-in jump service
* Install script (using distutils)

Source code
-----------
Sources available in 2 places:
* github: https://github.com/i2phosts/py-i2phosts
* git.repo.i2p: http://git.repo.i2p/w/py-i2phosts.git

Documentation
-------------

* [How to deploy for development](DEVEL)
* [Architecture overview](ARCH)

TODO and ideas
--------------
**Web interface**
* Add hostname reservation feature into admin interface
* Improve design
* Add categorisation by tags
* Add news
* Lookup tool b32->b64 in web-interface
* Add option "share subdomains" to add form: everyone will be permitted to add subdomains in this domain
* Register multiple subdomains in the same time with primary domain registration
* Search: show b32 also
* Implement flexible API for exchanging between registrators
* Show meaningfull error pages instead of redirects to /

**Internals**
* Parallel lookups in checker
* Add "last probe" timestamp for hosts. It will help to reduce lookups frequency for inactive hosts.
* Display "key conflict" errors in admin interface or send email to admin
* Probe alive hosts for http service, and provide http:// links at browse page only for them
* Implement json-rpc API for inter-registration services communications.

**Other**
* Write some documentation ("how it works" for each component, INSTALL, README and so on)
