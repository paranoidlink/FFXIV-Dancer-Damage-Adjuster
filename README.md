FFXIV Dancer Damage Adjuster

A tool I made to help with solo practice on Dancer, it will take the amount of Espirit that your party and dancer partner generate and figure out how many saber dance casts were missed because of this.

This is currently calibrated to my static in order to calibrate it for yourself you'll need to go to the Dancer Gear Calculator: https://docs.google.com/spreadsheets/d/1C13bsFedHyR0l6YJhqahfjOlQpTPCpCRL9TdItD-Jk4/edit#gid=1985340945 and adjust the variables party and partner to be the Espirit Generated from Dance Partner and Party respectively divided by 121.
It is also calibrated to my character in order to calibrate it to you, you'll need to go and do at least 10 saber dances on a target dummy and take the average damage from these casts (total damage from all casts / amount of casts) and then make this amount the damage variable, you'll also want to do the same for cascade and make the cascadeDamage variable this amount

When running the program it will ask you how long the fight lasted in seconds and then how much dps you did, once you input both of these it will do some math to replace the gcd's that could of been sabre dance if you were in a full group and adjust your dps to reflect this.

A few notes:
This program does assume that your entire static and dance partner are playing completely optimally to generate as much Espirit as possible and that you wouldn't miss any of these casts
It also assumes that sabre dance would always replace a cascade cast because making a full rotation simulator was outside the scope of this project so the adjusted dps would likely be a bit higher than what you would of actually got