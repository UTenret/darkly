### Flag 00

http://localhost:13080/?page=survey
Inspect option of Ben
Change value to 11 (negative didn't work)
03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA

### Flag 01 (WIP)

5 UNION SELECT COUNT(*), NULL FROM users -- 
5 UNION SELECT COUNT(*), first_name FROM users --

### Flag 02

http://localhost:13080/index.php?page=recover
Change webmaster@borntosec.com to whatever
1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

### Flag 03

http://localhost:13080/index.php?page=feedback
Name: a
0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E