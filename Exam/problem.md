## Exam Python M2

Create Python UI application that will:
* retrieve timezones from this link: (50p) 
  * http://worldtimeapi.org/api/timezone
* Allow the user to select a timezone and open a new window indicating the time in the selected timezone using this link: (50p)
  *  http://worldtimeapi.org/api/timezone/<area>/<zone>
Detailed description:
  - all windows must have title (5p)
  - all modules classes and methods must be documented (10p)
  - type hints should be used whenever possible (5p)
  - at least two unittests created for at lest one function (20p)
  - all timezones are displayed. (30p)
  - each timezone clicked will open a new window and show time in that timezone (20p)
  - retrieving time to display is done async or in separate thread or process (10p)

Note: You can choose to pack new Frame or open new window for each displayed time. 
For new window you can use tkinter.TopLevel(main_window)

