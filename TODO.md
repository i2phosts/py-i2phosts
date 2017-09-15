
TODO and ideas
==============

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
