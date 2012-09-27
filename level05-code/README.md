Many attempts have been made at creating a federated identity system for the web (see OpenID, for example). However, none of them have been successful. Until today.

The DomainAuthenticator is based off a novel protocol for establishing identities. To authenticate to a site, you simply provide it username, password, and pingback URL. The site posts your credentials to the pingback URL, which returns either "AUTHENTICATED" or "DENIED". If "AUTHENTICATED", the site considers you signed in as a user for the pingback domain.

You can check out the Stripe CTF DomainAuthenticator instance here: https://level05-2.stripe-ctf.com/user-XXXXXXXXXX. We've been using it to distribute the password to access Level 6. If you could only somehow authenticate as a user of a level05 machine...

To avoid nefarious exploits, the machine hosting the DomainAuthenticator has very locked down network access. It can only make outbound requests to other stripe-ctf.com servers. Though, you've heard that someone forgot to internally firewall off the high ports from the Level 2 server.

Interesting in setting up your own DomainAuthenticator? You can grab the source from git clone https://level05-2.stripe-ctf.com/user-XXXXXXXXXX/level05-code, or by reading on below. 

pingback url: https://level05-2.stripe-ctf.com/user-XXXXXXXXXX/?pingback=https://level02-3.stripe-ctf.com/user-XXXXXXXXXX/uploads/AUTHENTICATED

