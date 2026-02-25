Newest verion is now a direct DFavinci Resolve Plugin.
1. Place the .lua file in the following location:
   Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Utility\
   Mac: ~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility/
2. Restart Davinci Resolve
3. Open your timeline and go to: Workspace → Scripts → Utility → mark2markers
4. Select your .mark file


How I use this is as follows:

1. Copy the .mp4 and the <filename>.data/<filename>.mark from the sd card into a folder on my mac
2. run this script in the folder, it will detect all .mark files and convert them to edl
3. load the mp4 into davinci resolve
4. create a timeline for it
5. right click on the timeline in the Media Pool, go to Timelines\Import\Timeline Markers from EDL
6. Select the EDL file created from this script
7. Next go to Index to see your markers.

Right now they will all be named CLICK because that is what XbotGo names them in their file.
