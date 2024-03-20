# PC Innovation Insitute 24 Badge
 Base files and instructions for using and hacking this year's Innovation Institute Badge

## What is it?
This year's Innovation Institute badge is following the example of badges from coding and hacking conferences and including a programmable screen. If it can be programmed, it can be hacked! The screen and the board it is attached to are a [Pimoroni Badger 2040](https://shop.pimoroni.com/products/badger-2040?variant=39752959852627), which supports a 2.9", 296 X 128 pixel E Ink display which retains an image even without being plugged in to power. The Badger also has a number of interfaces, including 5 front buttons, and 2 back buttons, a USB-c port for power and programming, a battery connector, and even a STEMMA connector for adding sensors. The "brains" of the Badger is a [Raspberry Pi 2040](https://www.raspberrypi.com/products/rp2040/) microcontroller which can be easily programmed (or reprogrammed) with MicroPython.

## Using the Badge "As-is"
Along with your name, school, and position, your badge comes with a few built in apps which give you helpful information for the Innovation Institute.
1. To use the screen and built in apps, you must first power up your badge. You can do so by either plugging your badge into a laptop or charger using a standard USBC cable, or you can use the battery pack supplied in your conference bag. Be sure to turn the batter pack's power on!
2. To access the app menu screen, press the "A" and "C" buttons on the bottom of the badge at the same time.
3. Once in the menu, you can change pages and find more apps with the up and down buttons on the right side of the badge, and select an app with the corresponding buttons on the bottom of the badge.
4. To return the badge to it's original screen, just select the "Badge" app.

## Hacking your Badge
If you can, attend [Session 1A: Programming Your Badger](https://tenthannualinnovationinstit2024.sched.com/event/1T3we/session-1a-programming-your-badger) where we will learn the basics of how the code in the badge works and how you can modify it. In case you can't make it to the session, or if you want to dive in and learn more after the Institute is over, start with [Pimoroni's Getting Started with Badger 2040](https://learn.pimoroni.com/article/getting-started-with-badger-2040) guide. With a little Python knowlede, you can program the badge to do amazing things!
This Github repository contains the code saved your badge (except for your personalized name and school) in case you mess something on your actuall badge and need to start over. 


