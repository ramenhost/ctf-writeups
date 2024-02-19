## rev/the-secret-of-java-island

The Secret of Java Island is a 2024 point-and-click graphic adventure game developed and published by LA CTF Games. It takes place in a fictional version of Indonesia during the age of hacking. The player assumes the role of Benson Liu, a young man who dreams of becoming a hacker, and explores fictional flags while solving puzzles.

**Given:** `game.jar`

### Solution
Game story to get flag:  
    1. Go to computer.  
    2. Perform exploit sequence (left/right buttons) to get glove.  
    3. Go to lever to get the flag.

Decompile `game.jar` using JD-GUI to find this.
```java
case 4:
        if (paramInt == 0) {
          exploit += "d";
          story.setText("You clobbered the DOM. That was exploit #" + exploit.length() + ".");
        } else {
          exploit += "p";
          story.setText("You polluted the prototype. That was exploit #" + exploit.length() + ".");
        } 
        if (exploit.length() == 8)
          try {
            MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
            if (!Arrays.equals(messageDigest.digest(exploit.getBytes("UTF-8")), new byte[] { 
                  69, 70, -81, -117, -10, 109, 15, 29, 19, 113, 
                  61, -123, -39, 82, -11, -34, 104, -98, -111, 9, 
                  43, 35, -19, 22, 52, -55, -124, -45, -72, -23, 
                  96, -77 })) {
              state = 7;
            } else {
              state = 6;
            } 
            updateGame();
          } catch (Exception exception) {
            throw new RuntimeException(exception);
          }  
        return;
      case 5:
```

#### Brute force exploit sequence:
The code checks hash of button press history.  
Left button - d  
Right button - p  
The history string of length 8 containing d and p should match SHA256 digest `4546af8bf66d0f1d13713d85d952f5de689e91092b23ed1634c984d3b8e960b3`.
Brute force the hash using `hash_solve.sh` to find the correct sequence of left/right button and apply it in game.
