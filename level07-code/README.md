Welcome to the penultimate level, Level 7.

WaffleCopter is a new service delivering locally-sourced organic waffles hot off of vintage waffle irons straight to your location using quad-rotor GPS-enabled helicopters. The service is modeled after TacoCopter, an innovative and highly successful early contender in the airborne food delivery industry. WaffleCopter is currently being tested in private beta in select locations.

Your goal is to order one of the decadent Liège Waffles, offered only to WaffleCopter's first premium subscribers.

Log in to your account at https://level07-2.stripe-ctf.com/user-tjzmiaerww with username ctf and password password. You will find your API credentials after logging in. You can fetch the code for the level via
git clone https://level07-2.stripe-ctf.com/user-tjzmiaerww/level07-code, or you can read it below. You may find the sample API client in client.py particularly helpful. 

i did a sha padding attack based on https://blog.whitehatsec.com/hash-length-extension-attacks/ my crafted post lets me order as user 2: requests.post("https://level07-2.stripe-ctf.com/user-tjzmiaerww//orders", data="count=2&lat=42.39561&user_id=2&long=-71.13051&waffle=dream\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02@&waffle=liege|sig:e413eb4b487fbd8f55477d1857c6540cac814fe6")
